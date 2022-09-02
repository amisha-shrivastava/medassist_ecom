#import functools
from functools import reduce
L1=[['Pepsi',20,15],['Fanta',45,30],['Frooti',100,60],['Appy',10,5]]
def fn_actualprice(a,b):
    return a+b[1]
def fn_offerprice(a,b):
    return a+b[2]
actualprice=reduce(fn_actualprice,L1,0)
offerprice=reduce(fn_offerprice,L1,0)
print(actualprice)
print(offerprice)
print(actualprice-offerprice)

















