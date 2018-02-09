#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import random
print("-------------")
print(" R A N D O M ")
print("-------------")
min1=input("输入最小数 ")

if min1=="this":
 import this
 exit()
 
if min1=="null":
 print("结果 "+str(random.random()))
 exit()

max2=input("输入最大数 ")

if max2=="this":
 import this
 exit()
 
if max2=="null":
 print("结果 "+str(random.random()))
 exit()

ranmd= random.randint(int(min1),int(max2))
rand="结果"+str(ranmd)
print(rand)