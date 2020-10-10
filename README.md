## NJUPT CHINANET Connector
### 南邮电信网自动连接器
> 2020/10/10: Just have finished the njupt-chinanet connector for pc(both linux and windows)

### How to use
#### windows
- download this project
- open the .py file, and replace the cfg with [] in the code
    ```
        username = '[username]'
        password = '[pwd]'
        openwifi(device='[linux | windows]')
    ```
- then save the change
- then install the required packages
    ```
        pip3 install -r requirement.txt
    ```
- then create an new .txt file in your computer, and enter:
    ```
        python3 /[absolute path to the file]/loginchinanet.py
    ```
- save and quit, and change .txt into .bat
- find the startup folder in your computer, something like this:
    ```
        C:\Users\[username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    ```
- then move the .bat file into this folder, if failed, store it in another foler, then create a shorcut of it, then move the shortcut into the folder above like.
- then restart the pc, you'll see the net is connected automatically.

#### linux
- download this project
- open the .py file, and replace the cfg with [] in the code
    ```
        username = '[username]'
        password = '[pwd]'
        openwifi(device='[linux | windows]')
    ```
- then save the change
- then install the required packages
    ```
        pip3 install -r requirement.txt
    ```
- then create an new .sh file in your computer, and enter:
    ```
        #!/bin/bash
        python3 /[absolute path to the file]/loginchinanet.py
    ```
- move the shell into /etc/init.d
- then add the shell to run-upon-startup
    ```
        update-rc.d [shell name] defaults 
    ```
- then restart the pc, you'll see the net is connected automatically.

 ***
If you find this useful, please star it! :)

Support from you is my greatest encouragement! (您的支持是对我的最大鼓励！)       
Thanks a lot! (谢谢充电！)       
<img src="https://github.com/DenryDu/DenryDu.github.io/blob/master/image_upload/wechat_charge.png" width="100"  alt="wechat_pay"/>
<img src="https://github.com/DenryDu/DenryDu.github.io/blob/master/image_upload/alipay_charge.jpg" width="100"  alt="ali_pay"/><br/>

