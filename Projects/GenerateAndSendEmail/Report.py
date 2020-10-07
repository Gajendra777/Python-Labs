#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import HorizontalBarChart
import locale
import math


def generate(filename,title,additional_info,table_data):


    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                    ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
                    ('ALIGN',(0,0),(-1,-1),'CENTER') ]
    report_table = Table(data= table_data, style= table_style, hAlign="LEFT")
    empty_line = Spacer(1,20)

    #Generate Pie Chart
    report_pie = Pie()
    report_pie.width = 300
    report_pie.height = 150
    report_pie.data = []
    report_pie.labels = []
    for car_list in table_data[1:]:
        report_pie.data.append(car_list[3])
        report_pie.labels.append(car_list[1])

    #Generate Bar Chart
    car_Revenue_list = [[item[1],locale.atof(item[2].strip("$"))*item[3]] for item in table_data[1:]]
    Sorted_Table_Data = sorted(car_Revenue_list,key=lambda x: x[1])



    bar = HorizontalBarChart()
    bar.width = 500
    bar.height = 150
    bar_data = []
    bar_category = []

    for item in Sorted_Table_Data[:-11:-1]:
        bar_category.append(item[0])
        bar_data.append(math.trunc(item[1]))

    bar.strokeColor = colors.black
    bar.valueAxis.valueMin = 0
    bar.valueAxis.valueStep = 2000000

    bar.data = [bar_data]
    bar.categoryAxis.categoryNames = bar_category


    report_chart = Drawing()
    report_chart.add(report_pie)

    report_bar_chart = Drawing()
    report_bar_chart.add(bar)

    report.build([report_title,empty_line,report_info,empty_line,report_table,empty_line,report_chart,empty_line,report_bar_chart])
