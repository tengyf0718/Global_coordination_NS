import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from pandas import DataFrame
from sklearn import metrics
from sklearn.decomposition import PCA

data_path_UC = r"F:\Yifan Teng\Data_new\Results\Results_WPOP_GDP_CO\UC_2020.xls" # CORE AREA
data_path_UE = r"F:\Yifan Teng\Data_new\Results\Results_WPOP_GDP_CO\UE_2020.xls" # EXTENSION AREA
data_path_ALL = r"F:\Yifan Teng\Data_new\Results\Results_WPOP_GDP_CO\ALL_BV_POP_NL2020.xls" #CORE + EXTENSION
# data_path_ALL = r"F:\Yifan Teng\Data_new\Results\Results_WPOP_GDP_CO\UC&UE_2020.xlsx" #CORE + EXTENSION

# label_mydata = r"F:\Yifan Teng\Data_new\Results\label.xls"
out_labeled = r"F:\Yifan Teng\Data_new\Results\Results_WPOP_GDP_CO\data_labeled_ALL_PP3.xls"
out_center = r"F:\Yifan Teng\Data_new\Results\Results_WPOP_GDP_CO\data_clusterCenters_ALL_PP3.xls"

# 导入数据，默认第一行为索引，index_col设定第一列也为索引
# 选择sheet， 从0开始编号， 直接引用sheet name也行
df = pd.read_excel(data_path_ALL, sheet_name=1, index_col=0) # UC MEAN
# selected_cols = ['BV_MEAN', 'POP_MEAN', 'ECO_MEAN']
selected_cols = ['BV_PP', 'POP', 'ECO_PP']
df_raw = df[selected_cols]

# 数据0-1标准化
df_normalized_data = df_raw.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
# print(df_normalized_data)

# # 利用皮尔逊相关系数查看多重共线性 及 可视化
# df_corr = df_normalized_data.corr()
# fig, ax = plt.subplots(figsize=(15, 10))
# sns.heatmap(data=df_corr, annot=True, fmt='.2f', annot_kws={'size': 7}, cmap='Blues')
# cax = plt.gcf().axes[-1]
# cax.tick_params(labelsize=7)
# plt.title('Pearson Correlation Coefficient Matrix', fontsize=7)
# plt.xticks(fontsize=7)
# plt.yticks(fontsize=7)
# plt.show()

# # ----------------- 判断可以聚为几类：手肘图、轮廓系数法--------------------
# # 手肘图法1——基于平均离差
# K = range(1, 18)
# meanDispersions = []
# for k in K:
#     kemans = KMeans(n_clusters=k, init='k-means++')
#     kemans.fit(df_normalized_data)
#     # 计算平均离差
#     m_Disp = sum(np.min(cdist(df_normalized_data, kemans.cluster_centers_, 'euclidean'), axis=1)) / df_normalized_data.shape[0]
#     meanDispersions.append(m_Disp)
#
# plt.rcParams['font.family'] = ['sans-serif']
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 使折线图显示中文
#
# plt.plot(K, meanDispersions, 'bx-')
# plt.xlabel('k')
# plt.ylabel('平均离差')
# plt.title('')
# plt.show()
#
# # 手肘图法2——基于SSE
# distortions = []  # 用来存放设置不同簇数时的SSE值
# for i in range(1,15):
#     kmModel = KMeans(n_clusters=i)
#     kmModel.fit(df_normalized_data)
#     distortions.append(kmModel.inertia_)  # 获取K-means算法的SSE
# # 绘制曲线
# plt.plot(range(1, 15), distortions, marker="o")
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.xlabel("K")
# plt.ylabel("Sum of Squared Errors(SSE)")
# plt.show()
#
# # 轮廓系数法
# K = range(2, 10)
# # 构建空列表，用于存储个中簇数下的轮廓系数
# S = []
# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(df_normalized_data)
#     labels = kmeans.labels_
#     # 调用字模块metrics中的silhouette_score函数，计算轮廓系数
#     S.append(metrics.silhouette_score(df_normalized_data, labels, metric='euclidean'))
#
# # 中文和负号的正常显示
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# # 设置绘图风格
# plt.style.use('ggplot')
# # 绘制K的个数与轮廓系数的关系
# plt.plot(K, S, 'b*-')
# plt.xlabel('K')
# plt.ylabel('Silhouette Coefficient Index')
# # 显示图形
# plt.show()

# ----------------- 开始 K-means 聚类的一系列过程---------------------
# K-means聚类
n_clusters = 3
kms = KMeans(n_clusters, init='k-means++')
data_fig = kms.fit(df_normalized_data)  # 模型拟合
centers = kms.cluster_centers_  # 计算聚类中心
labs = kms.labels_  # 为数据打标签
# df_labels = DataFrame(kms.labels_)  # 将标签存放为DataFrame
# df_labels.to_excel(label_mydata)  # 输出数据标签，其实输出可有可无

# # 将聚类结果为 0，1,2,3,4 的数据筛选出来 并打上标签
# df_A_0 = df_normalized_data[kms.labels_ == 0]
# df_A_1 = df_normalized_data[kms.labels_ == 1]
# df_A_2 = df_normalized_data[kms.labels_ == 2]
# df_A_3 = df_normalized_data[kms.labels_ == 3]
# df_A_4 = df_normalized_data[kms.labels_ == 4]
# m = np.shape(df_A_0)[1]
# df_A_0.insert(df_A_0.shape[1], 'label', 0)  # 打标签
# df_A_1.insert(df_A_1.shape[1], 'label', 1)
# df_A_2.insert(df_A_2.shape[1], 'label', 2)
# df_A_3.insert(df_A_3.shape[1], 'label', 3)
# df_A_4.insert(df_A_4.shape[1], 'label', 4)
# df_labels_data = pd.concat([df_A_0, df_A_1, df_A_2, df_A_3, df_A_4])  # 数据融合

# # 将聚类结果为 0，1,2,3,4 的数据筛选出来 并打上标签
# df_A_0 = df_normalized_data[kms.labels_ == 0]
# df_A_1 = df_normalized_data[kms.labels_ == 1]
# df_A_2 = df_normalized_data[kms.labels_ == 2]
# df_A_3 = df_normalized_data[kms.labels_ == 3]
# m = np.shape(df_A_0)[1]
# df_A_0.insert(df_A_0.shape[1], 'label', 0)  # 打标签
# df_A_1.insert(df_A_1.shape[1], 'label', 1)
# df_A_2.insert(df_A_2.shape[1], 'label', 2)
# df_A_3.insert(df_A_3.shape[1], 'label', 3)
# df_labels_data = pd.concat([df_A_0, df_A_1, df_A_2, df_A_3])  # 数据融合

# 将聚类结果为 0，1,2,3,4 的数据筛选出来 并打上标签
df_A_0 = df_normalized_data[kms.labels_ == 0]
df_A_1 = df_normalized_data[kms.labels_ == 1]
df_A_2 = df_normalized_data[kms.labels_ == 2]
m = np.shape(df_A_0)[1]
df_A_0.insert(df_A_0.shape[1], 'label', 0)  # 打标签
df_A_1.insert(df_A_1.shape[1], 'label', 1)
df_A_2.insert(df_A_2.shape[1], 'label', 2)
df_labels_data = pd.concat([df_A_0, df_A_1, df_A_2])  # 数据融合


df_labels_data.to_excel(out_labeled)  # 输出带有标签的数据

# 输出最终聚类中心
df_centers = DataFrame(centers)
df_centers.to_excel(out_center)
# --------------------到这里 K-means 聚类的流程算是结束了------------------------

# ------------------------下面介绍如何绘制聚类散点图-----------------------------
# 对二分类的散点图绘制，网上教程很多，此篇文章主要介绍多分类的散点图绘制问题
# 首先，对原数据进行 PCA 降维处理，获得散点图的横纵坐标轴数据
pca = PCA(n_components=2)  # 提取两个主成分，作为坐标轴
pca.fit(df_normalized_data)
data_pca = pca.transform(df_normalized_data)
data_pca = pd.DataFrame(data_pca, columns=['PC1', 'PC2'])
data_pca.insert(data_pca.shape[1], 'labels', labs)

# centers pca 对 K-means 的聚类中心降维，对应到散点图的二维坐标系中
pca = PCA(n_components=2)
pca.fit(centers)
data_pca_centers = pca.transform(centers)
data_pca_centers = pd.DataFrame(data_pca_centers, columns=['PC1', 'PC2'])

# Visualize it:
plt.figure(figsize=(8, 6))
plt.scatter(data_pca.values[:, 0], data_pca.values[:, 1], s=3, c=data_pca.values[:, 2], cmap='Accent')
plt.scatter(data_pca_centers.values[:, 0], data_pca_centers.values[:, 1], marker='o', s=55, c='#8E00FF')
plt.show()

