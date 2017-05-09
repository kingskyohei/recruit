import pandas as pd


def pre_entry_kaisu(naitei_cate1,naitei_cate2,PRE_ENTRY_DATA):

    ##
    # 学生全体の処理

    # GM_MASTER_ID行の削除
    PRE_ENTRY_DATA_CUS = PRE_ENTRY_DATA.drop("GM_MASTER_ID", axis=1)

    # プレエントリー回数の平均値算出
    mean_pre_entry_kaisu = PRE_ENTRY_DATA_CUS.groupby(['YM']).mean()
    mean_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'MEAN_PRE_ENTRY_KAISU'},inplace=True)
    mean_pre_entry_kaisu.sort_index(ascending=False)

    # プレエントリー回数の中央値算出
    median_pre_entry_kaisu = PRE_ENTRY_DATA_CUS.groupby(['YM']).median()
    median_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'MEDIAN_PRE_ENTRY_KAISU'},inplace=True)
    median_pre_entry_kaisu.sort_index(ascending=False)

    # プレエントリー回数の合計値算出
    sum_pre_entry_kaisu = PRE_ENTRY_DATA_CUS.groupby(['YM']).sum()
    sum_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'SUM_PRE_ENTRY_KAISU'},inplace=True)
    sum_pre_entry_kaisu.sort_index(ascending=False)

    # 全体のプレエントリー回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    pre_entry_merged = pd.merge(mean_pre_entry_kaisu,median_pre_entry_kaisu,left_index='YM',right_index='YM',how='inner',)
    pre_entry_merged_2 = pd.merge(pre_entry_merged,sum_pre_entry_kaisu,left_index='YM',right_index='YM',how='inner')

    ##
    # M認定学生の処理

    # M認定の学生のプレエントリー履歴を抽出
    M_PRE_ENTRY_DATA = pd.merge(naitei_cate1,PRE_ENTRY_DATA,left_on='GM_MASTER_ID',right_on='GM_MASTER_ID',how='inner',suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    M_PRE_ENTRY_DATA_CUS = M_PRE_ENTRY_DATA.drop("GM_MASTER_ID", axis=1)

    # M認定の学生のプレエントリー回数の平均値算出
    m_mean_pre_entry_kaisu = M_PRE_ENTRY_DATA_CUS.groupby(['YM']).mean()
    m_mean_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'MEAN_PRE_ENTRY_KAISU'},inplace=True)
    m_mean_pre_entry_kaisu.sort_index(ascending=False)

    # M認定の学生のプレエントリー回数の中央値算出
    m_median_pre_entry_kaisu = M_PRE_ENTRY_DATA_CUS.groupby(['YM']).median()
    m_median_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'MEDIAN_PRE_ENTRY_KAISU'},inplace=True)
    m_median_pre_entry_kaisu.sort_index(ascending=False)

    # M認定の学生のプレエントリー回数の合計値算出
    m_sum_pre_entry_kaisu = M_PRE_ENTRY_DATA_CUS.groupby(['YM']).count()
    m_sum_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'SUM_PRE_ENTRY_KAISU'},inplace=True)
    m_sum_pre_entry_kaisu.sort_index(ascending=False)

    # M認定の学生のプレエントリー回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    m_pre_entry_merged = pd.merge(m_mean_pre_entry_kaisu,m_median_pre_entry_kaisu,left_index='YM',right_index='YM',how='inner',)
    m_pre_entry_merged_2 = pd.merge(m_pre_entry_merged,m_sum_pre_entry_kaisu,left_index='YM',right_index='YM',how='inner')

    # print(m_pre_entry_merged_2)
    # 月ごとに全体のPRE_ENTRY回数の平均値、中央値、合計値を求める


    ##
    # T認定学生の処理

    # T認定の学生のプレエントリー履歴を抽出
    T_PRE_ENTRY_DATA = pd.merge(naitei_cate2,PRE_ENTRY_DATA,left_on='GM_MASTER_ID',right_on='GM_MASTER_ID',how='inner',suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    T_PRE_ENTRY_DATA_CUS = T_PRE_ENTRY_DATA.drop("GM_MASTER_ID", axis=1)

    # T認定の学生のプレエントリー回数の平均値算出
    t_mean_pre_entry_kaisu = T_PRE_ENTRY_DATA_CUS.groupby(['YM']).mean()
    t_mean_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'MEAN_PRE_ENTRY_KAISU'},inplace=True)
    t_mean_pre_entry_kaisu.sort_index(ascending=False)

    # T認定の学生のプレエントリー回数の中央値算出
    t_median_pre_entry_kaisu = T_PRE_ENTRY_DATA_CUS.groupby(['YM']).median()
    t_median_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'MEDIAN_PRE_ENTRY_KAISU'},inplace=True)
    t_median_pre_entry_kaisu.sort_index(ascending=False)

    # T認定の学生のプレエントリー回数の合計値算出
    t_sum_pre_entry_kaisu = T_PRE_ENTRY_DATA_CUS.groupby(['YM']).count()
    t_sum_pre_entry_kaisu.rename(columns={'PRE_ENTRY_KAISU':'SUM_PRE_ENTRY_KAISU'},inplace=True)
    t_sum_pre_entry_kaisu.sort_index(ascending=False)

    # T認定の学生のプレエントリー回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    t_pre_entry_merged = pd.merge(t_mean_pre_entry_kaisu,t_median_pre_entry_kaisu,left_index='YM',right_index='YM',how='inner')
    t_pre_entry_merged_2 = pd.merge(t_pre_entry_merged,t_sum_pre_entry_kaisu,left_index='YM',right_index='YM',how='inner')

    # 全体、M認定、T認定学生のデータの結合 pre_entry_merged_2の結合
    pre_entry_merged_ALL_M = pd.merge(pre_entry_merged_2,m_pre_entry_merged_2,left_index='YM',right_index='YM',how='inner',suffixes=('_all', '_m'))

    pre_entry_merged_ALL_M_T = pd.merge(pre_entry_merged_ALL_M,t_pre_entry_merged_2,left_index='YM',right_index='YM',how='inner',suffixes=('_all_m', '_t'))
    pre_entry_merged_ALL_M_T.rename(columns={'MEAN_PRE_ENTRY_KAISU':'MEAN_PRE_ENTRY_KAISU_t','MEDIAN_PRE_ENTRY_KAISU':'MEDIAN_PRE_ENTRY_KAISU_t','SUM_PRE_ENTRY_KAISU':'SUM_PRE_ENTRY_KAISU_t'},inplace=True)


    # 全体に対する計算値の算出 結合したデータの計算
    # M認定 平均値の全体比
    pre_entry_merged_ALL_M_T['m_mean_dif'] = pre_entry_merged_ALL_M_T['MEAN_PRE_ENTRY_KAISU_m'] - pre_entry_merged_ALL_M_T['MEAN_PRE_ENTRY_KAISU_all']
    pre_entry_merged_ALL_M_T['m_median_dif'] = pre_entry_merged_ALL_M_T['MEDIAN_PRE_ENTRY_KAISU_m'] - pre_entry_merged_ALL_M_T['MEDIAN_PRE_ENTRY_KAISU_all']

    # T認定 中央値の全体比
    pre_entry_merged_ALL_M_T['t_mean_dif'] = pre_entry_merged_ALL_M_T['MEAN_PRE_ENTRY_KAISU_t'] - pre_entry_merged_ALL_M_T['MEAN_PRE_ENTRY_KAISU_all']
    pre_entry_merged_ALL_M_T['t_median_dif'] = pre_entry_merged_ALL_M_T['MEDIAN_PRE_ENTRY_KAISU_t'] - pre_entry_merged_ALL_M_T['MEDIAN_PRE_ENTRY_KAISU_all']

    # 出力カラムの設定
    PRE_ENTRY_CSV_DATA = pre_entry_merged_ALL_M_T[["m_mean_dif","m_median_dif","t_mean_dif","t_median_dif","SUM_PRE_ENTRY_KAISU_m","SUM_PRE_ENTRY_KAISU_t"]]

    # csvデータの出力
    PRE_ENTRY_CSV_DATA.to_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/PRE_ENTRY.csv',index=True,encoding="utf-8")
