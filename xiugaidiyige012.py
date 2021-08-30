#-*- codeing = utf-8 -*-
#@Time: 2021/8/28 8:19
#@Auther: Jack hou
#@File: xiugaidiyige012.py
#@Software: PyCharm

import os

# path = input("请输入目录 修改目录下所有文本文件每一行的第一个数字")
path = 'C:\\Users\\25659\\OneDrive\\桌面\\15\\labels\\'
# x = input(" 修改为：")
x = "2"
for root, dirs, files in os.walk(path):
    for f in files:
        file = open(os.path.join(root, f), "r")
        fs = file.readlines()
        for i in range(len(fs)):
            #print(i.replace(i[0],x,1))
            fs[i] = fs[i].replace(fs[i][0],x,1)
        for i in fs:
            print(i)
        file.close()
        file_read = open(os.path.join(root, f), "w")
        file_read.writelines(fs)
        file_read.close()