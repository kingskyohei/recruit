import pandas as pd


def login_kaisu(naitei_cate1,naitei_cate2,LOGIN_DATA):

    ##
    # 学生全体の処理

    # GM_MASTER_ID行の削除
    LOGIN_DATA_CUS = LOGIN_DATA.drop("GM_MASTER_ID", axis=1)

    # ログイン回数の平均値算出
    mean_login_kaisu = LOGIN_DATA_CUS.groupby(['YM']).mean()
    mean_login_kaisu.rename(columns={'LOGIN_KAISU':'MEAN_LOGIN_KAISU'},inplace=True)
    mean_login_kaisu.sort_index(ascending=False)

    # ログイン回数の中央値算出
    median_login_kaisu = LOGIN_DATA_CUS.groupby(['YM']).median()
    median_login_kaisu.rename(columns={'LOGIN_KAISU':'MEDIAN_LOGIN_KAISU'},inplace=True)
    median_login_kaisu.sort_index(ascending=False)

    # ログイン回数の合計値算出
    sum_login_kaisu = LOGIN_DATA_CUS.groupby(['YM']).sum()
    sum_login_kaisu.rename(columns={'LOGIN_KAISU':'SUM_LOGIN_KAISU'},inplace=True)
    sum_login_kaisu.sort_index(ascending=False)

    # 全体のログイン回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    login_merged = pd.merge(mean_login_kaisu,median_login_kaisu,left_index='YM',right_index='YM',how='inner',)
    login_merged_2 = pd.merge(login_merged,sum_login_kaisu,left_index='YM',right_index='YM',how='inner')

    ##
    # M認定学生の処理

    # M認定の学生のログイン履歴を抽出
    M_LOGIN_DATA = pd.merge(naitei_cate1,LOGIN_DATA,left_on='GM_MASTER_ID',right_on='GM_MASTER_ID',how='inner',suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    M_LOGIN_DATA_CUS = M_LOGIN_DATA.drop("GM_MASTER_ID", axis=1)

    # M認定の学生のログイン回数の平均値算出
    m_mean_login_kaisu = M_LOGIN_DATA_CUS.groupby(['YM']).mean()
    m_mean_login_kaisu.rename(columns={'LOGIN_KAISU':'MEAN_LOGIN_KAISU'},inplace=True)
    m_mean_login_kaisu.sort_index(ascending=False)

    # M認定の学生のログイン回数の中央値算出
    m_median_login_kaisu = M_LOGIN_DATA_CUS.groupby(['YM']).median()
    m_median_login_kaisu.rename(columns={'LOGIN_KAISU':'MEDIAN_LOGIN_KAISU'},inplace=True)
    m_median_login_kaisu.sort_index(ascending=False)

    # M認定の学生のログイン回数の合計値算出
    m_sum_login_kaisu = M_LOGIN_DATA_CUS.groupby(['YM']).sum()
    m_sum_login_kaisu.rename(columns={'LOGIN_KAISU':'SUM_LOGIN_KAISU'},inplace=True)
    m_sum_login_kaisu.sort_index(ascending=False)

    # M認定の学生のログイン回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    m_login_merged = pd.merge(m_mean_login_kaisu,m_median_login_kaisu,left_index='YM',right_index='YM',how='inner',)
    m_login_merged_2 = pd.merge(m_login_merged,m_sum_login_kaisu,left_index='YM',right_index='YM',how='inner')

    # print(m_login_merged_2)
    # 月ごとに全体のLOGIN回数の平均値、中央値、合計値を求める


    ##
    # T認定学生の処理

    # T認定の学生のログイン履歴を抽出
    T_LOGIN_DATA = pd.merge(naitei_cate2,LOGIN_DATA,left_on='GM_MASTER_ID',right_on='GM_MASTER_ID',how='inner',suffixes=('_test', '_class'))

    # GM_MASTER_ID行の削除
    T_LOGIN_DATA_CUS = T_LOGIN_DATA.drop("GM_MASTER_ID", axis=1)

    # T認定の学生のログイン回数の平均値算出
    t_mean_login_kaisu = T_LOGIN_DATA_CUS.groupby(['YM']).mean()
    t_mean_login_kaisu.rename(columns={'LOGIN_KAISU':'MEAN_LOGIN_KAISU'},inplace=True)
    t_mean_login_kaisu.sort_index(ascending=False)

    # T認定の学生のログイン回数の中央値算出
    t_median_login_kaisu = T_LOGIN_DATA_CUS.groupby(['YM']).median()
    t_median_login_kaisu.rename(columns={'LOGIN_KAISU':'MEDIAN_LOGIN_KAISU'},inplace=True)
    t_median_login_kaisu.sort_index(ascending=False)

    # T認定の学生のログイン回数の合計値算出
    t_sum_login_kaisu = T_LOGIN_DATA_CUS.groupby(['YM']).sum()
    t_sum_login_kaisu.rename(columns={'LOGIN_KAISU':'SUM_LOGIN_KAISU'},inplace=True)
    t_sum_login_kaisu.sort_index(ascending=False)

    # T認定の学生のログイン回数を月ごとに平均値、中央値、合計値の順で並べる indexであるYMを使って結合
    t_login_merged = pd.merge(t_mean_login_kaisu,t_median_login_kaisu,left_index='YM',right_index='YM',how='inner')
    t_login_merged_2 = pd.merge(t_login_merged,t_sum_login_kaisu,left_index='YM',right_index='YM',how='inner')

    # 全体、M認定、T認定学生のデータの結合 login_merged_2の結合
    login_merged_ALL_M = pd.merge(login_merged_2,m_login_merged_2,left_index='YM',right_index='YM',how='inner',suffixes=('_all', '_m'))

    login_merged_ALL_M_T = pd.merge(login_merged_ALL_M,t_login_merged_2,left_index='YM',right_index='YM',how='inner',suffixes=('_all_m', '_t'))
    login_merged_ALL_M_T.rename(columns={'MEAN_LOGIN_KAISU':'MEAN_LOGIN_KAISU_t','MEDIAN_LOGIN_KAISU':'MEDIAN_LOGIN_KAISU_t','SUM_LOGIN_KAISU':'SUM_LOGIN_KAISU_t'},inplace=True)


    # 全体に対する計算値の算出 結合したデータの計算
    # M認定 平均値の全体比
    login_merged_ALL_M_T['m_mean_dif'] = login_merged_ALL_M_T['MEAN_LOGIN_KAISU_m'] - login_merged_ALL_M_T['MEAN_LOGIN_KAISU_all']
    login_merged_ALL_M_T['m_median_dif'] = login_merged_ALL_M_T['MEDIAN_LOGIN_KAISU_m'] - login_merged_ALL_M_T['MEDIAN_LOGIN_KAISU_all']

    # T認定 中央値の全体比
    login_merged_ALL_M_T['t_mean_dif'] = login_merged_ALL_M_T['MEAN_LOGIN_KAISU_t'] - login_merged_ALL_M_T['MEAN_LOGIN_KAISU_all']
    login_merged_ALL_M_T['t_median_dif'] = login_merged_ALL_M_T['MEDIAN_LOGIN_KAISU_t'] - login_merged_ALL_M_T['MEDIAN_LOGIN_KAISU_all']

    # login_merged_ALL_M_T['sum_dif'] = login_merged_ALL_M_T['MEDIAN_LOGIN_KAISU_m'] - login_merged_ALL_M_T['MEDIAN_LOGIN_KAISU_all']

    # 出力カラムの設定
    # GM_MASTER_ID行の削除
    print(login_merged_ALL_M_T)
    LOGIN_CSV_DATA = login_merged_ALL_M_T[["m_mean_dif","m_median_dif","t_mean_dif","t_median_dif","SUM_LOGIN_KAISU_m","SUM_LOGIN_KAISU_t"]]

    # print(LOGIN_CSV_DATA)
    # csvデータの出力
    LOGIN_CSV_DATA.to_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/LOGIN.csv',index=True,encoding="utf-8")


##
# ログイン回数集計の関数呼び出し

# # 内定者のID取り込み
# naitei_cate1 = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/M_NINTEI.csv",sep="\t",names=['GM_MASTER_ID'])
# naitei_cate2 = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/T_NINTEI.csv",sep="\t",names=['GM_MASTER_ID'])
#
# # 各種データ取り込み
# # ログイン情報
# LOGIN_DATA = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/LOGIN.csv",sep="\t",
#                          names=['GM_MASTER_ID','YM','LOGIN_KAISU'],
#                          )
# login = LOGIN()
# login.login_kaisu(naitei_cate1,naitei_cate2,LOGIN_DATA)
# # login_kaisu()