import arcpy
from arcpy.sa import *
import os

# ===============================
# 参数设置（修改为你的路径）
# ===============================
arcpy.env.workspace = r"F:\Data_new"
arcpy.env.overwriteOutput = True

# zone_shp = r"F:\Data_new\MID_DATA.gdb\UC_NS_sub_CounAndConti_Moll"  # SHP
zone_shp = r"F:\Data_new\MID_DATA.gdb\ALL_MODIS_2020"  # SHP
zone_field = "Id"                          # 统计字段
value_raster = r"F:\Data_new\GHS_BUILT_V_E2020_GLOBE_R2023A_54009_100_V1_0\GHS_BUILT_V_E2020_GLOBE_R2023A_54009_100_V1_0.tif"    # 栅格文件
out_table = r"F:\Data_new\MID_DATA.gdb\ALL_BV_2020_GHSL"            # 临时输出
# out_csv = r"F:\Data_new\UE_POP_2020.csv"        # 最终输出 CSV

# ===============================
# 检查许可
# ===============================
arcpy.CheckOutExtension("Spatial")

# ===============================
# 执行 zonal statistics as table
# ===============================
outZSaT = ZonalStatisticsAsTable(zone_shp, zone_field, value_raster, out_table, "DATA","ALL")

print("Zonal statistics table created:", out_table)

# # ===============================
# # 转换 DBF → CSV
# # ===============================
# arcpy.conversion.TableToTable(
#     in_rows=out_table,
#     out_path=os.path.dirname(out_csv),
#     out_name=os.path.basename(out_csv).replace(".csv", "")
# )
#
# # 上一步会生成一个文件夹内的表，可用 pandas 再导出真正的 CSV
# import pandas as pd
# csv_table = os.path.join(os.path.dirname(out_csv), os.path.basename(out_csv).replace(".csv", "") + ".dbf")
# df = pd.DataFrame(arcpy.da.TableToNumPyArray(csv_table, "*"))
# df.to_csv(out_csv, index=False, encoding="utf-8-sig")
#
# print("CSV 文件输出完成：", out_csv)

