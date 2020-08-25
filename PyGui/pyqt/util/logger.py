#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author :        NIEJUN 
# Datetime：      2020/8/25 20:23
# IDE:            PyCharm
# File Name：     logger.py
# DESCRIP：
import logging
import logging.config


def console_logging(log_level=logging.INFO):
    console_handler = logging.StreamHandler()
    logging.basicConfig(level=log_level,format='%(asctime)s - %(name)s - %(levelname)s -----> %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S', handlers=[console_handler])
    return logging.getLogger()


if __name__ == '__main__':
    logger = console_logging(logging.DEBUG)
    logger.debug('debug 信息')
    logger.info('info 信息')
    logger.warning('warn 信息')
    logger.error('error 信息')
    logger.critical('critical 信息')


