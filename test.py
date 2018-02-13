#/usr/bin/env python
# -*- coding: UTF-8 -*-

def NumEqual(num1,num2):
    if(num1>num2):
        print("%d is too small!" % num2)
        return False
    elif(num1<num2):
        print("%d is too big!" % num2)
        return False
    if(num1==num2):
        print("%d BINGO!" % num2)
        return True

from random import randint

Fdata = open("GameData.txt")
try:
    BestSocre = int(Fdata.read())
except:
    BestSocre = 0
print("your best Socre is %d let's try again!" % BestSocre)
Fdata.close()
num = randint(1,100)
testNum = 0
Chk = False
Game_Times = 1;
print ("Guess what I think?")
testNum = int(input("the number is:"))
while not Chk:
    Chk = NumEqual(num,testNum)
    if(not Chk):
        print ("Guess Again!")
        testNum = int(input("the number is:"))
        Game_Times += 1
if(Game_Times < BestSocre or BestSocre == 0):
    print("New reword! %d" %Game_Times)
    FWrite = open("GameData.txt",'w')
    FWrite.write(str(Game_Times))
    FWrite.close()
else:
    print("your socre %d" % BestSocre)