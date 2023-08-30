import uiautomator2 as u2
import time
d = u2.connect("127.0.0.1")

print(d.info)

# d.uiautomator.stop()
# 测试在安卓13中如果不用会被杀掉
a=d.uiautomator.running()
print(a)
if not a: # 是否在运行
    d.uiautomator.start()# 启动
    time.sleep(1)

# time.sleep(2)
# 测试代码
d.click(680,2200)
time.sleep(1)
d.swipe(500,0,500,1000)
d.screenshot("1.png")






# 测试代码 目前正常