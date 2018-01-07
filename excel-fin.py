#coding=utf-8

import os

f1=open("expression.sh","w")

for root,dirs,files in os.walk("./"):
    for file in files:
        if("csv" in file):
            string1='",",'
            f1.write("awk -F ',' '{print $1,"+string1+"$3}' ")
            f1.write(file)
            f1.write(" |")
            string2='"Gene"'
            string3='"Expr Level (Z-Score)"'
            f1.write("awk -F ',' '{print $1,"+string1+"$2}' |sort -n -k1 |awk -F ',' '")
            f1.write("{print $1,$2}' |sed /^[[:space:]]*$/d ")
            f1.write("|awk -F ' ' 'BEGIN{print ")
            f1.write(string2+","+string1+string3)
            f1.write("} {print $1,"+string1+"$2}' ")
            f1.write(">/home/weiss/Desktop/expression1/")
            f1.write(file)
            f1.write('\n')

f1.close()
