# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:34:28 2019

@author: USER
"""

a1 = [[1,1,1,0,0,1,0,0,0,1],800]
a2 = [[1,1,0,1,0,0,0,0,1,0],700]
a3 = [[0,0,1,0,1,0,0,1,0,0],1100]
a4 = [[1,1,0,1,1,1,1,0,0,1],550]
a5 = [[1,0,0,1,0,0,0,1,0,0],450]
a6 = [[0,1,0,0,1,0,0,1,0,1],750]
a7 = [[0,0,1,1,1,0,1,1,1,0],610]
a8 = [[0,0,0,1,1,0,0,0,0,1],500]
a9 = [[1,0,0,0,0,1,1,1,0,0],900]
a10 = [[0,0,1,0,1,0,0,0,1,0],850]
a11 = [[1,0,0,0,1,0,0,1,0,0],800]
a12 = [[1,0,0,1,1,0,0,0,1,0],700]

def swap(a):
    #Partial schedule with days d2,d3,d6,d7 fixed
    temp1 = a[0][0]
    a[0][0] = a[0][1]
    a[0][1] = a[0][2]
    a[0][2] = temp1
    
    temp2 = a[0][8]
    temp3 = a[0][9]
    a[0][8] = a[0][5]
    a[0][9] = a[0][6]
    a[0][5] = temp2
    a[0][6] = temp3
    
    return a

def LB1a(a):
    candidate=[]
    for i in range(len(a[0])):
        if a[0][i]==1:
            candidate.append(i)
    
    c = candidate[-1]-candidate[0]-len(candidate)+1
    
    return c*a[1]

def LB1b(a):
    c=0
    if (a[0][0]==1 and a[0][1]==0)or (a[0][-2]==0 and a[0][-1]==1):
        c=1
    return c*a[1]


cost1 = 0
cost1 = LB1a(swap(a1))+ LB1a(swap(a4)) + LB1a(swap(a7))
    
cost2 = 0
cost2 = LB1b(swap(a2))+ LB1b(swap(a3))+ LB1b(swap(a6))+ LB1b(swap(a10))+ LB1b(swap(a9))
    
print('LB1=', cost1+cost2)
    
   