import os
import random
import sys
import socket
import requests
from os import system

def s(command,ignore=True):
    prefix=">nul 2>nul " if ignore else ""
    return system(prefix+command)


def e(ret=1):
    print("\n程序无法继续运行，按任意键退出...")
    s("pause")
    exit(ret)

def checkdir():
    workdir = os.getcwd().lower()
    if workdir != "c:\\bioweb":
        print("程序所在路径不正确，请安装到C:\\BioWeb")
        e(1)

def checkUAC():
    tmpfile = os.environ["SystemRoot"]+"\\System32\\bioweb_tmp"+str(random.random())
    try:
        open(tmpfile,"w").write("UAC test")
        os.remove(tmpfile)
    except PermissionError:
        print("对不起，现在本安装程序没有足够的权限呢。。。")
        print("请关闭本窗口后右键，选择“以管理员身份运行”~")
        system("pause")
        e(2)
    print("正在搭建服务器，马上就好~")

def uninstall():
    s("bin\\httpd -k stop")
    s("bin\\httpd -k uninstall")

def install():
    s("bin\\httpd -k install")
    return s("bin\\httpd -k start")==0

def start_browser():
    s("start \"\" http://127.0.0.1")

def is_port_open():  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    try:  
        s.connect(("0.0.0.0",80))  
        s.shutdown(2)  
        return True  
    except:  
        return False  

def is_server_ok():
    x=requests.get("http://127.0.0.1/",timeout=1)
    return "Apache" in x.headers.get("Server")

def stop_iis():
    s("net stop IISADMIN")
    s("net stop W3SVC")

if __name__ == "__main__":
    if is_server_ok():
        start_browser()
    else:
        checkUAC()
        checkdir()
        if is_port_open():
            stop_iis()
            uninstall()
        if install():
            start_browser()
        else:
            print("未知原因的安装失败")
            e(3)