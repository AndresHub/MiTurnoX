import os
root = os.getcwd()
videoroot =rf"{root}\Videos"
var = os.listdir(videoroot)
"""var = os.path.exists('1.mp4')"""
var2 = len(var)
for item in var:
    print(item)