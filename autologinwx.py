import pyautogui
from PIL import Image
import time

def find_and_click_button(image_path):
    time.sleep(30)   # 等待30秒
    screenshot = pyautogui.screenshot() # 截取屏幕
    button_image = Image.open(image_path)   # 加载目标图片
    position = pyautogui.locate(button_image, screenshot)   # 查找目标图片在屏幕上的位置

    if position is not None:
        center = pyautogui.center(position) # 获取按钮中心点的位置
        pyautogui.click(center) # 点击按钮
        print("登录按钮已点击")
    else:
        print("未找到登录按钮")

if __name__ == "__main__":
    login_button_path = "./login.png"   # 指定登录按钮的图片路径
    find_and_click_button(login_button_path)
