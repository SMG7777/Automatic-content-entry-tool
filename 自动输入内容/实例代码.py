import pynput
import time
import easygui as eg

mouse = pynput.mouse.Controller() #创建虚拟鼠标
keyboard = pynput.keyboard.Controller() #创建虚拟键盘

cs = int(eg.enterbox("请输入你要输入的次数：(不能是负数）"))
text = eg.enterbox("请输入你要输入的内容：")
sleep = float(eg.enterbox("请输入你要每次输入之间间隔时间："))

eg.msgbox("请关闭此窗口，然后开始倒计时5秒,现在请将鼠标方式你要输入框上")
time.sleep(5)
for i in range(cs):
    keyboard.type(text)
    keyboard.press(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.enter)
    time.sleep(sleep)

eg.msgbox("输入完毕，请关闭此窗口退出程序")
