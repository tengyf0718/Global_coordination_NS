import arcpy
from arcpy import env
from arcpy.sa import *
import pandas as pd
import os

# ================= Replace these =================
workspace = r"F:\Yifan Teng\Data_new"
env.workspace = workspace
env.overwriteOutput = True

countries_fc = r"F:\Yifan Teng\Data_new\MID_DATA.gdb\Countr_ne50m_Moll"   # 国家矢量
country_id_field = "SOVEREIGNT"    # 用于匹配Excel的国家ID字段
excel_path = r"F:\Yifan Teng\Data_new\Results\NL2020_COUNT.xls"
excel_sheet = "NL_SCALE_FACTOR2020_GDP"
scale_field_name = "SCALE_FACTOR"  # Excel中的列名（将写入到矢量的字段）
nightlight_raster = r"F:\Yifan Teng\Data_new\MID_IMAGE.gdb\NL2020_Moll" # NL
out_scale_raster = r"F:\Yifan Teng\Data_new\MID_IMAGE.gdb\scale_raster_2020GDP" # scale factor
out_corrected = r"F:\Yifan Teng\Data_new\MID_IMAGE.gdb\NL_CORRECTION_2020GDP_Moll"
# =================================================

# 检查 Spatial Analyst 扩展
arcpy.CheckOutExtension("Spatial")

# 1) 读取 Excel -> pandas
df = pd.read_excel(excel_path, sheet_name=excel_sheet)
# # 确保列存在
# if country_id_field not in df.columns and 'ISO_A3' in df.columns:
#     # 如果excel用了不同列名，适当处理
#     df.rename(columns={'ISO_A3': country_id_field}, inplace=True)
# if scale_field_name not in df.columns:
#     raise ValueError(f"Excel中未找到列 '{scale_field_name}'")

# 构造 dict: id -> scale
scale_map = dict(zip(df[country_id_field].astype(str), df[scale_field_name].astype(float)))

# 2) 在矢量中添加/更新 scale 字段
# 如果字段不存在则添加
if scale_field_name not in [f.name for f in arcpy.ListFields(countries_fc)]:
    arcpy.AddField_management(countries_fc, scale_field_name, "DOUBLE")

# 将 scale 写入矢量（未匹配到的设为 1 或 None）
with arcpy.da.UpdateCursor(countries_fc, [country_id_field, scale_field_name]) as ucur:
    for row in ucur:
        key = str(row[0])
        if key in scale_map:
            row[1] = float(scale_map[key])
        else:
            # 处理缺失：这里设为1（不改变夜光）
            row[1] = 1.0
        ucur.updateRow(row)

# 3) 确保投影一致：把矢量投影到栅格的坐标系（如果不一致）
r_desc = arcpy.Describe(nightlight_raster)
r_sr = r_desc.spatialReference
fc_sr = arcpy.Describe(countries_fc).spatialReference
if fc_sr.name != r_sr.name:
    print("投影不一致：将矢量投影到栅格的投影坐标系...")
    projected_fc = os.path.join("in_memory", "countries_proj")
    arcpy.Project_management(countries_fc, projected_fc, r_sr)
    countries_for_raster = projected_fc
else:
    countries_for_raster = countries_fc

# 4) 设置对齐（snapRaster）、输出像元大小与extent
env.snapRaster = nightlight_raster
# 获取参考栅格 cellsize（假设为方形）
cellsize = Raster(nightlight_raster).meanCellWidth
env.cellSize = cellsize
env.extent = Raster(nightlight_raster).extent

# 5) Polygon to Raster：把 scale 字段栅格化
# 使用 MAXIMUM_AREA 或 FIRST 方法不过这里值一致，使用 "NONE" fallback
arcpy.conversion.PolygonToRaster(
    in_features=countries_for_raster,
    value_field=scale_field_name,
    out_rasterdataset=out_scale_raster,
    cell_assignment="MAXIMUM_AREA",
    priority_field="",
    cellsize=cellsize
)
print("scale raster created:", out_scale_raster)

# 6) 将 scale raster 的 NoData 替换为 1（如果需要）
scale_r = Raster(out_scale_raster)
# 创建临时掩膜：将 NoData 处赋值1
# 使用 Con(IsNull(scale_r), 1, scale_r)
scale_filled = Con(IsNull(scale_r), 1, scale_r)

# 7) 乘法操作：校正夜光
ntl = Raster(nightlight_raster)
corrected = ntl * scale_filled
corrected.save(out_corrected)
print("Corrected raster saved:", out_corrected)

# 8) 清理 in_memory（如果使用）
if 'projected_fc' in locals():
    arcpy.Delete_management(projected_fc)

arcpy.CheckInExtension("Spatial")
