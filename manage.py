#encoding:utf-8
import os
import sys
import random
import socket
import requests
from os import system
from sys import argv

flag_UAC=True

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
    global flag_UAC
    tmpfile = os.environ["SystemRoot"]+"\\System32\\bioweb_tmp"+str(random.random())
    try:
        open(tmpfile,"w").write("UAC test")
        os.remove(tmpfile)
        flag_UAC=False
    except PermissionError:
        print("对不起，现在本安装程序没有足够的权限呢。。。")
        print("请关闭本窗口后右键，选择“以管理员身份运行”~")
        e(2)

def uninstall():
    global flag_UAC
    if flag_UAC:
        checkUAC()
    s("bin\\httpd -k stop")
    s("bin\\httpd -k uninstall")

def installapache():
    global flag_UAC
    if flag_UAC:
        checkUAC()
    s("bin\\httpd -k install")
    return s("bin\\httpd -k start")==0

def start_browser():
    s("start \"\" http://127.0.0.1")

def is_80port_listening():  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    try:  
        s.connect(("127.0.0.1",80))  
        s.shutdown(2)  
        return True
    except:  
        return False

def is_server_ok():
    try:
        x=requests.get("http://127.0.0.1/",timeout=1)
        return "Apache" in x.headers.get("Server")
    except:
        return False

def stop_iis():
    global flag_UAC
    if flag_UAC:
        checkUAC()
    s("net stop IISADMIN")
    s("net stop W3SVC")

def stop_nginx():
    global flag_UAC
    if flag_UAC:
        checkUAC()
    s("taskkill /f /im nginx.exe")

def install():
    if is_server_ok():
        start_browser()
    else:
        checkUAC()
        checkdir()
        if is_80port_listening():
            stop_iis()
            stop_nginx()
            if is_80port_listening():
                uninstall()
                if is_80port_listening():
                    print("""您的80端口仍被占用，以下为 netstat -ano|find ":80"|find "LISTENING" 的执行结果：""")
                    system('netstat -ano|find ":80"|find "LISTENING"')
                    print("其中最后一列为进程的PID，您可以手动结束占用80端口的进程后再次运行本安装程序")
                    e(3)
        print("正在搭建服务器，马上就好~")
        if installapache() and is_server_ok():
            start_browser()
        else:
            print("未知原因的安装失败")
            e(3)

    
if __name__ == "__main__":
    if len(argv)==1:
        print("""用法：
安装/启动：python manage.py install
卸载：python manage.py remove""")
        system("pause")
        exit(0)
    if argv[1]=="install":
        install()
    elif argv[1]=="remove":
        uninstall()
        print("Apache服务已经卸载，您可以手动删除C:\BioWeb")
        system("pause")
    elif argv[1]=="start":
        install()