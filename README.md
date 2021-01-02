## NJUPT CHINANET Connector
### 南邮电信网自动连接器
![](https://img.shields.io/badge/language-python-green.svg)  ![](https://img.shields.io/badge/NJUPT_CHINANET_Connector-v1.0.1-519dd9.svg)

A tool to automatically connect to NJUPT CHINANET      
> 南邮电信wifi自动连接器（可以设置为解锁自启动项）
## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background
## Install

## Usage
#### windows
- download this project
- open the .py file, and replace the cfg with [] in the code
    ```
        username = '[username]'
        password = '[pwd]'
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
## Related Efforts
## Maintainer
[@DenryDu](https://github.com/DenryDu)
## Contributing
> 2020/10/10: Just have finished the njupt-chinanet connector for pc(both linux and windows)                      
> 2020/10/11: Fix the problem of cannot set proxy to 'auto' on linux
### Contributor
[@DenryDu](https://github.com/DenryDu)
## License
 ***
If you find this useful, please star it, PLEASE! :)

