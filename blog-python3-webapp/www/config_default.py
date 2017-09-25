#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'libingbin2015@aliyun.com'

'''
    Default configurations.
'''

# 'secret': secret 是必需的选项，这是用于签名会话ID cookie的密钥。这可以是单个密钥的字符串或多个秘密的数组(只有第一个元素将用于签名会话ID cookie)而在验证请求中的签名时，将考虑所有元素
# 另外, 考虑到安全性, 这个密钥是不建议存储在的程序中的. 最好的方法是存储在你的系统环境变量中, 通过 os.getenv(key, default=None) 获得

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'toor',
        'db': 'db'
    },
    'session': {
        'secret': 'libingbin2015@aliyun.com'
    }
}
