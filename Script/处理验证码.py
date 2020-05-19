# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:07:47 2019

@author: liuyuntao
"""

import pytesseract
from PIL import Image

image = Image.open(r"C:\Users\liuyuntao\Desktop\exercise\验证码.jpg")
string = pytesseract.image_to_string(image)

print(string)