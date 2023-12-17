import subprocess
import os
from PIL import Image, ImageDraw, ImageFont



def run_makefile_cpp_program(directory):
    # 切换到包含Makefile的目录
    os.chdir(directory)
    print("starting data processing")
    # 使用'make'命令编译程序
    subprocess.run(['make'], check=True)

    # 执行生成的程序
    subprocess.run(['./my_program'], check=True)


def run_python_script(script_path):
    print("starting image processing")
    subprocess.call(["python", script_path])
    print("done")

# 使用你的Python脚本路径替换"your_script.py"



# 获取当前工作目录
current_directory = os.getcwd()

run_makefile_cpp_program('.\\process\\PROCESS\\data_process')



os.chdir(current_directory)
run_python_script(".\\image.py")

# 打开图片
img = Image.open('.\\marked_image1.png')


# 创建一个可以在给定图像上绘图的对象
draw = ImageDraw.Draw(img)

# 设置字体和大小
font = ImageFont.truetype('simhei.ttf', 15)

text = open(".\\process\\PROCESS\\data\\output.txt","r",encoding='utf-8')

text_content = text.read()

# 在图片上添加文字
draw.text((10, 10), text_content, font=font, fill='white')
img.show()
print("show image")
# 保存图片
img.save('image_with_text.png')
