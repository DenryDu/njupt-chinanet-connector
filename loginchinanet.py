#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import io
import os
import sys
import time
import netifaces
import platform

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
 
def openwifi():
    device = platform.system();
    if device=='windows':
        try:
            os.system('netsh wlan connect name=NJUPT-CHINANET')
        except Exception:
            pass
    else:
        try:
            all_nc = netifaces.interfaces();
            nc = list(set(all_nc)-set(['lo']));
            nc = nc[0];
            os.system("sudo rfkill unblock wifi" )
            os.system("sudo ifconfig "+ nc +" up" )
            os.system("sudo gsettings set org.gnome.system.proxy mode auto")
            os.system("sudo iw dev "+ nc +" connect NJUPT-CHINANET")
#            os.system("gsettings set org.gnome.system.proxy mode auto")
        except Exception:
            pass
    time.sleep(1)
     
def killtask():
    try:
        os.system('TASKKILL /F /IM chrome.exe ')
    except Exception:
        pass
 
def login(username,password):
    url = 'http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=p.njupt.edu.cn&iTermType=1&wlanacname=XL-BRAS-SR8806-X&mac=00-00-00-00-00-00&enAdvert=0&queryACIP=0&loginMethod=1'
    body = {
            "DDDDD": ",0,"+username+"@njxy",
            "upass": password,
            "R1": "0",
            "R2": "0",
            "R3": "0",
            "R6": "0",
            "para": "00",
            "0MKKey": "123456",
            "buttonClicked": "",
            "redirect_url": "",
            "err_flag": "",
            "username": "",
            "password": "",
            "user": "",
            "cmd": "",
            "Login": "",
            "v6ip": ""
          }
    headers = {        
              "c": "ACSetting",
              "a": "Login",
              "protocol": "http:",
              "hostname": "p.njupt.edu.cn",
              "iTermType": "1",
              "wlanuserip": "10.165.217.76",
              "wlanacip": "10.255.252.150",
              "wlanacname": "XL-BRAS-SR8806-X",
              "mac": "00-00-00-00-00-00",
              "ip": "10.165.217.76",
              "enAdvert": "0",
              "queryACIP": "0",
              "loginMethod": "1"
            }
    try:
        response = requests.post(url, data = body)
    except Exception:
        pass 
    else:
        # 返回信息
        print(body)
        # 返回响应头
        print(response.status_code)
        # 判断是否成功
        if response.text.__contains__('认证成功') or response.text.__contains__('信息页'):
            print('connect success')
        else:
            print('connect failed')

def main():
    
    # replace [username] with your username
    username = '[username]'
    # replace [pwd] with your pwd
    password = '[password]'
    openwifi()
    login(username,password)
    killtask()
    try:
        os._exit()
    except Exception:
        pass

main()



