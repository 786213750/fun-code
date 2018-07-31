import numpy as np
import pandas as pd

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
print(Cal_gamma(4))
        
    