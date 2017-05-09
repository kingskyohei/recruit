import pandas as pd

def setumeikai_kaisu(naitei_cate1,naitei_cate2,SETUMEIKAI_DATA):

    ##
    # 学生全体の処理

    # GM_MASTER_ID行の削除
    SETUMEIKAI_DATA_CUS = SETUMEIKAI_DATA.drop("GM_MASTER_ID", axis=1)

    # ログイン回数の平均値算出
    mean_setumeikai_kaisu = SETUMEIKAI_DATA_CUS.groupby(['YM']).mean()
    mean_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'MEAN_SETUMEIKAI_KAISU'}, inplace=True)
    mean_setumeikai_kaisu.sort_index(ascending=False)

    # ログイン回数の中央値算出
    median_setumeikai_kaisu = SETUMEIKAI_DATA_CUS.groupby(['YM']).median()
    median_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'MEDIAN_SETUMEIKAI_KAISU'}, inplace=True)
    median_setumeikai_kaisu.sort_index(ascending=False)

    # ログイン回数の合計値算出
    sum_setumeikai_kaisu = SETUMEIKAI_DATA_CUS.groupby(['YM']).sum()
    sum_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'SUM_SETUMEIKAI_KAISU'}, inplace=True)
    sum_setumeikai_kaisu.sort_index(ascending=False)

    # 全体のログイン回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    setumeikai_merged = pd.merge(mean_setumeikai_kaisu, median_setumeikai_kaisu, left_index='YM', right_index='YM',
                                 how='inner', )
    setumeikai_merged_2 = pd.merge(setumeikai_merged, sum_setumeikai_kaisu, left_index='YM', right_index='YM', how='inner')

    ##
    # M認定学生の処理

    # M認定の学生のログイン履歴を抽出
    M_SETUMEIKAI_DATA = pd.merge(naitei_cate1, SETUMEIKAI_DATA, left_on='GM_MASTER_ID', right_on='GM_MASTER_ID',
                                 how='inner', suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    M_SETUMEIKAI_DATA_CUS = M_SETUMEIKAI_DATA.drop("GM_MASTER_ID", axis=1)

    # M認定の学生のログイン回数の平均値算出
    m_mean_setumeikai_kaisu = M_SETUMEIKAI_DATA_CUS.groupby(['YM']).mean()
    m_mean_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'MEAN_SETUMEIKAI_KAISU'}, inplace=True)
    m_mean_setumeikai_kaisu.sort_index(ascending=False)

    # M認定の学生のログイン回数の中央値算出
    m_median_setumeikai_kaisu = M_SETUMEIKAI_DATA_CUS.groupby(['YM']).median()
    m_median_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'MEDIAN_SETUMEIKAI_KAISU'}, inplace=True)
    m_median_setumeikai_kaisu.sort_index(ascending=False)

    # M認定の学生のログイン回数の合計値算出
    m_sum_setumeikai_kaisu = M_SETUMEIKAI_DATA_CUS.groupby(['YM']).sum()
    m_sum_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'SUM_SETUMEIKAI_KAISU'}, inplace=True)
    m_sum_setumeikai_kaisu.sort_index(ascending=False)

    # M認定の学生のログイン回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    m_setumeikai_merged = pd.merge(m_mean_setumeikai_kaisu, m_median_setumeikai_kaisu, left_index='YM', right_index='YM',
                                   how='inner', )
    m_setumeikai_merged_2 = pd.merge(m_setumeikai_merged, m_sum_setumeikai_kaisu, left_index='YM', right_index='YM',
                                     how='inner')


    ##
    # T認定学生の処理

    # T認定の学生のログイン履歴を抽出
    T_SETUMEIKAI_DATA = pd.merge(naitei_cate2, SETUMEIKAI_DATA, left_on='GM_MASTER_ID', right_on='GM_MASTER_ID',
                                 how='inner', suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    T_SETUMEIKAI_DATA_CUS = T_SETUMEIKAI_DATA.drop("GM_MASTER_ID", axis=1)

    # T認定の学生のログイン回数の平均値算出
    t_mean_setumeikai_kaisu = T_SETUMEIKAI_DATA_CUS.groupby(['YM']).mean()
    t_mean_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'MEAN_SETUMEIKAI_KAISU'}, inplace=True)
    t_mean_setumeikai_kaisu.sort_index(ascending=False)

    # T認定の学生のログイン回数の中央値算出
    t_median_setumeikai_kaisu = T_SETUMEIKAI_DATA_CUS.groupby(['YM']).median()
    t_median_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'MEDIAN_SETUMEIKAI_KAISU'}, inplace=True)
    t_median_setumeikai_kaisu.sort_index(ascending=False)

    # T認定の学生のログイン回数の合計値算出
    t_sum_setumeikai_kaisu = T_SETUMEIKAI_DATA_CUS.groupby(['YM']).sum()
    t_sum_setumeikai_kaisu.rename(columns={'SETUMEIKAI_KAISU': 'SUM_SETUMEIKAI_KAISU'}, inplace=True)
    t_sum_setumeikai_kaisu.sort_index(ascending=False)

    # T認定の学生のログイン回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    t_setumeikai_merged = pd.merge(t_mean_setumeikai_kaisu, t_median_setumeikai_kaisu, left_index='YM', right_index='YM',
                                   how='inner')
    t_setumeikai_merged_2 = pd.merge(t_setumeikai_merged, t_sum_setumeikai_kaisu, left_index='YM', right_index='YM',
                                     how='inner')

    # 全体、M認定、T認定学生のデータの結合 setumeikai_merged_2の結合
    setumeikai_merged_ALL_M = pd.merge(setumeikai_merged_2, m_setumeikai_merged_2, left_index='YM', right_index='YM',
                                       how='inner', suffixes=('_all', '_m'))

    setumeikai_merged_ALL_M_T = pd.merge(setumeikai_merged_ALL_M, t_setumeikai_merged_2, left_index='YM', right_index='YM',
                                         how='inner', suffixes=('_all_m', '_t'))
    setumeikai_merged_ALL_M_T.rename(
        columns={'MEAN_SETUMEIKAI_KAISU': 'MEAN_SETUMEIKAI_KAISU_t', 'MEDIAN_SETUMEIKAI_KAISU': 'MEDIAN_SETUMEIKAI_KAISU_t',
                 'SUM_SETUMEIKAI_KAISU': 'SUM_SETUMEIKAI_KAISU_t'}, inplace=True)

    # 全体に対する計算値の算出 結合したデータの計算
    # M認定 平均値の全体比
    setumeikai_merged_ALL_M_T['m_mean_dif'] = setumeikai_merged_ALL_M_T['MEAN_SETUMEIKAI_KAISU_m'] - \
                                              setumeikai_merged_ALL_M_T['MEAN_SETUMEIKAI_KAISU_all']
    setumeikai_merged_ALL_M_T['m_median_dif'] = setumeikai_merged_ALL_M_T['MEDIAN_SETUMEIKAI_KAISU_m'] - \
                                                setumeikai_merged_ALL_M_T['MEDIAN_SETUMEIKAI_KAISU_all']

    # T認定 中央値の全体比
    setumeikai_merged_ALL_M_T['t_mean_dif'] = setumeikai_merged_ALL_M_T['MEAN_SETUMEIKAI_KAISU_t'] - \
                                              setumeikai_merged_ALL_M_T['MEAN_SETUMEIKAI_KAISU_all']
    setumeikai_merged_ALL_M_T['t_median_dif'] = setumeikai_merged_ALL_M_T['MEDIAN_SETUMEIKAI_KAISU_t'] - \
                                                setumeikai_merged_ALL_M_T['MEDIAN_SETUMEIKAI_KAISU_all']


    # 出力カラムの設定
    SETUMEIKAI_CSV_DATA = setumeikai_merged_ALL_M_T[
        ["m_mean_dif", "m_median_dif", "t_mean_dif", "t_median_dif", "SUM_SETUMEIKAI_KAISU_m", "SUM_SETUMEIKAI_KAISU_t"]]

    # csvデータの出力
    SETUMEIKAI_CSV_DATA.to_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/SETUMEIKAI.csv',
                             index=True, encoding="utf-8")

