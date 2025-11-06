import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm
from math import exp

# def cagr_extrapolate(gdp_df, target_year=2000, n_boot=2000, random_state=0):
#     # 保证按年排序，移除0或负值
#     df = gdp_df.dropna().sort_values('year')
#     df = df[df['GDP_PPP']>0]
#     years = df['year'].values
#     gdp = df['GDP_PPP'].values
#     if len(gdp) < 2:
#         return None, None  # 无法估计
#     # fit log-linear: ln(GDP) = a + b*year
#     X = years.reshape(-1,1)
#     y = np.log(gdp)
#     lm = LinearRegression().fit(X, y)
#     pred_log = lm.predict(np.array([[target_year]]))[0]
#     pred = np.exp(pred_log)
#     # bootstrap for CI: resample years-with-replacement pairs
#     np.random.seed(random_state)
#     boot_preds = []
#     n = len(years)
#     for i in range(n_boot):
#         idx = np.random.choice(np.arange(n), size=n, replace=True)
#         Xb = years[idx].reshape(-1,1)
#         yb = np.log(gdp[idx])
#         try:
#             lm_b = LinearRegression().fit(Xb, yb)
#             boot_preds.append(np.exp(lm_b.predict(np.array([[target_year]]))[0]))
#         except:
#             continue
#     lower = np.percentile(boot_preds, 2.5)
#     upper = np.percentile(boot_preds, 97.5)
#     return pred, (lower, upper)
#
#
# if __name__ == "__main__":
#     # 1. 读取 Excel
#     excel_path = r"F:\Yifan Teng\Data_new\API_NY.GDP.MKTP.PP.KD_DS2_en_excel_v2_1832.xls"
#     df = pd.read_excel(excel_path, sheet_name="Kosovo")
#
#     # 2. 调用函数
#     pred_2000, ci = cagr_extrapolate(df, target_year=2000)
#
#     # 3. 输出结果
#     print(f"Estimated GDP_PPP in 2000: {pred_2000:.2f}")
#     print(f"95% confidence interval: {ci}")

# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
#
# === 定义函数 ===
def cagr_extrapolate(gdp_df, target_year, n_boot=2000, random_state=0):
    rng = np.random.default_rng(random_state)
    gdp_df = gdp_df.sort_values("year")
    years = gdp_df["year"].values
    gdp = gdp_df["GDP"].values

    n_years = years[-1] - years[0]
    cagr = (gdp[-1] / gdp[0]) ** (1 / n_years) - 1

    idx = np.arange(len(gdp))
    cagr_samples = []
    for _ in range(n_boot):
        sample_idx = rng.choice(idx, size=len(idx), replace=True)
        s_years = years[sample_idx]
        s_gdp = gdp[sample_idx]
        try:
            cagr_i = (s_gdp.max() / s_gdp.min()) ** (1 / (s_years.max() - s_years.min())) - 1
            cagr_samples.append(cagr_i)
        except ZeroDivisionError:
            continue

    delta_t = target_year - years[-1]
    pred_samples = gdp[-1] * (1 + np.array(cagr_samples)) ** delta_t

    pred_mean = np.mean(pred_samples)
    ci = np.percentile(pred_samples, [2.5, 97.5])
    return pred_mean, tuple(ci), np.array(cagr_samples)


# # === 主程序 ===
# if __name__ == "__main__":
#     # 1. 读取数据
#     excel_path = r"F:\Yifan Teng\Data_new\API_NY.GDP.MKTP.KD_DS2_en_excel_v2_130141.xls"
#     df = pd.read_excel(excel_path, sheet_name="Yemen")
#     # df = pd.read_excel(excel_path, sheet_name="Kosovo")
#
#     df = df.sort_values("year")
#     years = df["year"].values
#     gdp = df["GDP"].values
#     # # 2. 分段数据
#     # df_early = df[(df["year"] >= 2008) & (df["year"] <= 2011)]
#     # df_late = df[(df["year"] >= 2012) & (df["year"] <= 2015)]
#     # years_early = df_early["year"].values
#     # years_late = df_late["year"].values
#     # gdp_early = df_early["GDP"].values
#     # gdp_late = df_late["GDP"].values
#
#     # 2. 拟合/外推
#     target_year1 = 2020
#     pred_mean1, ci1, cagr_samples1 = cagr_extrapolate(df, target_year=target_year1)
#     print(f"Estimated GDP in 2000: {pred_mean1:.2f}")
#     print(f"95% confidence interval: {ci1}")
#
#     # 3. 构建预测线
#     cagr_mean1 = np.mean(cagr_samples1)
#     all_years1 = np.arange(target_year1, years[-1] + 1)
#     gdp_proj1 = gdp[-1] * (1 + cagr_mean1) ** (all_years1 - years[-1])
#
#     # 4. 绘图
#     plt.figure(figsize=(8, 5))
#
#     # 实际数据：实线
#     plt.plot(years, gdp, 'o-', color="steelblue", label="Actual data")
#
#     # 预测区间
#     future_mask1 = all_years1 < years[0]
#     plt.plot(all_years1[future_mask1], gdp_proj1[future_mask1], '--', color="orange", label="Estimated trend")
#     plt.plot(all_years1[future_mask1], gdp_proj1[future_mask1], 'o', color="orange")
#
#     # 置信区间阴影
#     ci_lower1 = gdp[-1] * (1 + np.percentile(cagr_samples1, 2.5)) ** (all_years1 - years[-1])
#     ci_upper1 = gdp[-1] * (1 + np.percentile(cagr_samples1, 97.5)) ** (all_years1 - years[-1])
#     plt.fill_between(all_years1[future_mask1], ci_lower1[future_mask1], ci_upper1[future_mask1],
#                      color="orange", alpha=0.2, label="95% CI")
#
#     # 添加估计点
#     plt.scatter(target_year1, pred_mean1, color="red", zorder=5, label=f"Estimated 2020 GDP")
#     plt.text(target_year1 + 0.5, pred_mean1, f"{pred_mean1:,.0f}",
#              color="red", fontsize=10, va="bottom", ha="left",
#              bbox=dict(facecolor="white", edgecolor="none", alpha=0.6))
#     # # 2. 拟合/外推
#     # target_year1 = 2000
#     # pred_mean1, ci1, cagr_samples1 = cagr_extrapolate(df_early, target_year=target_year1)
#     # print(f"Estimated GDP in 2000: {pred_mean1:.2f}")
#     # print(f"95% confidence interval: {ci1}")
#     #
#     # # 3. 构建预测线
#     # cagr_mean1 = np.mean(cagr_samples1)
#     # all_years1 = np.arange(target_year1, years_early[-1] + 1)
#     # gdp_proj1 = gdp_early[-1] * (1 + cagr_mean1) ** (all_years1 - years_early[-1])
#     #
#     # # 4. 绘图
#     # plt.figure(figsize=(8, 5))
#     #
#     # # 实际数据：实线
#     # plt.plot(years, gdp, 'o-', color="steelblue", label="Actual data")
#     #
#     # # 预测区间
#     # future_mask1 = all_years1 < years_early[0]
#     # plt.plot(all_years1[future_mask1], gdp_proj1[future_mask1], '--', color="orange", label="Estimated trend")
#     # plt.plot(all_years1[future_mask1], gdp_proj1[future_mask1], 'o', color="orange")
#     #
#     # # 置信区间阴影
#     # ci_lower1 = gdp_early[-1] * (1 + np.percentile(cagr_samples1, 2.5)) ** (all_years1 - years_early[-1])
#     # ci_upper1 = gdp_early[-1] * (1 + np.percentile(cagr_samples1, 97.5)) ** (all_years1 - years_early[-1])
#     # plt.fill_between(all_years1[future_mask1], ci_lower1[future_mask1], ci_upper1[future_mask1],
#     #                  color="orange", alpha=0.2, label="95% CI")
#     #
#     # # 添加估计点
#     # plt.scatter(target_year1, pred_mean1, color="red", zorder=5, label=f"Estimated GDP")
#     # plt.text(target_year1 + 0.5, pred_mean1, f"{pred_mean1:,.0f}",
#     #          color="red", fontsize=10, va="bottom", ha="left",
#     #          bbox=dict(facecolor="white", edgecolor="none", alpha=0.6))
#     # #
#     # # 2️⃣ 预测未来（例如 2020）
#     # target_year2 = 2020
#     # pred_mean2, ci2, cagr_samples2 = cagr_extrapolate(df_late, target_year=target_year2)
#     # print(f"Estimated GDP in {target_year2}: {pred_mean2:.2f}")
#     # print(f"95% confidence interval: {ci2}")
#     #
#     # # 3️⃣ 构建预测线
#     # cagr_mean2 = np.mean(cagr_samples2)
#     # all_years2 = np.arange(years_late[0], target_year2 + 1)
#     # # gdp_proj = gdp[0] * (1 + cagr_mean) ** (all_years - years[0])
#     # # gdp_proj = np.interp(all_years, [years[0], target_year], [gdp[0], pred_mean])
#     # gdp_proj2 = gdp_late[-1] * (1 + cagr_mean2) ** (all_years2 - years_late[-1])
#     #
#     # # 🔸未来年份部分（虚线）
#     # future_mask2 = all_years2 > years_late[-1]
#     # plt.plot(all_years2[future_mask2], gdp_proj2[future_mask2], '--', color="orange")
#     # plt.plot(all_years2[future_mask2], gdp_proj2[future_mask2], 'o', color="orange")
#     #
#     # # 置信区间
#     # ci_lower2 = gdp_late[-1] * (1 + np.percentile(cagr_samples2, 2.5)) ** (all_years2 - years_late[-1])
#     # ci_upper2 = gdp_late[-1] * (1 + np.percentile(cagr_samples2, 97.5)) ** (all_years2 - years_late[-1])
#     # plt.fill_between(all_years2[future_mask2], ci_lower2[future_mask2], ci_upper2[future_mask2],
#     #                      color="orange", alpha=0.2)
#     #
#     # # 估计点
#     # plt.scatter(target_year2, pred_mean2, color="red", zorder=5)
#     # plt.text(target_year2 - 3, pred_mean2, f"{pred_mean2:,.0f}",
#     #              color="red", fontsize=10, va="bottom", ha="right",
#     #              bbox=dict(facecolor="white", edgecolor="none", alpha=0.6))
#
#     # 美化
#     # plt.xticks(np.arange(2000, 2021, 2))
#     plt.xlabel("Year")
#     plt.ylabel("GDP (constant 2015 US$)")
#     plt.title(f"Yemen GDP Estimation to {target_year1}")
#     plt.legend()
#     plt.grid(True, alpha=0.3)
#     plt.tight_layout()
#     plt.show()

# === 主程序 ===
if __name__ == "__main__":
    # 1️⃣ 读取数据
    excel_path = r"F:\Yifan Teng\Data_new\API_NY.GDP.MKTP.KD_DS2_en_excel_v2_130141.xls"
    df = pd.read_excel(excel_path, sheet_name="Yemen")

    df = df.sort_values("year")
    years = df["year"].values
    gdp = df["GDP"].values

    # 2️⃣ 预测未来（例如 2020）
    target_year = 2020
    pred_mean, ci, cagr_samples = cagr_extrapolate(df, target_year=target_year)
    print(f"Estimated GDP in {target_year}: {pred_mean:.2f}")
    print(f"95% confidence interval: {ci}")

    # 3️⃣ 构建预测线
    cagr_mean = np.mean(cagr_samples)
    all_years = np.arange(years[0], target_year + 1)
    gdp_proj = gdp[0] * (1 + cagr_mean) ** (all_years - years[0])

    # 4️⃣ 绘图
    plt.figure(figsize=(8, 5))
    plt.plot(years, gdp, 'o-', color="steelblue", label="Actual data")

    # # 🔸未来年份部分（虚线）
    future_mask = all_years > years[-1]
    # plt.plot(all_years[future_mask], gdp_proj[future_mask], '--', color="orange", label="Projected trend")
    # plt.plot(all_years[future_mask], gdp_proj[future_mask], 'o', color="orange")

    # 置信区间
    ci_lower = gdp[-1] * (1 + np.percentile(cagr_samples, 2.5)) ** (all_years - years[-1])
    ci_upper = gdp[-1] * (1 + np.percentile(cagr_samples, 97.5)) ** (all_years - years[-1])
    plt.fill_between(all_years[future_mask], ci_lower[future_mask], ci_upper[future_mask],
                     color="orange", alpha=0.2, label="95% CI")

    # 估计点
    target_year2 = 2019
    pred_mean2, ci2, cagr_samples2 = cagr_extrapolate(df, target_year=target_year2)
    df_pred = pd.DataFrame(data=[[target_year2, pred_mean2],
                       [target_year, pred_mean]],
                 columns=['year', 'GDP'])
    # 🔸未来年份部分（虚线）
    years_pred = df_pred["year"].values
    gdp_pred = df_pred["GDP"].values
    plt.plot(years_pred, gdp_pred, '--', color="orange", label="Projected trend")
    plt.plot(target_year2, pred_mean2, 'o', color="orange")
    plt.scatter(target_year, pred_mean, color="red", zorder=5, label=f"Projected {target_year} GDP")

    plt.text(target_year - 1, pred_mean, f"{pred_mean:,.0f}",
             color="red", fontsize=10, va="bottom", ha="right",
             bbox=dict(facecolor="white", edgecolor="none", alpha=0.6))

    # 美化
    plt.xlabel("Year")
    plt.ylabel("GDP (constant 2015 US$)")
    plt.title(f"Yemen GDP Projection to {target_year}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
