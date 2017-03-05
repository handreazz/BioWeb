#encoding:utf-8
import os
import sys
import random
from os import system
from sys import argv

def install():
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

def remove():
    tmpfile = os.environ["SystemRoot"]+"\\System32\\bioweb_tmp"+str(random.random())
    try:
        open(tmpfile,"w").write("UAC test")
        os.remove(tmpfile)
    except PermissionError:
        print("对不起，本安装程序没有足够的权限呢。。。")
        print("请右键管理员权限运行~")
        system("pause")
        exit(2)
    system(">nul 2>nul bin\\httpd -k stop & bin\\httpd -k uninstall ")
    system("sc delete Apache2.4")
    print("程序已经从系统服务中卸载，你可以手动删除C:\\BioWeb中的内容了")
    system("pause")

def start():
    system(">nul 2>nul bin\\httpd -k start")
    import requests
    try:
        requests.get("http://127.0.0.1")
    except:
        print("唔。。。发生了一个问题，服务启动不起来呢")
        print("下面将尝试重新安装...")
        system("pause")
        return install()
    system("start \"\" http://127.0.0.1")

if __name__ == "__main__":
    if len(argv)==1:
        print("""用法：
安装：python manage.py install
卸载：python manage.py remove
启动：python manage.py start""")
        system("pause>nul")
        exit(0)
    if argv[1]=="install":
        install()
    elif argv[1]=="remove":
        remove()
    elif argv[1]=="start":
        start()