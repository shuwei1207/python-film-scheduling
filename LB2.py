# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:02:02 2019

@author: LO
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

#算有a沒b的天數和沒a有b2的天數
def LB2d(a,b):
    count = 1
    L1 = []
    L2 = []
    
    #Partial schedule with days d2,d3,d6,d7 fixed
    for i in range(len(a[0])):
        if(i == 1 or i == 2 or i == 5 or i == 6):
            count += 1
            continue
        
        if(a[0][i] != b[0][i]):
            if(a[0][i] == 1):
                L1.append(count)
            else:
                L2.append(count)
        count += 1
    return L1, L2


#求出a,b中成本較低的
def minimum(a,b,c):
    return min(len(c[1])*a[1],len(c[0])*b[1])

A = [a2,a3,a6,a10]
#A = [a9]

#max-matching
def LB2c(A):
    L3 = []
    L4 = []
    L5 = []
    for i in range(len(A)):
        for j in range(1,len(A)-i):            
            if(A[i+j]!= None):
                L3.append(LB2d(A[i],A[i+j]))
                L4.append(minimum(A[i],A[i+j],L3[-1]))

    
    for i in range(len(L4)):
        if(len(L4) == 1):
            L5 = L4
            break
        if(i >= len(L4)/2):
            break
        L5.append(L4[i]+L4[len(L4)-i-1])
    
    print(L3)
    print(L4)
    print(L5)
    
    if(L5 == []):
        return 0
    else:
        return max(L5)



print('LB2 = ',LB2c(A))
