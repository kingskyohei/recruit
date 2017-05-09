import input_login,input_entry,input_IS_entry,input_setumeikai
import make_report

import xlsxwriter
import csv
import pandas as pd

### 前処理：クレンジングと内定者データ取り込み(input:tsv)

## リクナビIDがない場合
# ①氏名の一致

# ②mail addressの一致

# ①と②の和集合

## リクナビIDがある場合

# ファイル分割

## 内定者ファイルの読み込み (GM_MASTER_ID)
naitei_cate1 = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/M_NINTEI.csv",sep="\t",names=['GM_MASTER_ID'])
naitei_cate2 = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/T_NINTEI.csv",sep="\t",names=['GM_MASTER_ID'])


### 集計処理(input:tsv output:csv)

## 各種データ取り込み(ログイン、ISエントリー、プレエントリー、説明会予約)
# ログイン情報
LOGIN_DATA = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/LOGIN.csv",sep="\t",
                         names=['GM_MASTER_ID','YM','LOGIN_KAISU'],
                         )

# ISエントリー情報
IS_ENTRY_DATA = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/IS_ENTRY.csv",sep="\t",
                         names=['GM_MASTER_ID','YM','IS_ENTRY_KAISU'],
                         )

# プレエントリー情報
PRE_ENTRY_DATA = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/PRE_ENTRY.csv",sep="\t",
                         names=['GM_MASTER_ID','YM','PRE_ENTRY_KAISU'],
                         )

# 説明会情報
SETUMEIKAI_DATA = pd.read_csv("D:/Users/01016964/Desktop/内定者分析関連\顔ぶれ分析/レオパレス加工/レオパレス21対応/python_input/.csv",sep="\t",
                         names=['GM_MASTER_ID','YM','_KAISU'],
                         )

# 集計
#  ログインの集計
input_login.login_kaisu(naitei_cate1,naitei_cate2,LOGIN_DATA)

# ISエントリーの集計
input_IS_entry.is_entry_kaisu(naitei_cate1,naitei_cate2,IS_ENTRY_DATA)

# プレエントリーの集計
input_entry.pre_entry_kaisu(naitei_cate1,naitei_cate2,PRE_ENTRY_DATA)

# 説明会予約の集計
input_setumeikai.setumeikai_kaisu(naitei_cate1,naitei_cate2,SETUMEIKAI_DATA)

### レポート出力(input:csv ouput:excelファイル)
make_report.make_report()
