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
    report_path = f'result/{time.strftime("%Y%m%d-%H%M%S")}'
    pytest.main(['-vs', '-m', "application/explorer", f'--html={report_path}/report.html'])

    # 调用函数来压缩目录
    report_path = os.path.join(BASE_DIR, report_path)
    zip_directory(report_path, f"{report_path}/report.zip")
    Email().send_test_report("测试成功", f'{report_path}/report.zip')


if __name__ == '__main__':
    run_tests()
