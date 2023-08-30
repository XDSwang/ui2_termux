# ui2_termux
<!-- 搭接环境使用总结 -->
    <!-- 问题解决参好页面： -->
        1.https://testerhome.com/topics/17179
        2.https://github.com/openatx/atx-agent
        3.https://github.com/openatx/android-uiautomator-server/

    <!-- ui2环境 -->
        1.# Since uiautomator2 is still under development, you have to add --pre to install the development version
            pip install --upgrade --pre uiautomator2

            # Or you can install directly from github source
            git clone https://github.com/openatx/uiautomator2
            pip install -e uiautomator2
        2.详细页面：https://gitcode.net/mirrors/openatx/uiautomator2?utm_source=csdn_github_accelerator&from_codechina=yes#screenrecord

 
    <!-- termux环境 -->
        1.zerotermux:+恢复包：过程很麻烦直接使用这些复原初始环境
            zerotermux：目前没有上传
            恢复包：目前没有上传

    <!-- 无线adb问题： -->
        1.要链接wifl-开启分屏/原因开闭机器码页面就会消失和刷新
            
            查看配对码地址+端口
            adb pair 192.168.0.0:xxx
            接着输入配对码
            提示成功后
        2.有权限以后不用再执行第一步
            用connect本地地址+默认端口链接一下
            adb connect 127.0.0.1:42607
        3.会提示链接的
            adb devices
            查看设备