# coding=utf-8

import os
from PIL import Image

# 源文件夹
source_dir = "./source/"

# 目标文件夹
target_dir = "./target/"

# 一寸照片
size = (295, 413)


# 文件夹不存在时，创建
def mk_save_dir(path):
    if not os.path.exists(path):
        # 不存在则创建
        os.mkdir(path)
    else:
        # 存在时，清空文件夹
        rm_files = 'rm -rf ' + path + '/*'
        res = os.system(rm_files)
        if res == 0:
            print("清空文件夹" + path + "成功")
        pass


def convert_image(source_path, target_path):
    file_names = os.listdir(source_path)
    for file_name in file_names:
        # 获取规范的路径
        domain = os.path.abspath(source_path)
        # 带路径的文件名
        file_name = os.path.join(domain, file_name)
        # 如果是文件夹进入递归
        if os.path.isdir(file_name):
            child_source_dir = target_path + file_name.split('/')[-1]
            # 子文件夹，在目标文件夹里新建一个
            mk_save_dir(child_source_dir)
            # 递归
            convert_image(file_name, child_source_dir + '/')
            continue
        # 非图片，跳过
        if not file_name.lower().endswith(
                ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            continue
        source_image = Image.open(file_name)
        save_path = target_path + file_name.split('/')[-1]
        # 保存修改尺寸后的图片，ANTIALIAS 去锯齿
        source_image.resize(size, Image.ANTIALIAS).convert('RGB').save(save_path)


if __name__ == '__main__':
    # 清除MacOS生成的.DS_Store文件
    os.system("find " + source_dir + " -name '*.DS_Store' -type f -delete")
    # 创建目标主文件夹
    mk_save_dir(target_dir)
    convert_image(source_dir, target_dir)
    print("完成转换！")
