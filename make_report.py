import xlsxwriter
import csv
import pandas as pd

def make_report():
    workbook = xlsxwriter.Workbook('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_report/report.xlsx')
    worksheet = workbook.add_worksheet()

    # header行のフォーマット
    header_format = workbook.add_format({'align': 'center'})
    header_format.set_border(style=1)

    # 明細行のフォーマット
    string = workbook.add_format()
    string.set_border(style=1)
    integer = workbook.add_format({'num_format': '0'})
    integer.set_border(style=1)
    decimal = workbook.add_format({'num_format': '0.00'})
    decimal.set_border(style=1)
    percentage = workbook.add_format({'num_format': '0.0%'})
    percentage.set_border(style=1)

    # Create a new Chart object.
    # ログイン用
    login_line_chart_mean = workbook.add_chart({'type': 'line'})
    login_line_chart_median = workbook.add_chart({'type': 'line'})
    login_bar_chart = workbook.add_chart({'type': 'column'})

    # ISエントリー用
    is_entry_line_chart_mean = workbook.add_chart({'type': 'line'})
    is_entry_line_chart_median = workbook.add_chart({'type': 'line'})
    is_entry_bar_chart = workbook.add_chart({'type': 'column'})

    # エントリー用
    entry_line_chart_mean = workbook.add_chart({'type': 'line'})
    entry_line_chart_median = workbook.add_chart({'type': 'line'})
    entry_bar_chart = workbook.add_chart({'type': 'column'})

    # 説明会予約用
    setumeikai_line_chart_mean = workbook.add_chart({'type': 'line'})
    setumeikai_line_chart_median = workbook.add_chart({'type': 'line'})
    setumeikai_bar_chart = workbook.add_chart({'type': 'column'})

    file_login = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/LOGIN.csv')
    file_is_entry = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/IS_ENTRY.csv')
    file_entry = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/PRE_ENTRY.csv')
    file_setumeikai = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/SETUMEIKAI.csv')

    # ヘッダー行
    names_login = file_login.columns.values
    names_is_entry = file_is_entry.columns.values
    names_entry = file_entry.columns.values
    names_setumeikai = file_setumeikai.columns.values

    # header行の書き込み
    header_format.set_bg_color('#8fbc8f')

    worksheet.write_row('A1', names_login,header_format)
    worksheet.write_row('A41', names_is_entry,header_format)
    worksheet.write_row('A71', names_entry,header_format)
    worksheet.write_row('A101', names_setumeikai,header_format)

    # 明細行の設定

    # 明細行の書き込み
    # ログイン情報書き込み
    for i, ni in enumerate(names_login):
        worksheet.write_column('A2', file_login['YM'], string)
        worksheet.write_column('B2', file_login['M認定_来訪UU_平均値'], decimal)
        worksheet.write_column('C2', file_login['M認定_来訪UU_中央値'], decimal)
        worksheet.write_column('D2', file_login['T認定_来訪UU_平均値'], decimal)
        worksheet.write_column('E2', file_login['T認定_来訪UU_中央値'], decimal)
        worksheet.write_column('F2', file_login['M認定_UU数'], integer)
        worksheet.write_column('G2', file_login['T認定_UU数'], integer)

    # ISエントリー情報書き込み
    for i, ni in enumerate(names_entry):
        worksheet.write_column('A42', file_is_entry['YM'],string)
        worksheet.write_column('B42', file_is_entry['m_mean_dif'],decimal)
        worksheet.write_column('C42', file_is_entry['m_median_dif'],decimal)
        worksheet.write_column('D42', file_is_entry['t_mean_dif'],decimal)
        worksheet.write_column('E42', file_is_entry['t_median_dif'],decimal)
        worksheet.write_column('F42', file_is_entry['SUM_IS_ENTRY_KAISU_m'],integer)
        worksheet.write_column('G42', file_is_entry['SUM_IS_ENTRY_KAISU_t'],integer)

    # プレエントリー情報書き込み
    for i, ni in enumerate(names_entry):
        worksheet.write_column('A72', file_entry['YM'],string)
        worksheet.write_column('B72', file_entry['m_mean_dif'],decimal)
        worksheet.write_column('C72', file_entry['m_median_dif'],decimal)
        worksheet.write_column('D72', file_entry['t_mean_dif'],decimal)
        worksheet.write_column('E72', file_entry['t_median_dif'],decimal)
        worksheet.write_column('F72', file_entry['SUM_PRE_ENTRY_KAISU_m'],integer)
        worksheet.write_column('G72', file_entry['SUM_PRE_ENTRY_KAISU_t'],integer)

    # 説明会予約情報書き込み
    for i, ni in enumerate(names_entry):
        worksheet.write_column('A102', file_setumeikai['YM'],string)
        worksheet.write_column('B102', file_setumeikai['m_mean_dif'],decimal)
        worksheet.write_column('C102', file_setumeikai['m_median_dif'],decimal)
        worksheet.write_column('D102', file_setumeikai['t_mean_dif'],decimal)
        worksheet.write_column('E102', file_setumeikai['t_median_dif'],decimal)
        worksheet.write_column('F102', file_setumeikai['SUM_SETUMEIKAI_KAISU_m'],integer)
        worksheet.write_column('G102', file_setumeikai['SUM_SETUMEIKAI_KAISU_t'],integer)

    # 表の装飾
    #グラフの表示
    # 線グラフの描画

    # ログイン情報
    # 平均値
    login_line_chart_mean.add_series({'values': '=Sheet1!$B$2:$B$17','name': '=Sheet1!$B$1','marker': {'type': 'automatic'},})
    login_line_chart_mean.add_series({'values': '=Sheet1!$D$2:$D$17','name': '=Sheet1!$D$1','categories': '=Sheet1!$A$2:$A$17','marker': {'type': 'automatic'}})

    # 中央値
    login_line_chart_median.add_series({'values': '=Sheet1!$C$2:$C$17','name': '=Sheet1!$C$1','marker': {'type': 'automatic'}})
    login_line_chart_median.add_series({'values': '=Sheet1!$E$2:$E$17','name': '=Sheet1!$E$1','marker': {'type': 'automatic'},'categories': '=Sheet1!$A$2:$A$17'})

    # 棒グラフの描画
    login_bar_chart.add_series({'values': '=Sheet1!$F$2:$F$17','name': '=Sheet1!$F$1'})
    login_bar_chart.add_series({'values': '=Sheet1!$G$2:$G$17','categories': '=Sheet1!$A$2:$A$17','name':'=Sheet1!$G$1'})

    # ISエントリー情報
    # 平均値
    is_entry_line_chart_mean.add_series({'values': '=Sheet1!$B$42:$B$48','name': '=Sheet1!$B$41','marker': {'type': 'automatic'},})
    is_entry_line_chart_mean.add_series({'values': '=Sheet1!$D$42:$D$48','name': '=Sheet1!$D$41','categories': '=Sheet1!$A$42:$A$48','marker': {'type': 'automatic'}})

    # 中央値
    is_entry_line_chart_median.add_series({'values': '=Sheet1!$C$42:$C$48','name': '=Sheet1!$C$41','marker': {'type': 'automatic'}})
    is_entry_line_chart_median.add_series({'values': '=Sheet1!$E$42:$E$48','name': '=Sheet1!$E$41','marker': {'type': 'automatic'},'categories': '=Sheet1!$A$42:$A$48'})

    # 棒グラフの描画
    is_entry_bar_chart.add_series({'values': '=Sheet1!$F$42:$F$48','name': '=Sheet1!$F$41'})
    is_entry_bar_chart.add_series({'values': '=Sheet1!$G$42:$G$48','categories': '=Sheet1!$A$42:$A$48','name':'=Sheet1!$G$41'})


    # エントリー情報
    # 平均値
    entry_line_chart_mean.add_series({'values': '=Sheet1!$B$72:$B$78','name': '=Sheet1!$B$71','marker': {'type': 'automatic'},})
    entry_line_chart_mean.add_series({'values': '=Sheet1!$D$72:$D$78','name': '=Sheet1!$D$71','categories': '=Sheet1!$A$72:$A$78','marker': {'type': 'automatic'}})

    # 中央値
    entry_line_chart_median.add_series({'values': '=Sheet1!$C$72:$C$78','name': '=Sheet1!$C$71','marker': {'type': 'automatic'}})
    entry_line_chart_median.add_series({'values': '=Sheet1!$E$72:$E$78','name': '=Sheet1!$E$71','marker': {'type': 'automatic'},'categories': '=Sheet1!$A$72:$A$78'})

    # 棒グラフの描画
    entry_bar_chart.add_series({'values': '=Sheet1!$F$72:$F$78','name': '=Sheet1!$F$71'})
    entry_bar_chart.add_series({'values': '=Sheet1!$G$72:$G$78','categories': '=Sheet1!$A$72:$A$78','name':'=Sheet1!$G$71'})

    # 説明会予約情報
    # 平均値
    setumeikai_line_chart_mean.add_series({'values': '=Sheet1!$B$102:$B$108','name': '=Sheet1!$B$101','marker': {'type': 'automatic'},})
    setumeikai_line_chart_mean.add_series({'values': '=Sheet1!$D$102:$D$108','name': '=Sheet1!$D$101','categories': '=Sheet1!$A$102:$A$108','marker': {'type': 'automatic'}})

    # 中央値
    setumeikai_line_chart_median.add_series({'values': '=Sheet1!$C$102:$C$108','name': '=Sheet1!$C$101','marker': {'type': 'automatic'}})
    setumeikai_line_chart_median.add_series({'values': '=Sheet1!$E$102:$E$108','name': '=Sheet1!$E$101','marker': {'type': 'automatic'},'categories': '=Sheet1!$A$102:$A$108'})

    # 棒グラフの描画
    setumeikai_bar_chart.add_series({'values': '=Sheet1!$F$102:$F$108','name': '=Sheet1!$F$101'})
    setumeikai_bar_chart.add_series({'values': '=Sheet1!$G$102:$G$108','categories': '=Sheet1!$A$102:$A$108','name':'=Sheet1!$G$101'})

    # 棒グラフ/平均値の装飾
    # グラフサイズの設定
    login_bar_chart.set_size({'width': 400, 'height': 320})
    is_entry_bar_chart.set_size({'width': 400, 'height': 320})
    entry_bar_chart.set_size({'width': 400, 'height': 320})
    setumeikai_bar_chart.set_size({'width': 400, 'height': 320})

    # グラフタイトルの設定
    login_bar_chart.set_title({'name': 'ログインユーザー数','name_font': {'size': 12, 'メイリオ': True}})
    is_entry_bar_chart.set_title({'name': 'ISエントリーユーザー数','name_font': {'size': 12, 'メイリオ': True}})
    entry_bar_chart.set_title({'name': 'プレエントリーユーザー数','name_font': {'size': 12, 'メイリオ': True}})
    setumeikai_bar_chart.set_title({'name': '説明会予約ユーザー数','name_font': {'size': 12, 'メイリオ': True}})

    # X軸の設定
    login_bar_chart.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
        'date_axis': True,
        'minor_unit': 7,
        'minor_unit_type': 'months',
    })

    is_entry_bar_chart.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
        'date_axis': True,
        'minor_unit': 7,
        'minor_unit_type': 'months',
    })

    entry_bar_chart.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
        'date_axis': True,
        'minor_unit': 7,
        'minor_unit_type': 'months',
    })

    setumeikai_bar_chart.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
        'date_axis': True,
        'minor_unit': 7,
        'minor_unit_type': 'months',
    })

    # Y軸の設定
    login_bar_chart.set_y_axis({'visible': True})
    is_entry_bar_chart.set_y_axis({'visible': True})
    entry_bar_chart.set_y_axis({'visible': True})
    setumeikai_bar_chart.set_y_axis({'visible': True})

    # 棒グラフ/中央値
    # グラフサイズの設定
    login_line_chart_mean.set_size({'width': 400, 'height': 320})
    login_line_chart_median.set_size({'width': 400, 'height': 320})

    is_entry_line_chart_mean.set_size({'width': 400, 'height': 320})
    is_entry_line_chart_median.set_size({'width': 400, 'height': 320})

    entry_line_chart_mean.set_size({'width': 400, 'height': 320})
    entry_line_chart_median.set_size({'width': 400, 'height': 320})

    setumeikai_line_chart_mean.set_size({'width': 400, 'height': 320})
    setumeikai_line_chart_median.set_size({'width': 400, 'height': 320})

    # グラフタイトルの設定
    login_line_chart_mean.set_title({'name': 'ログイン回数/平均値','name_font': {'size': 12, 'メイリオ': True}})
    login_line_chart_median.set_title({'name': 'ログイン回数/中央値','name_font': {'size': 12, 'メイリオ': True}})

    is_entry_line_chart_mean.set_title({'name': 'ISエントリー回数/平均値','name_font': {'size': 12, 'メイリオ': True}})
    is_entry_line_chart_median.set_title({'name': 'ISエントリー回数/中央値','name_font': {'size': 12, 'メイリオ': True}})

    entry_line_chart_mean.set_title({'name': 'プレエントリー回数/平均値','name_font': {'size': 12, 'メイリオ': True}})
    entry_line_chart_median.set_title({'name': 'プレエントリー回数/中央値','name_font': {'size': 12, 'メイリオ': True}})

    setumeikai_line_chart_mean.set_title({'name': '説明会予約回数/平均値','name_font': {'size': 12, 'メイリオ': True}})
    setumeikai_line_chart_median.set_title({'name': '説明会予約回数/中央値','name_font': {'size': 12, 'メイリオ': True}})

    # X軸の設定
    login_line_chart_mean.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    is_entry_line_chart_mean.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    entry_line_chart_mean.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    setumeikai_line_chart_mean.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })


    login_line_chart_median.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    is_entry_line_chart_median.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    entry_line_chart_median.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    setumeikai_line_chart_median.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    # 凡例の設定
    # 棒グラフの凡例
    login_bar_chart.set_legend({'position': 'bottom'})
    is_entry_bar_chart.set_legend({'position': 'bottom'})
    entry_bar_chart.set_legend({'position': 'bottom'})
    setumeikai_bar_chart.set_legend({'position': 'bottom'})

    # 線グラフの凡例
    login_line_chart_mean.set_legend({'position': 'bottom'})
    is_entry_line_chart_mean.set_legend({'position': 'bottom'})
    entry_line_chart_mean.set_legend({'position': 'bottom'})
    setumeikai_line_chart_mean.set_legend({'position': 'bottom'})

    login_line_chart_median.set_legend({'position': 'bottom'})
    is_entry_line_chart_median.set_legend({'position': 'bottom'})
    entry_line_chart_median.set_legend({'position': 'bottom'})
    setumeikai_line_chart_median.set_legend({'position': 'bottom'})

    # chart1.add_series({'values': '=Sheet1!$A$1:$A$5'})
    # chart1.add_series({'values': '=Sheet1!$B$1:$B$5'})
    # chart1.add_series({'values': '=Sheet1!$C$1:$C$5'})
    # Insert the chart into the worksheet.

    # ログイン情報
    worksheet.insert_chart('A19', login_line_chart_mean)
    worksheet.insert_chart('H19', login_line_chart_median)
    worksheet.insert_chart('O19', login_bar_chart)

    # ISエントリー情報
    worksheet.insert_chart('A52', is_entry_line_chart_mean)
    worksheet.insert_chart('H52', is_entry_line_chart_median)
    worksheet.insert_chart('O52', is_entry_bar_chart)

    # エントリー情報
    worksheet.insert_chart('A80', entry_line_chart_mean)
    worksheet.insert_chart('H80', entry_line_chart_median)
    worksheet.insert_chart('O80', entry_bar_chart)

    # 説明会予約情報
    worksheet.insert_chart('A110', setumeikai_line_chart_mean)
    worksheet.insert_chart('H110', setumeikai_line_chart_median)
    worksheet.insert_chart('O110', setumeikai_bar_chart)

    workbook.close()

make_report()