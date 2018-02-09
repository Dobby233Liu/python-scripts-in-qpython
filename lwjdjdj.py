#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import random

def truecode(cal1,cal2,cal3,cal4):
  return (cal3-cal1+8-random.randint(2,cal1))+(cal4+cal2-random.randint(1,cal2))
  
calc_soultion=random.randint(1,255)
add_num=random.randint(1,255)
notify_soultion=calc_soultion-add_num
print("你猜得出1～255范围的随机数吗？")
print("每日数(tí)学(shì)题："+str(notify_soultion)+"+"+str(add_num)+"=?")
#print(calc_soultion)
it=input("请输入...")
#地狱模式代码
if it=='':
 #11
 print("请输入一个数字!!!")
 calc_soultion2=random.randint(8150,998889)
 add_num2=random.randint(1000,977999)
 notify_soultion2=(calc_soultion+55-85)-(add_num2+1)+truecode(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
 print("你猜得出1～255范围的随机数吗？")
 print("每日数(tí)学(shì)题："+str(notify_soultion2-6-random.randint(9,28))+"+"+str(add_num2-8-1)+"=?")
 #print(add_num+888-7+add_num2-6+notify_soultion+5-notify_soultion+15-1+add_num-8-random.randint(1,111))
 input("请输入...")
 print("U RE A IDIOT HAAAAAAAAAA")
 exit()
else:
 gu=int(it)
#地狱模式结束
if gu==calc_soultion:
 print("对了")
else:
 print("错了")
 print("答案：")
 print(calc_soultion)

	
#def usally_never_get(truecode):
#	if truecode==((5-3)+(2+7)): 
#	 print("答案：")
#  print(calc_soultion)


