# -*- coding: utf-8 -*-
import os
import time

import pytest
from loguru import logger

from lib.send_email import Email

# logger.add("logs/case_{time}.log", rotation="500MB")
from lib.zip_directory import zip_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULT_DIR = os.path.join(BASE_DIR, f'results/{time.strftime("%Y%m%d-%H%M%S")}')


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} Execution time {(end_time - start_time) / 60} min")
        return result

    return wrapper


@timer
def run_tests():
    if not os.path.isdir("result"):
        os.mkdir("result")

    if not os.path.isdir("result_zip"):
        os.mkdir("result_zip")

    pytest.main(['-sv', "application/explorer", '--html=result/report.html'])

    # 调用函数来压缩目录
    zip_directory("./result", "./result_zip/report.zip")
    body = f'ME浏览器页面元素检查程序运行完成，运行结果详情见附件！运行时间：{time.strftime("%Y-%m-%d %H:%M:%S")}'
    Email().send_test_report(body, './result_zip/report.zip')


if __name__ == '__main__':
    run_tests()
