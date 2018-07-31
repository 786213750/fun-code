from scipy.optimize import fsolve
import numpy as np
import math
import random

## pip install scipy  
##change the condition for gamma
def Cal_gamma(n):
    gamma=1
    while n>1:
        if n%2 !=0:
            gamma = 0
            break        
        if n%2**gamma ==0 and n%2**(gamma+1) != 0:
            break
        gamma=gamma+1
    return gamma


def equations(p):
    arr = np.zeros((n,n))
    indices = np.tril_indices(n)
    list_ca= list_cal.copy()
    for i in range(len(p)):
        if type(list_ca)==np.ndarray:
            list_ca=list_ca.tolist()
        list_ca.append(p[i])

    arr[indices] = list_ca
    arr=np.array(arr) 
    functions=arr.dot(arr[-1,:])
    out=[]
    for i in range(n):
        globals()['a%s' % i] = functions[i]-c_list[i]   
        out.append(globals()['a%s' % i])

    return tuple(out)

def use_f(d,c):
    globals()['list_cal']=[]
    for i in range(d):
        globals()['n']=i+1
        globals()['c_list']=[]
        for j in range(n):
            ##c_list.append((c**Cal_gamma(j+1)-c**Cal_gamma(n-j-1)+c**Cal_gamma(n))/2)  ###this is the line for calculating right side of equation fix it 
            c_list.append(2)                                                           ##delete this line
        r_list =[random.random() for _ in range(n)]
        #print(r_list)
        cal=fsolve(equations,r_list,xtol=10e-7) 
        for i in range(len(cal)):
            if type(list_cal)==np.ndarray:
                globals()['list_cal']=list_cal.tolist()
            list_cal.append(cal[i])        
    return(list_cal)
## solver https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html#scipy.optimize.fsolve
x=  use_f(3,1)
arr = np.zeros((3,3))         
indices = np.tril_indices(3)
arr[indices] = x
print(x)
print(arr)


