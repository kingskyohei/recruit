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

    # エントリー用
    entry_line_chart_mean = workbook.add_chart({'type': 'line'})
    entry_line_chart_median = workbook.add_chart({'type': 'line'})
    entry_bar_chart = workbook.add_chart({'type': 'column'})


    file_login = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/LOGIN.csv')
    file_is_entry = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/IS_ENTRY.csv')
    file_entry = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/PRE_ENTRY.csv')
    file_setumeikai = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/SETUMEIKAI.csv')

    # ヘッダー行
    names_login = file_login.columns.values
    names_entry = file_entry.columns.values

    # header行の書き込み
    header_format.set_bg_color('#8fbc8f')

    worksheet.write_row('A1', names_login,header_format)
    worksheet.write_row('A41', names_entry,header_format)

    # 明細行の設定

    # 明細行の書き込み
    # ログイン情報書き込み
    for i, ni in enumerate(names_login):
        worksheet.write_column('A2', file_login['YM'], string)
        worksheet.write_column('B2', file_login['m_mean_dif'], decimal)
        worksheet.write_column('C2', file_login['m_median_dif'], decimal)
        worksheet.write_column('D2', file_login['t_mean_dif'], decimal)
        worksheet.write_column('E2', file_login['t_median_dif'], decimal)
        worksheet.write_column('F2', file_login['SUM_LOGIN_KAISU_m'], integer)
        worksheet.write_column('G2', file_login['SUM_LOGIN_KAISU_t'], integer)

    # ISエントリー情報書き込み
    for i, ni in enumerate(names_entry):
        worksheet.write_column('A42', file_entry['YM'],string)
        worksheet.write_column('B42', file_entry['m_mean_dif'],decimal)
        worksheet.write_column('C42', file_entry['m_median_dif'],decimal)
        worksheet.write_column('D42', file_entry['t_mean_dif'],decimal)
        worksheet.write_column('E42', file_entry['t_median_dif'],decimal)
        worksheet.write_column('F42', file_entry['SUM_PRE_ENTRY_KAISU_m'],integer)
        worksheet.write_column('G42', file_entry['SUM_PRE_ENTRY_KAISU_t'],integer)



    # 表の装飾
    #グラフの表示
    # 線グラフの描画

    # ログイン情報
    # 平均値
    login_line_chart_mean.add_series({'values': '=Sheet1!$B$2:$B$8','name': '=Sheet1!$B$1','marker': {'type': 'automatic'},})
    login_line_chart_mean.add_series({'values': '=Sheet1!$D$2:$D$8','name': '=Sheet1!$D$1','categories': '=Sheet1!$A$2:$A$8','marker': {'type': 'automatic'}})

    # 中央値
    login_line_chart_median.add_series({'values': '=Sheet1!$C$2:$C$8','name': '=Sheet1!$C$1','marker': {'type': 'automatic'}})
    login_line_chart_median.add_series({'values': '=Sheet1!$E$2:$E$8','name': '=Sheet1!$E$1','marker': {'type': 'automatic'},'categories': '=Sheet1!$A$2:$A$8'})

    # 棒グラフの描画
    login_bar_chart.add_series({'values': '=Sheet1!$F$2:$F$8','name': '=Sheet1!$F$1'})
    login_bar_chart.add_series({'values': '=Sheet1!$G$2:$G$8','categories': '=Sheet1!$A$2:$A$8','name':'=Sheet1!$G$1'})

    # エントリー情報
    # 平均値
    entry_line_chart_mean.add_series({'values': '=Sheet1!$B$42:$B$48','name': '=Sheet1!$B$41','marker': {'type': 'automatic'},})
    entry_line_chart_mean.add_series({'values': '=Sheet1!$D$42:$D$48','name': '=Sheet1!$D$41','categories': '=Sheet1!$A$42:$A$48','marker': {'type': 'automatic'}})

    # 中央値
    entry_line_chart_median.add_series({'values': '=Sheet1!$C$42:$C$48','name': '=Sheet1!$C$41','marker': {'type': 'automatic'}})
    entry_line_chart_median.add_series({'values': '=Sheet1!$E$42:$E$48','name': '=Sheet1!$E$41','marker': {'type': 'automatic'},'categories': '=Sheet1!$A$42:$A$48'})

    # 棒グラフの描画
    entry_bar_chart.add_series({'values': '=Sheet1!$F$42:$F$48','name': '=Sheet1!$F$41'})
    entry_bar_chart.add_series({'values': '=Sheet1!$G$42:$G$48','categories': '=Sheet1!$A$42:$A$48','name':'=Sheet1!$G$41'})



    # 棒グラフ/平均値の装飾
    # グラフサイズの設定
    login_bar_chart.set_size({'width': 400, 'height': 320})
    entry_bar_chart.set_size({'width': 400, 'height': 320})

    # グラフタイトルの設定
    login_bar_chart.set_title({'name': 'ログインユーザー数','name_font': {'size': 12, 'メイリオ': True}})
    entry_bar_chart.set_title({'name': 'エントリーユーザー数','name_font': {'size': 12, 'メイリオ': True}})

    # X軸の設定
    login_bar_chart.set_x_axis({
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

    # Y軸の設定
    login_bar_chart.set_y_axis({'visible': True})
    entry_bar_chart.set_y_axis({'visible': True})

    # 棒グラフ/中央値
    # グラフサイズの設定
    login_line_chart_mean.set_size({'width': 400, 'height': 320})
    login_line_chart_median.set_size({'width': 400, 'height': 320})

    entry_line_chart_mean.set_size({'width': 400, 'height': 320})
    entry_line_chart_median.set_size({'width': 400, 'height': 320})

    # グラフタイトルの設定
    login_line_chart_mean.set_title({'name': 'ログイン回数/平均値','name_font': {'size': 12, 'メイリオ': True}})
    login_line_chart_median.set_title({'name': 'ログイン回数/中央値','name_font': {'size': 12, 'メイリオ': True}})

    entry_line_chart_mean.set_title({'name': 'エントリー回数/平均値','name_font': {'size': 12, 'メイリオ': True}})
    entry_line_chart_median.set_title({'name': 'エントリー回数/中央値','name_font': {'size': 12, 'メイリオ': True}})

    # X軸の設定
    login_line_chart_mean.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    entry_line_chart_mean.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    login_line_chart_median.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    entry_line_chart_median.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    # 凡例の設定
    # 棒グラフの凡例
    login_bar_chart.set_legend({'position': 'bottom'})
    entry_bar_chart.set_legend({'position': 'bottom'})

    # 線グラフの凡例
    login_line_chart_mean.set_legend({'position': 'bottom'})
    entry_line_chart_mean.set_legend({'position': 'bottom'})

    login_line_chart_median.set_legend({'position': 'bottom'})
    entry_line_chart_median.set_legend({'position': 'bottom'})

    # chart1.add_series({'values': '=Sheet1!$A$1:$A$5'})
    # chart1.add_series({'values': '=Sheet1!$B$1:$B$5'})
    # chart1.add_series({'values': '=Sheet1!$C$1:$C$5'})
    # Insert the chart into the worksheet.

    # ログイン情報
    worksheet.insert_chart('A19', login_line_chart_mean)
    worksheet.insert_chart('H19', login_line_chart_median)
    worksheet.insert_chart('O19', login_bar_chart)

    # エントリー情報
    worksheet.insert_chart('A50', entry_line_chart_mean)
    worksheet.insert_chart('H50', entry_line_chart_median)
    worksheet.insert_chart('O50', entry_bar_chart)
    # worksheet.insert_chart('A22', chart1)
    workbook.close()

make_report()