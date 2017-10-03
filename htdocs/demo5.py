#!C:/BioWeb/python.exe
# coding: utf-8
from EasyLogin import EasyLogin
print("Content-type:text/html;charset=utf-8\r\n\r\n")#这一步必须写好，请一定保留这一行

import requests
page = requests.get("http://tianqi.2345.com/t/7day_tq_js/58457.js").text
data = page.split("day2:[")[1].split("]")[0].split(",")
# data应该是一个数组，表示明天的天气数据，如：['"18～23℃"', '"三"', '"阴"', '"东北风"', '"28"', '"10月04日"']
# 有多余的引号怎么办呢，交给你处理啦

print("杭州明日({tomorrow_date})天气：{tomorrow_weather} {tomorrow_temperature}<br>".format(tomorrow_date=data[5], tomorrow_weather=data[2], tomorrow_temperature=data[0]))

print("""<a href=# onclick="window.history.go(-1)">返回</a> """)