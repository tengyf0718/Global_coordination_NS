import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpmath import linspace
from sympy.printing.pretty.pretty_symbology import line_width

# data_path_UC = r"F:\Data_new\Results\UC_ALL_2020.xls" # CORE AREA
# data_path_UE = r"F:\Data_new\Results\UE_ALL_2020.xls" # EXTENSION AREA
data_path_UC = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UC_2020.xls" # CORE AREA
data_path_UE = r"F:\Data_new\Results\Results_WPOP_GDP_CO\UE_2020.xls" # EXTENSION AREA
data_path_ALL = r"F:\Data_new\Results\Results_WPOP_GDP_CO\ALL_BV_POP_NL2020.xls" #CORE + EXTENSION
# out_excel = r"F:\Data_new\Results\UC&UE_PP_CCDM_onlyminmax.xls"
out_excel = r"F:\Data_new\Results\Results_WPOP_GDP_CO\ALL_CCDM_WORLD_GDP_PP.xls"

def minmax_series(s):
    return (s - s.min()) / (s.max() - s.min())
def zscore_series(s):
    return (s - s.mean()) / s.std(ddof=0)
# def z_score(data):
#     mean = np.mean(data)
#     std = np.std(data)
#     return (data - mean) / std

# 导入数据，默认第一行为索引，index_col设定第一列也为索引
# 选择sheet， 从0开始编号， 直接引用sheet name也行
df = pd.read_excel(data_path_ALL, sheet_name=1, index_col=0) # UC MEAN
# cols = ['BV_MEAN', 'POP_MEAN', 'ECO_MEAN']
cols = ['BV_PP', 'POP', 'ECO_PP']
# # minmax标准化
# df['BV_PP_norm'] = minmax_series(df['BV_PP'])
# df['POP_norm'] = minmax_series(df['POP'])
# df['ECO_PP_norm'] = minmax_series(df['ECO_PP'])

# log1p minmax标准化
for col in cols:
    df[col+'_log'] = np.log1p(df[col])
# df['BV_MEAN_norm'] = minmax_series(df['BV_MEAN_log'])
# df['POP_MEAN_norm'] = minmax_series(df['POP_MEAN_log'])
# df['ECO_MEAN_norm'] = minmax_series(df['ECO_MEAN_log'])
df['BV_PP_norm'] = minmax_series(df['BV_PP_log'])
df['POP_norm'] = minmax_series(df['POP_log'])
df['ECO_PP_norm'] = minmax_series(df['ECO_PP_log'])

# # z-score normalization
# df['BV_MEAN_norm'] = z_score(df['BV_MEAN'])
# df['POP_MEAN_norm'] = z_score(df['POP_MEAN'])
# df['ECO_MEAN_norm'] = z_score(df['ECO_MEAN'])
# df['BV_MEAN_zero'] = zscore_series(df['BV_MEAN'])
# df['POP_MEAN_zero'] = zscore_series(df['POP_MEAN'])
# df['ECO_MEAN_zero'] = zscore_series(df['ECO_MEAN'])
# df['BV_MEAN_norm'] = minmax_series(df['BV_MEAN_zero'])
# df['POP_MEAN_norm'] = minmax_series(df['POP_MEAN_zero'])
# df['ECO_MEAN_norm'] = minmax_series(df['ECO_MEAN_zero'])

# 假设每个维度本身就是一个系统（即每个U只有一个指标）
# df['U1_space'] = df['BV_MEAN_norm']
# df['U2_pop'] = df['POP_MEAN_norm']
# df['U3_econ'] = df['ECO_MEAN_norm']
df['U1_space'] = df['BV_PP_norm']
df['U2_pop'] = df['POP_norm']
df['U3_econ'] = df['ECO_PP_norm']
# 假设三个系统同等重要
alpha, beta, gamma = 1/3, 1/3, 1/3

# C = [U1 * U2 * U3 / ((U1 + U2 + U3)/3)^3] ^ (1/3)
df['C'] = ((df['U1_space'] * df['U2_pop'] * df['U3_econ']) /
           ((df['U1_space'] + df['U2_pop'] + df['U3_econ']) / 3) ** 3) ** (1/3)
df['T'] = alpha * df['U1_space'] + beta * df['U2_pop'] + gamma * df['U3_econ']
df['D'] = np.sqrt(df['C'] * df['T'])


# output_cols = cols + [col + '_norm' for col in cols] + [
#     'U1_space', 'U2_pop', 'U3_econ', 'C', 'T', 'D'
# ]
output_cols = cols + [col + '_log' for col in cols] + [col + '_norm' for col in cols] + [
    'U1_space', 'U2_pop', 'U3_econ', 'C', 'T', 'D'
]
df.to_excel(out_excel, index=False)
df.to_csv(out_excel.replace('.xls', '.csv'), index=False)

# y = np.sqrt(df['T'])
# plt.scatter(df['T'], df['D'], c=df['C'], cmap='coolwarm')
x = linspace(0.05,1,100)
y = np.sqrt(x)
plt.figure(figsize=(6,4.5))
plt.plot(x, y, color='gray',linewidth=2, zorder=1)
plt.text(0.7, np.sqrt(0.7) + 0.005, r'$y=\sqrt{x}$', fontsize=9, ha='right')
# #  辅助线
# a_values = [0.8, 0.6, 0.4]
# for a in a_values:
#     plt.plot(x, a*y, color='lightgray', linestyle='--', linewidth=1)
#     plt.text(0.4, a*np.sqrt(0.4) + 0.005, f'{a}√x', color='gray', fontsize=9, ha='right')
# t = linspace(0.05,0.4,400)
# c = linspace(0,1,400)
# T, C = np.meshgrid(t, c)
# D = np.sqrt(C*T)
# contour = plt.contour(T, D, C, levels=200,cmap='coolwarm',alpha=0.3 ,zorder=1)
plt.scatter(df.loc[df['D']>0, 'T'], df.loc[df['D']>0, 'D'], c=df.loc[df['D']>0, 'C'], cmap='coolwarm',zorder=2, vmin=0,vmax=1)

# plt.xticks(fontsize=8)
# plt.yticks(fontsize=8)
plt.xlabel('Comprehensive Development Index (T)')
plt.ylabel('Coordination Degree (D)')
# plt.title('Urban Area Coupling Coordination Pattern')
plt.colorbar(label='Coupling Degree (C)')
plt.show()

