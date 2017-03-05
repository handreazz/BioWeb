#!C:/BioWeb/python.exe
#coding:utf-8
import cgi

print("Content-type:text/html;charset=utf-8\r\n\r\n")
#保留上几行就对了
form = cgi.FieldStorage()
xing = form.getvalue('xing',"Unknown")
ming =  form.getvalue('ming',"Unknown")

print("Hello~你好呀")
print(xing)
print(ming)