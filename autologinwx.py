
'''
    作者：imoki
    仓库：https://github.com/imoki
    更新时间：2024年10月15日
    脚本功能：修改微信版本号，自动登录微信，并运行微信消息监控程序
'''
import pyautogui
from PIL import Image
import time
import subprocess

login_button_path = "F:\\login.png"   # “进入微信”按钮的图片路径
login2_button_path = "F:\\login2.png"   # “登录”按钮的图片路径
another_script_path = "F:\\start.py"   # 运行微信消息监控程序
changeVersionPath = "F:\\changeWxVersion.py"   # 切换微信版本

def switch_window(num_times=1):
    """
    切换窗口 num_times 次。
    :param num_times: 切换次数，默认为1次
    """
    pyautogui.keyDown('alt')
    for _ in range(num_times):
        pyautogui.press('tab')
        time.sleep(0.1)  # 短暂延迟，确保切换成功
    pyautogui.keyUp('alt')
    
# 点击登录按钮
def find_and_click_button():
    time.sleep(80)   # 等待80秒
    run_another_script(changeVersionPath)    # 切换微信版本
    time.sleep(10)   # 等待10秒
    
    button_image = Image.open(login_button_path)   # 加载目标图片
    button_image2 = Image.open(login2_button_path)   # 加载目标图片

    flag = 0
    position = 0
    count = 0
    for _ in range(5):
        screenshot = pyautogui.screenshot() # 截取屏幕
        count += 1
        try:
            # position = pyautogui.locateOnScreen(button_image, grayscale=True, confidence=0.7)
            position = pyautogui.locate(button_image2, screenshot)
            if position is not None:
                print("找到了图像")
                flag = 1
                break
            else:
                print("未找到图像，再次尝试...")
                switch_window(count)
                time.sleep(1)
        except pyautogui.ImageNotFoundException as e:
            switch_window(count)
            print(f"未能找到图像 {e}")
    
    if flag == 0:   
        screenshot = pyautogui.screenshot() # 截取屏幕
        for _ in range(5):
            count += 1
            try:
                # position = pyautogui.locateOnScreen(button_image, grayscale=True, confidence=0.7)
                position = pyautogui.locate(button_image, screenshot)
                if position is not None:
                    print("找到了图像")
                    flag = 1
                    break
                else:
                    print("未找到图像，再次尝试...")
                    switch_window(count)
                    time.sleep(1)
            except pyautogui.ImageNotFoundException as e:
                switch_window(count)
                print(f"未能找到图像 {e}")
                
    
    center = pyautogui.center(position) # 获取按钮中心点的位置
    pyautogui.click(center) # 点击按钮
    print("登录按钮已点击")

    time.sleep(30)   # 等待30秒
    print("运行另一个脚本")
    run_another_script(another_script_path) # 消息监控程序

# 运行其他脚本
def run_another_script(script_path):
    try:
        # 调用另一个Python脚本
        subprocess.run(["python", script_path], check=True)
        print("脚本执行成功")
    except subprocess.CalledProcessError as e:
        print(f"脚本执行失败：{e}")
    except FileNotFoundError:
        print(f"文件未找到：{script_path}")
    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    find_and_click_button()
