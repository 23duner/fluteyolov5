import os
import shutil


def generate_labels(image_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg"):  # 确保处理的是JPG文件
            # 创建同名的TXT文件
            txt_filename = filename.replace(".jpg", ".txt")
            txt_path = os.path.join(output_folder, txt_filename)

            # 写入内容到TXT文件
            with open(txt_path, 'w') as f:
                f.write("0 0.25 0.5 0.5 0.9"
                        "0 0.75 0.5 0.5 0.9")  # 按照给定的标注格式写入内容

            print(f"Label file created for {filename}")

def generate_labels1(image_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历文件夹中的所有文件夹
    for folder_name in os.listdir(image_folder):
        folder_path = os.path.join(image_folder, folder_name)
        if os.path.isdir(folder_path):
            # 遍历文件夹中的所有文件
            for filename in os.listdir(folder_path):
                if filename.endswith(".jpg"):  # 确保处理的是JPG文件
                    # 创建同名的TXT文件
                    txt_filename = filename.replace(".jpg", ".txt")
                    txt_path = os.path.join(output_folder, txt_filename)

                    # 写入内容到TXT文件
                    with open(txt_path, 'w') as f:
                        f.write("3 0.23 0.5 0.4 0.9\n3 0.78 0.5 0.4 0.9")  # 按照给定的标注格式写入内容
                    print(f"Label file created for {filename}")
def copy_contents(src_folder, dest_folder):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹中的所有文件和文件夹
    for item in os.listdir(src_folder):
        src_path = os.path.join(src_folder, item)
        dest_path = os.path.join(dest_folder, item)

        # 如果是文件，则复制文件
        if os.path.isfile(src_path):
            dest_path = os.path.join(dest_folder, item)
            shutil.copy2(src_path, dest_path)
        elif os.path.isdir(src_path):
            # 如果是文件夹，则遍历文件夹并复制其中的文件
            for sub_item in os.listdir(src_path):
                sub_src_path = os.path.join(src_path, sub_item)
                if os.path.isfile(sub_src_path):
                    dest_path = os.path.join(dest_folder, sub_item)
                    shutil.copy2(sub_src_path, dest_path)

# 使用示例
# image_folder = 'F:/cccc/flutestudy/mydata/datas/train/newxi'  # 替换为你的图片文件夹路径
# output_folder = 'F:\cccc/flutestudy\yolo/flutedata\labels'  # 替换为你希望存放输出文件的路径
# copy_folder = 'F:\cccc/flutestudy\yolo/flutedata\images'  # 替换为目标文件夹路径

image_folder = 'F:\cccc/flutestudy\errordata\手指靠外'  # 替换为你的图片文件夹路径
output_folder = 'F:\cccc/flutestudy\yolo/errordata\labels'  # 替换为你希望存放输出文件的路径
copy_folder = 'F:\cccc/flutestudy\yolo\errordata\images'  # 替换为目标文件夹路径
generate_labels1(image_folder, output_folder)
copy_contents(image_folder, copy_folder)