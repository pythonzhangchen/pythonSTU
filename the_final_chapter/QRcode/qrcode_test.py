# -*- coding: utf-8 -*-
# @Time : 2022/4/27 16:21 
# @Author : chen.zhang 
# @File : qrcode.py
# https://pypi.org/project/qrcode/5.1/
import qrcode
# 简易方法
# img = qrcode.make('www.baidu.com')
# img.save('qrs/abc.png')

# 精确设置方法
qr = qrcode.QRCode(
    version=5, # 密度
    error_correction=qrcode.constants.ERROR_CORRECT_H,      # ERROR_CORRECT_H，ERROR_CORRECT_高容错率
    box_size=20,    # 整个大小
    border=1,       # 边界
)
qr.add_data('www.baidu.com')
qr.make(fit=True)

img = qr.make_image()
img.save('qrs/1.png')