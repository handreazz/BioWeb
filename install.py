import os
import random
from os import system
workdir = os.getcwd().lower()
if workdir != "c:\\bioweb":
    print("程序所在路径不正确，请安装到C:\\BioWeb")
    exit(1)
tmpfile = os.environ["SystemRoot"]+"\\System32\\bioweb_tmp"+str(random.random())
try:
    open(tmpfile,"w").write("UAC test")
    os.remove(tmpfile)
except PermissionError:
    print("对不起，本安装程序没有足够的权限呢。。。")
    print("请右键管理员权限运行~")
    system("pause")
    exit(2)
print("正在搭建服务器，马上就好~")
system(">nul 2>nul bin\\httpd -k stop & bin\\httpd -k uninstall ")
system(">nul 2>nul bin\\httpd -k install & bin\\httpd -k start ")
system("start \"\" http://127.0.0.1")