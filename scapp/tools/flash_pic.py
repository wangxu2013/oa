# coding:utf-8
from flask import make_response
import base64

import openFlashChart
from openFlashChart_varieties import Bar_3d,Line,Pie
from openFlashChart_varieties import bar_3d_value,dot_value,x_axis_labels,x_axis_label,pie_value

colorArr = ['#66b032','#d0ea2b','#fefe33','#fabc02','#fb9902',
			'#fd5308','#fe2712','#a7194b','#8601af','#3d01a4',
			'#4b4bfc','#0247fe']

#导出flash图片(base64格式)
class flash_pic():
	def bar_3d(self,search_result,y_legend,column_text,org,time):
		#定义chart
		chart = openFlashChart.template(u''+time+'年'+org+'公司费用统计柱状图')
		chart.set_y_legend(y_legend, style = '{font-size: 12px}')#设置y轴
		#横坐标
		x_labels = []
		for row in search_result:
			x_labels.append(row[0])
		chart.set_x_axis(colour = '#736AFF', three_d = 5, labels = x_axis_labels(labels = x_labels))

		row_num = len(search_result)#共多少条记录
		column_num = len(search_result[0])#每条记录有几列
		#取值
		mymax = 0
		
		for column_i in range(1,column_num):
			plot = Bar_3d()
			values = []
			for row in search_result:
				if int(row[column_i]) > mymax:
					mymax = int(row[column_i])
				values.append(bar_3d_value(int(row[column_i]), colorArr[column_i-1]))
			plot.set_values(values=values)
			plot.set_colour(colorArr[column_i-1])
			plot['on-show'] = dict([['type','pop-up'],['cascade',1],['delay',0.5]])#api中没有on-show 手动加上
			plot['text'] = column_text[column_i-1]
			chart.add_element(plot)
			values = []
		chart.set_y_axis(min = 0, max = mymax)
		return chart.encode()

	def line_hollow(self,search_result,y_legend,line_text):
		#定义chart
		chart = openFlashChart.template(u'折线图')
		chart.set_y_legend(y_legend, style = '{font-size: 12px}')#设置y轴
		#横坐标
		x_labels = []
		for row in search_result:
			x_labels.append(row[0])
		chart.set_x_axis(colour = '#736AFF', three_d = 5, labels = x_axis_labels(labels = x_labels))

		row_num = len(search_result)#共多少条记录
		column_num = len(search_result[0])#每条记录有几列
		#取值
		mymax = 0
		
		for column_i in range(1,column_num):
			plot = Line()
			values = []
			for row in search_result:
				if int(row[column_i]) > mymax:
					mymax = int(row[column_i])
				values.append(int(row[column_i]))
			plot.set_values(values=values)
			plot.set_colour(colorArr[column_i-1])
			plot['on-show'] = dict([['type','shrink-in'],['cascade',1],['delay',0.5]])#api中没有on-show 手动加上
			plot['dot-style'] = dict([['type','star'],['colour','#a44a80'],['dot-size',5]])#api中没有dot-style 手动加上
			plot['text'] = line_text[column_i-1]
			chart.add_element(plot)
			values = []
		chart.set_y_axis(min = 0, max = mymax)
		return chart.encode()

	def pie(self,search_result,title):
		plot = Pie(start_angle = 35, animate = True,  label_colour = '#432BAF')
		values = []
		colours = []
		count = 0
		for row in search_result:
			count+=1
			values.append(pie_value(int(row[1]),(row[0],None,None)))
			colours.append(colorArr[count/len(colorArr)])
		if not search_result:
			values.append(pie_value(1,("None",None,None)))
			colours.append(colorArr[count/len(colorArr)])
		plot.set_values(values=values)
		plot.colours = colours
		plot.set_tooltip('#val# of #total#<br>#percent# of 100%')
		plot.set_gradient_fill(True)
		plot.set_on_click('plot1')
		plot.set_no_labels(False)

		chart = openFlashChart.template(u''+title+'')
		chart.add_element(plot)

		return chart.encode()

	def export(self, imageData,filename):
		imgData = base64.b64decode(imageData)
		#return send_file(io.BytesIO(imgData))
		response = make_response(imgData)
		response.headers['Content-Type'] = 'image/jpeg'
		response.headers['Content-Disposition'] = 'attachment; filename='+filename+'.jpg'
		return response