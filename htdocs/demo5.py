#!C:/BioWeb/python.exe
#coding:utf-8
from EasyLogin import EasyLogin
print("Content-type:text/html;charset=utf-8\r\n\r\n")#这一步必须写好，请一定保留这一行

a=EasyLogin()
a.get("http://m.weather.com.cn/mweather/101210101.shtml")
mingtian = a.b.find("b",text="明天")
weather1 = mingtian.find_next("img")["alt"]
weather2 = mingtian.find_next("img").find_next("img")["alt"]
temperature = mingtian.find_next("span").text

print("杭州明日天气：{}~{} {}<br>".format(weather1,weather2,temperature))

print("""<a href=# onclick="window.history.go(-1)">返回</a> """)