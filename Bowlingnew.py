# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:55:23 2019

@author: Abhilash
"""


import numpy as np

Enterdata = dict()

for i in range(10):
    
    data = int(input("Enter the first chance for trail"+str(i)))
    if data == 10:
        
        data1 = 0    
        a = [data,data1]
    else:
        data1 = int(input("Enter the second chance for trail"+str(i)))
        a = [data,data1]
    if (i==9 and data ==10) :
        data1 = int(input("Enter the second chance for trail "+str(i)))
        data2 = int(input("Enter the third chance for trail " +str(i)))
        a = [data,data1,data2]
    elif(i==9 and data+data1 ==10):
        data2 = int(input("Enter the third chance for trail "+str(i)))
        
        a = [data,data1,data2]
    Enterdata[i] = a        

sumall = 0
for j in range(len(Enterdata)):

    if (j==9):
        a = Enterdata[j]
        sumall = sumall+np.sum(a)    
        print("The total sum is",sum)
        break    
    if(Enterdata[j][0] == 10):
        if(Enterdata[j+1][1]==0):
            if (j!=8):
            
                sumall = sumall +Enterdata[j][0]+ Enterdata[j+1][0] +  Enterdata[j+2][0]
            else:
                sumall = sumall +Enterdata[j][0]+ (Enterdata[j+1][0] +  Enterdata[j+1][1])
        else:
            sumall = sumall +Enterdata[j][0]+ (Enterdata[j+1][0] +  Enterdata[j+1][1])    
    else:
        if(Enterdata[j][0]+Enterdata[j][1] == 10):
            sumall = sumall + Enterdata[j][0]+(Enterdata[j][1] + Enterdata[j+1][0])
        else:
            sumall = sumall+Enterdata[j][0]+Enterdata[j][1]
    print(sumall)