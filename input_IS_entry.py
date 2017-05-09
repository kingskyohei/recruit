import pandas as pd

def is_entry_kaisu(naitei_cate1,naitei_cate2,IS_ENTRY_DATA):


    ##
    # 学生全体の処理

    # GM_MASTER_ID行の削除
    IS_ENTRY_DATA_CUS = IS_ENTRY_DATA.drop("GM_MASTER_ID", axis=1)

    # ISエントリー回数の平均値算出
    mean_is_entry_kaisu = IS_ENTRY_DATA_CUS.groupby(['YM']).mean()
    mean_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'MEAN_IS_ENTRY_KAISU'}, inplace=True)
    mean_is_entry_kaisu.sort_index(ascending=False)

    # ISエントリー回数の中央値算出
    median_is_entry_kaisu = IS_ENTRY_DATA_CUS.groupby(['YM']).median()
    median_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'MEDIAN_IS_ENTRY_KAISU'}, inplace=True)
    median_is_entry_kaisu.sort_index(ascending=False)

    # ISエントリー回数の合計値算出
    sum_is_entry_kaisu = IS_ENTRY_DATA_CUS.groupby(['YM']).sum()
    sum_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'SUM_IS_ENTRY_KAISU'}, inplace=True)
    sum_is_entry_kaisu.sort_index(ascending=False)

    # 全体のISエントリー回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    is_entry_merged = pd.merge(mean_is_entry_kaisu, median_is_entry_kaisu, left_index='YM', right_index='YM', how='inner', )
    is_entry_merged_2 = pd.merge(is_entry_merged, sum_is_entry_kaisu, left_index='YM', right_index='YM', how='inner')

    ##
    # M認定学生の処理

    # M認定の学生のISエントリー履歴を抽出
    M_IS_ENTRY_DATA = pd.merge(naitei_cate1, IS_ENTRY_DATA, left_on='GM_MASTER_ID', right_on='GM_MASTER_ID', how='inner',
                               suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    M_IS_ENTRY_DATA_CUS = M_IS_ENTRY_DATA.drop("GM_MASTER_ID", axis=1)

    # M認定の学生のISエントリー回数の平均値算出
    m_mean_is_entry_kaisu = M_IS_ENTRY_DATA_CUS.groupby(['YM']).mean()
    m_mean_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'MEAN_IS_ENTRY_KAISU'}, inplace=True)
    m_mean_is_entry_kaisu.sort_index(ascending=False)

    # M認定の学生のISエントリー回数の中央値算出
    m_median_is_entry_kaisu = M_IS_ENTRY_DATA_CUS.groupby(['YM']).median()
    m_median_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'MEDIAN_IS_ENTRY_KAISU'}, inplace=True)
    m_median_is_entry_kaisu.sort_index(ascending=False)

    # M認定の学生のISエントリー回数の合計値算出
    m_sum_is_entry_kaisu = M_IS_ENTRY_DATA_CUS.groupby(['YM']).sum()
    m_sum_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'SUM_IS_ENTRY_KAISU'}, inplace=True)
    m_sum_is_entry_kaisu.sort_index(ascending=False)

    # M認定の学生のISエントリー回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    m_is_entry_merged = pd.merge(m_mean_is_entry_kaisu, m_median_is_entry_kaisu, left_index='YM', right_index='YM',
                                 how='inner', )
    m_is_entry_merged_2 = pd.merge(m_is_entry_merged, m_sum_is_entry_kaisu, left_index='YM', right_index='YM', how='inner')

    # print(m_is_entry_merged_2)
    # 月ごとに全体のIS_ENTRY回数の平均値、中央値、合計値を求める


    ##
    # T認定学生の処理

    # T認定の学生のISエントリー履歴を抽出
    T_IS_ENTRY_DATA = pd.merge(naitei_cate2, IS_ENTRY_DATA, left_on='GM_MASTER_ID', right_on='GM_MASTER_ID', how='inner',
                               suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    T_IS_ENTRY_DATA_CUS = T_IS_ENTRY_DATA.drop("GM_MASTER_ID", axis=1)

    # T認定の学生のISエントリー回数の平均値算出
    t_mean_is_entry_kaisu = T_IS_ENTRY_DATA_CUS.groupby(['YM']).mean()
    t_mean_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'MEAN_IS_ENTRY_KAISU'}, inplace=True)
    t_mean_is_entry_kaisu.sort_index(ascending=False)

    # T認定の学生のISエントリー回数の中央値算出
    t_median_is_entry_kaisu = T_IS_ENTRY_DATA_CUS.groupby(['YM']).median()
    t_median_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'MEDIAN_IS_ENTRY_KAISU'}, inplace=True)
    t_median_is_entry_kaisu.sort_index(ascending=False)

    # T認定の学生のISエントリー回数の合計値算出
    t_sum_is_entry_kaisu = T_IS_ENTRY_DATA_CUS.groupby(['YM']).sum()
    t_sum_is_entry_kaisu.rename(columns={'IS_ENTRY_KAISU': 'SUM_IS_ENTRY_KAISU'}, inplace=True)
    t_sum_is_entry_kaisu.sort_index(ascending=False)

    # T認定の学生のISエントリー回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    t_is_entry_merged = pd.merge(t_mean_is_entry_kaisu, t_median_is_entry_kaisu, left_index='YM', right_index='YM',
                                 how='inner')
    t_is_entry_merged_2 = pd.merge(t_is_entry_merged, t_sum_is_entry_kaisu, left_index='YM', right_index='YM', how='inner')

    # 全体、M認定、T認定学生のデータの結合 is_entry_merged_2の結合
    is_entry_merged_ALL_M = pd.merge(is_entry_merged_2, m_is_entry_merged_2, left_index='YM', right_index='YM', how='inner',
                                     suffixes=('_all', '_m'))

    is_entry_merged_ALL_M_T = pd.merge(is_entry_merged_ALL_M, t_is_entry_merged_2, left_index='YM', right_index='YM',
                                       how='inner', suffixes=('_all_m', '_t'))
    is_entry_merged_ALL_M_T.rename(
        columns={'MEAN_IS_ENTRY_KAISU': 'MEAN_IS_ENTRY_KAISU_t', 'MEDIAN_IS_ENTRY_KAISU': 'MEDIAN_IS_ENTRY_KAISU_t',
                 'SUM_IS_ENTRY_KAISU': 'SUM_IS_ENTRY_KAISU_t'}, inplace=True)

    # 全体に対する計算値の算出 結合したデータの計算
    # M認定 平均値の全体比
    is_entry_merged_ALL_M_T['m_mean_dif'] = is_entry_merged_ALL_M_T['MEAN_IS_ENTRY_KAISU_m'] - is_entry_merged_ALL_M_T[
        'MEAN_IS_ENTRY_KAISU_all']
    is_entry_merged_ALL_M_T['m_median_dif'] = is_entry_merged_ALL_M_T['MEDIAN_IS_ENTRY_KAISU_m'] - is_entry_merged_ALL_M_T[
        'MEDIAN_IS_ENTRY_KAISU_all']

    # T認定 中央値の全体比
    is_entry_merged_ALL_M_T['t_mean_dif'] = is_entry_merged_ALL_M_T['MEAN_IS_ENTRY_KAISU_t'] - is_entry_merged_ALL_M_T[
        'MEAN_IS_ENTRY_KAISU_all']
    is_entry_merged_ALL_M_T['t_median_dif'] = is_entry_merged_ALL_M_T['MEDIAN_IS_ENTRY_KAISU_t'] - is_entry_merged_ALL_M_T[
        'MEDIAN_IS_ENTRY_KAISU_all']


    # 出力カラムの設定
    IS_ENTRY_CSV_DATA = is_entry_merged_ALL_M_T[["m_mean_dif", "m_median_dif", "t_mean_dif", "t_median_dif", "SUM_IS_ENTRY_KAISU_m", "SUM_IS_ENTRY_KAISU_t"]]

    # csvデータの出力
    IS_ENTRY_CSV_DATA.to_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/IS_ENTRY.csv',
                              index=True, encoding="utf-8")

