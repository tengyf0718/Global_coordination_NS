import pandas as pd
import numpy as np
from sqlalchemy import column

data_path_UC = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UC_CCDM_WORLD_GDP_PP.xls" # CORE AREA
data_path_UE = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UE_CCDM_WORLD_GDP_PP.xls" # EXTENSION AREA
data_path_ALL = r"F:\Data_new\Results\Results_WPOP_GDP_CO\ALL_CCDM_WORLD_GDP_PP_WITHNS.xls" # MODIS 2020 ENTIRE AREA

# 按照  南北方国家  来统计变量
out_NS_UC = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UC_NS_statistics.xls"
out_NS_UE = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UE_NS_statistics.xls"
out_NS_ALL = r"F:\Data_new\Results\Results_WPOP_GDP_CO\ALL_NS_statistics.xls"
# 按照  subregion  来统计变量
out_SUB_UC = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UC_SUB_statistics.xls"
out_SUB_UE = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UE_SUB_statistics.xls"
out_SUB_ALL = r"F:\Data_new\Results\Results_WPOP_GDP_CO\ALL_SUB_statistics.xls"
# 按照  ECONOMY  来统计变量
out_ECOTYPE_UC = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UC_ECOTYPE_statistics.xls"
out_ECOTYPE_UE = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UE_ECOTYPE_statistics.xls"
out_ECOTYPE_ALL = r"F:\Data_new\Results\Results_WPOP_GDP_CO\ALL_ECOTYPE_statistics.xls"
# 按照 SOVEREIGNT 来统计变量
out_SOVEREIGNT_ALL = r"F:\Data_new\Results\Results_WPOP_GDP_CO\ALL_SOVEREIGNT_statistics.xls"

# 选择CORE area
df_uc = pd.read_excel(data_path_UC, sheet_name=0, index_col=0)
# 选择expansion area
df_ue = pd.read_excel(data_path_UE, sheet_name=0, index_col=0)
# 选择MODIS 2020 ENTIRE area
df_all = pd.read_excel(data_path_ALL, sheet_name=1, index_col=0)


# # -------------按照南北方国家来统计变量UC-------------
# stats_uc_NS = df_uc.groupby("Classifica").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('Classifica', 'count')
# ).reset_index()
#
# stats_uc_NS['BV'] = stats_uc_NS['BV_mean'].round(3).astype(str) + "±" + stats_uc_NS['BV_std'].round(3).astype(str)
# stats_uc_NS['POP'] = stats_uc_NS['POP_mean'].round(3).astype(str) + "±" + stats_uc_NS['POP_std'].round(3).astype(str)
# stats_uc_NS['ECO'] = stats_uc_NS['ECO_mean'].round(3).astype(str) + "±" + stats_uc_NS['ECO_std'].round(3).astype(str)
# stats_uc_NS['BV_PP'] = stats_uc_NS['BV_PP_mean'].round(3).astype(str) + "±" + stats_uc_NS['BV_PP_std'].round(3).astype(str)
# stats_uc_NS['ECO_PP'] = stats_uc_NS['ECO_PP_mean'].round(3).astype(str) + "±" + stats_uc_NS['ECO_PP_std'].round(3).astype(str)
# stats_uc_NS['C'] = stats_uc_NS['C_mean'].round(3).astype(str) + "±" + stats_uc_NS['C_std'].round(3).astype(str)
# stats_uc_NS['D'] = stats_uc_NS['D_mean'].round(3).astype(str) + "±" + stats_uc_NS['D_std'].round(3).astype(str)
#
# final_UC_NS = stats_uc_NS[['Classifica','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_UC_NS.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_UC_NS.to_excel(out_NS_UC, index=True)
#
#
# # -------------按照南北方国家来统计变量UE-------------
# stats_ue_NS = df_ue.groupby("Classifica").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('Classifica', 'count')
# ).reset_index()
#
# stats_ue_NS['BV'] = stats_ue_NS['BV_mean'].round(3).astype(str) + "±" + stats_ue_NS['BV_std'].round(3).astype(str)
# stats_ue_NS['POP'] = stats_ue_NS['POP_mean'].round(3).astype(str) + "±" + stats_ue_NS['POP_std'].round(3).astype(str)
# stats_ue_NS['ECO'] = stats_ue_NS['ECO_mean'].round(3).astype(str) + "±" + stats_ue_NS['ECO_std'].round(3).astype(str)
# stats_ue_NS['BV_PP'] = stats_ue_NS['BV_PP_mean'].round(3).astype(str) + "±" + stats_ue_NS['BV_PP_std'].round(3).astype(str)
# stats_ue_NS['ECO_PP'] = stats_ue_NS['ECO_PP_mean'].round(3).astype(str) + "±" + stats_ue_NS['ECO_PP_std'].round(3).astype(str)
# stats_ue_NS['C'] = stats_ue_NS['C_mean'].round(3).astype(str) + "±" + stats_ue_NS['C_std'].round(3).astype(str)
# stats_ue_NS['D'] = stats_ue_NS['D_mean'].round(3).astype(str) + "±" + stats_ue_NS['D_std'].round(3).astype(str)
#
# final_UE_NS = stats_ue_NS[['Classifica','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_UE_NS.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_UE_NS.to_excel(out_NS_UE, index=True)

# # -------------按照南北方国家来统计变量ALL-------------
# stats_all_NS = df_all.groupby("Classifica").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('Classifica', 'count')
# ).reset_index()
#
# stats_all_NS['BV'] = stats_all_NS['BV_mean'].round(3).astype(str) + "±" + stats_all_NS['BV_std'].round(3).astype(str)
# stats_all_NS['POP'] = stats_all_NS['POP_mean'].round(3).astype(str) + "±" + stats_all_NS['POP_std'].round(3).astype(str)
# stats_all_NS['ECO'] = stats_all_NS['ECO_mean'].round(3).astype(str) + "±" + stats_all_NS['ECO_std'].round(3).astype(str)
# stats_all_NS['BV_PP'] = stats_all_NS['BV_PP_mean'].round(3).astype(str) + "±" + stats_all_NS['BV_PP_std'].round(3).astype(str)
# stats_all_NS['ECO_PP'] = stats_all_NS['ECO_PP_mean'].round(3).astype(str) + "±" + stats_all_NS['ECO_PP_std'].round(3).astype(str)
# stats_all_NS['C'] = stats_all_NS['C_mean'].round(3).astype(str) + "±" + stats_all_NS['C_std'].round(3).astype(str)
# stats_all_NS['D'] = stats_all_NS['D_mean'].round(3).astype(str) + "±" + stats_all_NS['D_std'].round(3).astype(str)
#
# final_ALL_NS = stats_all_NS[['Classifica','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_ALL_NS.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_ALL_NS.to_excel(out_NS_ALL, index=True)


# # -------------按照SUBREGION来统计变量UC-------------
# stats_uc_SUB = df_uc.groupby("SUBREGION").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('SUBREGION', 'count')
# ).reset_index()
#
# stats_uc_SUB['BV'] = stats_uc_SUB['BV_mean'].round(3).astype(str) + "±" + stats_uc_SUB['BV_std'].round(3).astype(str)
# stats_uc_SUB['POP'] = stats_uc_SUB['POP_mean'].round(3).astype(str) + "±" + stats_uc_SUB['POP_std'].round(3).astype(str)
# stats_uc_SUB['ECO'] = stats_uc_SUB['ECO_mean'].round(3).astype(str) + "±" + stats_uc_SUB['ECO_std'].round(3).astype(str)
# stats_uc_SUB['BV_PP'] = stats_uc_SUB['BV_PP_mean'].round(3).astype(str) + "±" + stats_uc_SUB['BV_PP_std'].round(3).astype(str)
# stats_uc_SUB['ECO_PP'] = stats_uc_SUB['ECO_PP_mean'].round(3).astype(str) + "±" + stats_uc_SUB['ECO_PP_std'].round(3).astype(str)
# stats_uc_SUB['C'] = stats_uc_SUB['C_mean'].round(3).astype(str) + "±" + stats_uc_SUB['C_std'].round(3).astype(str)
# stats_uc_SUB['D'] = stats_uc_SUB['D_mean'].round(3).astype(str) + "±" + stats_uc_SUB['D_std'].round(3).astype(str)
#
# final_UC_SUB = stats_uc_SUB[['SUBREGION','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_UC_SUB.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_UC_SUB.to_excel(out_SUB_UC, index=True)
#
# # -------------按照SUBREGION来统计变量UE-------------
# stats_ue_SUB = df_ue.groupby("SUBREGION").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('SUBREGION', 'count')
# ).reset_index()
#
# stats_ue_SUB['BV'] = stats_ue_SUB['BV_mean'].round(3).astype(str) + "±" + stats_ue_SUB['BV_std'].round(3).astype(str)
# stats_ue_SUB['POP'] = stats_ue_SUB['POP_mean'].round(3).astype(str) + "±" + stats_ue_SUB['POP_std'].round(3).astype(str)
# stats_ue_SUB['ECO'] = stats_ue_SUB['ECO_mean'].round(3).astype(str) + "±" + stats_ue_SUB['ECO_std'].round(3).astype(str)
# stats_ue_SUB['BV_PP'] = stats_ue_SUB['BV_PP_mean'].round(3).astype(str) + "±" + stats_ue_SUB['BV_PP_std'].round(3).astype(str)
# stats_ue_SUB['ECO_PP'] = stats_ue_SUB['ECO_PP_mean'].round(3).astype(str) + "±" + stats_ue_SUB['ECO_PP_std'].round(3).astype(str)
# stats_ue_SUB['C'] = stats_ue_SUB['C_mean'].round(3).astype(str) + "±" + stats_ue_SUB['C_std'].round(3).astype(str)
# stats_ue_SUB['D'] = stats_ue_SUB['D_mean'].round(3).astype(str) + "±" + stats_ue_SUB['D_std'].round(3).astype(str)
#
# final_UE_SUB = stats_ue_SUB[['SUBREGION','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_UE_SUB.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_UE_SUB.to_excel(out_SUB_UE, index=True)

# # -------------按照SUBREGION来统计变量ALL-------------
# stats_all_SUB = df_all.groupby("SUBREGION").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('SUBREGION', 'count')
# ).reset_index()
#
# stats_all_SUB['BV'] = stats_all_SUB['BV_mean'].round(3).astype(str) + "±" + stats_all_SUB['BV_std'].round(3).astype(str)
# stats_all_SUB['POP'] = stats_all_SUB['POP_mean'].round(3).astype(str) + "±" + stats_all_SUB['POP_std'].round(3).astype(str)
# stats_all_SUB['ECO'] = stats_all_SUB['ECO_mean'].round(3).astype(str) + "±" + stats_all_SUB['ECO_std'].round(3).astype(str)
# stats_all_SUB['BV_PP'] = stats_all_SUB['BV_PP_mean'].round(3).astype(str) + "±" + stats_all_SUB['BV_PP_std'].round(3).astype(str)
# stats_all_SUB['ECO_PP'] = stats_all_SUB['ECO_PP_mean'].round(3).astype(str) + "±" + stats_all_SUB['ECO_PP_std'].round(3).astype(str)
# stats_all_SUB['C'] = stats_all_SUB['C_mean'].round(3).astype(str) + "±" + stats_all_SUB['C_std'].round(3).astype(str)
# stats_all_SUB['D'] = stats_all_SUB['D_mean'].round(3).astype(str) + "±" + stats_all_SUB['D_std'].round(3).astype(str)
#
# final_ALL_SUB = stats_all_SUB[['SUBREGION','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_ALL_SUB.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_ALL_SUB.to_excel(out_SUB_ALL, index=True)


# # -------------按照ECOTYPE来统计变量UC-------------
# stats_uc_ECOTYPE = df_uc.groupby("ECONOMY").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('ECONOMY', 'count')
# ).reset_index()
#
# stats_uc_ECOTYPE['BV'] = stats_uc_ECOTYPE['BV_mean'].round(3).astype(str) + "±" + stats_uc_ECOTYPE['BV_std'].round(3).astype(str)
# stats_uc_ECOTYPE['POP'] = stats_uc_ECOTYPE['POP_mean'].round(3).astype(str) + "±" + stats_uc_ECOTYPE['POP_std'].round(3).astype(str)
# stats_uc_ECOTYPE['ECO'] = stats_uc_ECOTYPE['ECO_mean'].round(3).astype(str) + "±" + stats_uc_ECOTYPE['ECO_std'].round(3).astype(str)
# stats_uc_ECOTYPE['BV_PP'] = stats_uc_ECOTYPE['BV_PP_mean'].round(3).astype(str) + "±" + stats_uc_ECOTYPE['BV_PP_std'].round(3).astype(str)
# stats_uc_ECOTYPE['ECO_PP'] = stats_uc_ECOTYPE['ECO_PP_mean'].round(3).astype(str) + "±" + stats_uc_ECOTYPE['ECO_PP_std'].round(3).astype(str)
# stats_uc_ECOTYPE['C'] = stats_uc_ECOTYPE['C_mean'].round(3).astype(str) + "±" + stats_uc_ECOTYPE['C_std'].round(3).astype(str)
# stats_uc_ECOTYPE['D'] = stats_uc_ECOTYPE['D_mean'].round(3).astype(str) + "±" + stats_uc_ECOTYPE['D_std'].round(3).astype(str)
#
# final_UC_ECOTYPE = stats_uc_ECOTYPE[['ECONOMY','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_UC_ECOTYPE.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_UC_ECOTYPE.to_excel(out_ECOTYPE_UC, index=True)
#
# # -------------按照ECOTYPE来统计变量UE-------------
# stats_ue_ECOTYPE = df_ue.groupby("ECONOMY").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('ECONOMY', 'count')
# ).reset_index()
#
# stats_ue_ECOTYPE['BV'] = stats_ue_ECOTYPE['BV_mean'].round(3).astype(str) + "±" + stats_ue_ECOTYPE['BV_std'].round(3).astype(str)
# stats_ue_ECOTYPE['POP'] = stats_ue_ECOTYPE['POP_mean'].round(3).astype(str) + "±" + stats_ue_ECOTYPE['POP_std'].round(3).astype(str)
# stats_ue_ECOTYPE['ECO'] = stats_ue_ECOTYPE['ECO_mean'].round(3).astype(str) + "±" + stats_ue_ECOTYPE['ECO_std'].round(3).astype(str)
# stats_ue_ECOTYPE['BV_PP'] = stats_ue_ECOTYPE['BV_PP_mean'].round(3).astype(str) + "±" + stats_ue_ECOTYPE['BV_PP_std'].round(3).astype(str)
# stats_ue_ECOTYPE['ECO_PP'] = stats_ue_ECOTYPE['ECO_PP_mean'].round(3).astype(str) + "±" + stats_ue_ECOTYPE['ECO_PP_std'].round(3).astype(str)
# stats_ue_ECOTYPE['C'] = stats_ue_ECOTYPE['C_mean'].round(3).astype(str) + "±" + stats_ue_ECOTYPE['C_std'].round(3).astype(str)
# stats_ue_ECOTYPE['D'] = stats_ue_ECOTYPE['D_mean'].round(3).astype(str) + "±" + stats_ue_ECOTYPE['D_std'].round(3).astype(str)
#
# final_UE_ECOTYPE = stats_ue_ECOTYPE[['ECONOMY','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_UE_ECOTYPE.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_UE_ECOTYPE.to_excel(out_ECOTYPE_UE, index=True)

# # -------------按照ECOTYPE来统计变量ALL-------------
# stats_all_ECOTYPE = df_all.groupby("ECONOMY").agg(
#     BV_mean=('BV_MEAN', 'mean'),
#     BV_std=('BV_MEAN', 'std'),
#     POP_mean=('POP_MEAN', 'mean'),
#     POP_std=('POP_MEAN', 'std'),
#     ECO_mean=('ECO_MEAN', 'mean'),
#     ECO_std=('ECO_MEAN', 'std'),
#     BV_PP_mean=('BV_PP', 'mean'),
#     BV_PP_std=('BV_PP', 'std'),
#     ECO_PP_mean=('ECO_PP', 'mean'),
#     ECO_PP_std=('ECO_PP', 'std'),
#     C_mean=('C', 'mean'),
#     C_std=('C', 'std'),
#     D_mean=('D', 'mean'),
#     D_std=('D', 'std'),
#     n=('ECONOMY', 'count')
# ).reset_index()
#
# stats_all_ECOTYPE['BV'] = stats_all_ECOTYPE['BV_mean'].round(3).astype(str) + "±" + stats_all_ECOTYPE['BV_std'].round(3).astype(str)
# stats_all_ECOTYPE['POP'] = stats_all_ECOTYPE['POP_mean'].round(3).astype(str) + "±" + stats_all_ECOTYPE['POP_std'].round(3).astype(str)
# stats_all_ECOTYPE['ECO'] = stats_all_ECOTYPE['ECO_mean'].round(3).astype(str) + "±" + stats_all_ECOTYPE['ECO_std'].round(3).astype(str)
# stats_all_ECOTYPE['BV_PP'] = stats_all_ECOTYPE['BV_PP_mean'].round(3).astype(str) + "±" + stats_all_ECOTYPE['BV_PP_std'].round(3).astype(str)
# stats_all_ECOTYPE['ECO_PP'] = stats_all_ECOTYPE['ECO_PP_mean'].round(3).astype(str) + "±" + stats_all_ECOTYPE['ECO_PP_std'].round(3).astype(str)
# stats_all_ECOTYPE['C'] = stats_all_ECOTYPE['C_mean'].round(3).astype(str) + "±" + stats_all_ECOTYPE['C_std'].round(3).astype(str)
# stats_all_ECOTYPE['D'] = stats_all_ECOTYPE['D_mean'].round(3).astype(str) + "±" + stats_all_ECOTYPE['D_std'].round(3).astype(str)
#
# final_ALL_ECOTYPE = stats_all_ECOTYPE[['ECONOMY','n',
#                      'BV_mean','BV_std',
#                      'POP_mean','POP_std',
#                      'ECO_mean','ECO_std',
#                      'BV_PP_mean','BV_PP_std',
#                      'ECO_PP_mean','ECO_PP_std',
#                      'C_mean','C_std',
#                      'D_mean','D_std',
#                      'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
# final_ALL_ECOTYPE.rename(columns={'n':'(# of urban areas)'}, inplace=True)
# final_ALL_ECOTYPE.to_excel(out_ECOTYPE_ALL, index=True)

# -------------按照ECOTYPE来统计变量ALL-------------
stats_all_SOVEREIGNT = df_all.groupby("SOVEREIGNT").agg(
    BV_mean=('BV_MEAN', 'mean'),
    BV_std=('BV_MEAN', 'std'),
    POP_mean=('POP_MEAN', 'mean'),
    POP_std=('POP_MEAN', 'std'),
    ECO_mean=('ECO_MEAN', 'mean'),
    ECO_std=('ECO_MEAN', 'std'),
    BV_PP_mean=('BV_PP', 'mean'),
    BV_PP_std=('BV_PP', 'std'),
    ECO_PP_mean=('ECO_PP', 'mean'),
    ECO_PP_std=('ECO_PP', 'std'),
    C_mean=('C', 'mean'),
    C_std=('C', 'std'),
    D_mean=('D', 'mean'),
    D_std=('D', 'std'),
    n=('SOVEREIGNT', 'count')
).reset_index()

stats_all_SOVEREIGNT['BV'] = stats_all_SOVEREIGNT['BV_mean'].round(3).astype(str) + "±" + stats_all_SOVEREIGNT['BV_std'].round(3).astype(str)
stats_all_SOVEREIGNT['POP'] = stats_all_SOVEREIGNT['POP_mean'].round(3).astype(str) + "±" + stats_all_SOVEREIGNT['POP_std'].round(3).astype(str)
stats_all_SOVEREIGNT['ECO'] = stats_all_SOVEREIGNT['ECO_mean'].round(3).astype(str) + "±" + stats_all_SOVEREIGNT['ECO_std'].round(3).astype(str)
stats_all_SOVEREIGNT['BV_PP'] = stats_all_SOVEREIGNT['BV_PP_mean'].round(3).astype(str) + "±" + stats_all_SOVEREIGNT['BV_PP_std'].round(3).astype(str)
stats_all_SOVEREIGNT['ECO_PP'] = stats_all_SOVEREIGNT['ECO_PP_mean'].round(3).astype(str) + "±" + stats_all_SOVEREIGNT['ECO_PP_std'].round(3).astype(str)
stats_all_SOVEREIGNT['C'] = stats_all_SOVEREIGNT['C_mean'].round(3).astype(str) + "±" + stats_all_SOVEREIGNT['C_std'].round(3).astype(str)
stats_all_SOVEREIGNT['D'] = stats_all_SOVEREIGNT['D_mean'].round(3).astype(str) + "±" + stats_all_SOVEREIGNT['D_std'].round(3).astype(str)

final_ALL_SOVEREIGNT = stats_all_SOVEREIGNT[['SOVEREIGNT','n',
                     'BV_mean','BV_std',
                     'POP_mean','POP_std',
                     'ECO_mean','ECO_std',
                     'BV_PP_mean','BV_PP_std',
                     'ECO_PP_mean','ECO_PP_std',
                     'C_mean','C_std',
                     'D_mean','D_std',
                     'BV','POP','ECO','BV_PP','ECO_PP','C','D']]
final_ALL_SOVEREIGNT.rename(columns={'n':'(# of urban areas)'}, inplace=True)

final_ALL_SOVEREIGNT.to_excel(out_SOVEREIGNT_ALL, index=True)
