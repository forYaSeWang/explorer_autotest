import os
import zipfile


def zip_directory(directory, zip_name):
    """
    - 根据要压缩的文件目录，压缩名称，生成压缩文件
    :param directory: 需要压缩的目录
    :param zip_name: 压缩后的文件名称
    :return: 压缩后的文件
    """
    # 创建一个 Zip 文件对象
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    # 遍历目录并将文件逐个添加到 Zip 文件对象中
    for root, _, files in os.walk(directory):
        for file in files:
            # 将文件添加到 Zip 文件
            file_path = os.path.join(root, file)
            arc_name = os.path.relpath(file_path, os.path.dirname(directory))
            zipf.write(file_path, arcname=arc_name)

    # 关闭 Zip 文件对象
    zipf.close()


if __name__ == '__main__':
    # 要压缩的目录
    directory_to_zip = '../result'
    # 压缩后的 Zip 文件路径及文件名 - 注意不要搞到result这个目录了，会循环去压缩
    zip_file_name = '../report.zip'

    # 调用函数来压缩目录
    zip_directory(directory_to_zip, zip_file_name)
