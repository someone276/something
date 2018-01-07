#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      李
#
# Created:     21/12/2017
# Copyright:   (c) 李 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re

def length(filename):
    #测量文件内基因长度

    #打开指定文件，将其转换成去掉换行键的字符串
    with open(filename) as file_object:
        lines=file_object.readlines()
    file_string=''
    for line in lines:
        file_string+=line.strip()

    string=''
    for i in file_string:
        if(i=='A' or i=='C' or i=='G' or i=='T' or i=='N'):
            string+=i
        else:
            pass

    #输出字符串长度
    return len(string)


#主函数部分，通过txt文档中储存的文件名输出对应长度
with open('filename.txt') as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.strip()+' : '+str(length(line.strip())))
