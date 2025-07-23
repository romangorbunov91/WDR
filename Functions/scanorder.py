# version 0.1 by romangorbunov91
# 23-Jul-2025
import numpy as np

def zigzag_order(Nrow, Ncol, LH_to_RL):
    s = np.zeros((Nrow, Ncol), dtype=int)
    
    n = Nrow - 1
    m = 0
    
    counter = 1
    s[n,m] = counter

    while counter < Nrow*Ncol:
        if LH_to_RL:
            n += 1
            m += 1
        else:
            n -= 1
            m -= 1
        
        if n < 0:
            n = 0
            if not LH_to_RL:
                m += 2
            else:
                m += 1
            LH_to_RL = True
        elif n > (Nrow-1):
            n = Nrow-1
            LH_to_RL = False    

        if m < 0:
            m = 0
            LH_to_RL = True
        elif m > (Ncol-1):
            m = Ncol-1
            if LH_to_RL:
                n -= 2
            else:
                n -= 1
            LH_to_RL = False      
        
        counter += 1
        s[n,m] = counter
    return s

def horizont_order(Nrow, Ncol, L_to_R):
    s = np.zeros((Nrow, Ncol), dtype=int)
    
    n = Nrow - 1
    if L_to_R:
        m = 0
    else:
        m = Ncol - 1
    
    counter = 1
    s[n,m] = counter
    
    while counter < Nrow*Ncol:
        if L_to_R:
            m += 1
        else:
            m -= 1
        
        if (m >= (Ncol-1)) or (m <= 0):
            n -= 1
            L_to_R ^= True  # XOR with True flips the value
        
        if n < 0:
            raise ValueError("Roman: Index exceeds number of rows")
        
        counter += 1
        s[n,m] = counter
    return s

#def vertical_order(Nrow, Ncol, LH_to_RL):