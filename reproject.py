import arcpy

in_shp = r"F:\Yifan Teng\Data_new\MID_DATA.gdb\GUB2018_50_NS_sub_CounAndConti"
out_shp = r"F:\Yifan Teng\Data_new\MID_DATA.gdb\GUB2018_50_NS_sub_CounAndConti_Moll"
tif = r"F:\Yifan Teng\Data_new\GHS_BUILT_H_AGBH_E2018_GLOBE_R2023A_54009_100_V1_0\GHS_BUILT_H_AGBH_E2018_GLOBE_R2023A_54009_100_V1_0.tif"

sr = arcpy.Describe(tif).spatialReference
arcpy.management.Project(in_shp, out_shp, sr)
