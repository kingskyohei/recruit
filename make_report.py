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
    line_chart_mean = workbook.add_chart({'type': 'line'})
    line_chart_median = workbook.add_chart({'type': 'line'})
    bar_chart = workbook.add_chart({'type': 'column'})
    # chart1 = workbook.add_chart({'type': 'column'})
    file = pd.read_csv('D:/Users/01016964/Desktop/内定者分析関連/顔ぶれ分析/レオパレス加工/レオパレス21対応/python_output/PRE_ENTRY.csv')

    # ヘッダー行
    names = file.columns.values

    # header行の書き込み
    header_format.set_bg_color('#8fbc8f')
    worksheet.write_row('A1', names,header_format)

    # 明細行の設定

    # 明細行の書き込み
    for i, ni in enumerate(names):
        worksheet.write_column('A2', file['YM'],string)
        worksheet.write_column('B2', file['m_mean_dif'],decimal)
        worksheet.write_column('C2', file['m_median_dif'],decimal)
        worksheet.write_column('D2', file['t_mean_dif'],decimal)
        worksheet.write_column('E2', file['m_median_dif'],decimal)
        worksheet.write_column('F2', file['SUM_PRE_ENTRY_KAISU_m'],integer)
        worksheet.write_column('G2', file['SUM_PRE_ENTRY_KAISU_t'],integer)
        # worksheet.write_column('A2', file['YM'], string)
        # worksheet.write_column('B2', file['ENTRY_M_MEAN'], decimal)
        # worksheet.write_column('C2', file['ENTRY_M_MEDIAN'], decimal)
        # worksheet.write_column('D2', file['ENTRY_T_MEAN'], decimal)
        # worksheet.write_column('E2', file['ENTRY_T_MEDIAN'], decimal)
        # worksheet.write_column('F2', file['ENTRY_M_COUNT'], integer)
        # worksheet.write_column('G2', file['ENTRY_T_COUNT'], integer)

    # 表の装飾
    #グラフの表示
    # 線グラフの描画
    # 平均値

    line_chart_mean.add_series({'values': '=Sheet1!$B$2:$B$8','name': '=Sheet1!$B$1','marker': {'type': 'automatic'},})
    line_chart_mean.add_series({'values': '=Sheet1!$D$2:$D$8','name': '=Sheet1!$D$1','categories': '=Sheet1!$A$2:$A$8','marker': {'type': 'automatic'}})

    # 中央値
    line_chart_median.add_series({'values': '=Sheet1!$C$2:$C$8','name': '=Sheet1!$C$1','marker': {'type': 'automatic'}})
    line_chart_median.add_series({'values': '=Sheet1!$E$2:$E$8','name': '=Sheet1!$E$1','marker': {'type': 'automatic'},'categories': '=Sheet1!$A$2:$A$8'})

    # 棒グラフの描画
    bar_chart.add_series({'values': '=Sheet1!$F$2:$F$8','name': '=Sheet1!$F$1'})
    bar_chart.add_series({'values': '=Sheet1!$G$2:$G$8','categories': '=Sheet1!$A$2:$A$8','name':'=Sheet1!$G$1'})

    # 棒グラフ/平均値の装飾
    # グラフサイズの設定
    bar_chart.set_size({'width': 400, 'height': 320})
    # グラフタイトルの設定
    bar_chart.set_title({'name': 'エントリーユーザー数','name_font': {'size': 12, 'メイリオ': True}})

    # X軸の設定
    bar_chart.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
        'date_axis': True,
        'minor_unit': 7,
        'minor_unit_type': 'months',
    })
    # Y軸の設定
    bar_chart.set_y_axis({'visible': True})

    # 棒グラフ/中央値
    # グラフサイズの設定
    line_chart_mean.set_size({'width': 400, 'height': 320})
    line_chart_median.set_size({'width': 400, 'height': 320})

    # グラフタイトルの設定
    line_chart_mean.set_title({'name': 'エントリー回数/平均値','name_font': {'size': 12, 'メイリオ': True}})

    line_chart_median.set_title({'name': 'エントリー回数/中央値','name_font': {'size': 12, 'メイリオ': True}})

    # X軸の設定
    line_chart_mean.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    line_chart_median.set_x_axis({
        'name_font': {'size': 12,'メイリオ': True},
        'num_font': {'メイリオ': True },
    })

    # 凡例の設定
    # 棒グラフの凡例
    bar_chart.set_legend({'position': 'bottom'})

    # 線グラフの凡例
    line_chart_mean.set_legend({'position': 'bottom'})
    line_chart_median.set_legend({'position': 'bottom'})

    # chart1.add_series({'values': '=Sheet1!$A$1:$A$5'})
    # chart1.add_series({'values': '=Sheet1!$B$1:$B$5'})
    # chart1.add_series({'values': '=Sheet1!$C$1:$C$5'})
    # Insert the chart into the worksheet.
    worksheet.insert_chart('I10', bar_chart)
    worksheet.insert_chart('A10', line_chart_mean)
    worksheet.insert_chart('A27', line_chart_median)
    # worksheet.insert_chart('A22', chart1)
    workbook.close()