# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:03:10 2019

@author: USER
"""

import numpy as np
import time
from gurobipy import *

cons = [0,0,0,0,0,0,0,0]
#演員每日成本 ci
c = [200, 250, 400, 320, 400, 260, 120] 
#片場每日成本
C = 2000

#每場所需時間 bj
b = [2, 0.5, 1.5, 1.5, 2, 1, 3, 3.5]

#每日工時 B
B = 5

#場景j需要演員i aij
a = [[1,1,1,0,0,1,0,0],
     [1,1,0,0,0,1,1,0],
     [0,1,0,1,0,0,0,1],
     [0,1,0,1,1,1,0,0],
     [0,1,0,0,0,0,0,1],
     [0,0,1,1,0,1,0,1],
     [1,0,1,0,1,0,1,0]]

m = len(c) #i
n = len(b) #j
d = 3 #k

try:
  M = Model("mip1")
  #m為job n為工作 有4job 5work [, , , ]X5
  
  x=M.addVars(n,d,vtype=GRB.BINARY,name="x")
  z=M.addVars(d,vtype=GRB.BINARY,name="z")
  y=M.addVars(m,d,vtype=GRB.BINARY,name="y")
  v=M.addVars(m,vtype=GRB.INTEGER,name="v")
##  可以設lb ub (int用)
#  i=M.addVars(n,vtype=GRB.INTEGER,name="i")
#  w=M.addVars(n,vtype=GRB.INTEGER,name="w")
  M.update()
  Line = LinExpr()
#      Line.addTerms(1,c[2,i]) #前面係數後面變數 c0 c1 c2的係數都是1
  #Line.addTerms(C*(d-1))
  for i in range(m):
      Line.addTerms(c[i],v[i])
  for i in range(d):
      Line.addTerms(C,z[i])
      
  M.setObjective(Line,GRB.MINIMIZE)
  
  for j in range(n):
      cons[0] = LinExpr()
      for k in range(d):
          cons[0].addTerms(1,x[j,k])
      M.addConstr(cons[0]==1)
  
  for k in range(d):
      cons[1] = LinExpr()
      for j in range(n):
          cons[1].addTerms(b[j],x[j,k])
      M.addConstr(cons[1]<= B*z[k])
      
  for i in range(m):
      for j in range(n):
          for k in range(d):
              M.addConstr(a[i][j]*x[j,k]<=y[i,k])
  
  for i in range(m):
      for k_2 in range(d):
          for k_1 in range(d):
              M.addConstr(v[i]>=(k_2-k_1+1) + (y[i,k_1]-1)*m + (y[i,k_2]-1)*m) 
 
  starttime = time.time()     
  M.optimize()
  endtime = time.time()     
  
  for v in M.getVars():
      print('%s %g'%(v.varName,v.x))
      
  print('Obj:%g'%M.objVal)
  
except GurobiError:
    print('Encountered a Gurobi error')
    
except AttributeError:
    print('Encountered an attribute error')
    
print('Total:',endtime-starttime) 