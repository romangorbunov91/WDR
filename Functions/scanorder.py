# version 0.3 by romangorbunov91
# 26-Jul-2025
import numpy as np

def zigzag_order(Nrow, Ncol, LH_to_RL, init_value):
    s = np.zeros((Nrow, Ncol), dtype=int)
    
    n = Nrow - 1
    m = 0
    
    counter = init_value
    s[n,m] = counter

    while (counter - init_value) < (Nrow*Ncol - 1):
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

def horizont_order(Nrow, Ncol, LEFT_to_RIGHT, BOT_to_TOP, init_value):
    s = np.zeros((Nrow, Ncol), dtype=int)
     
    if LEFT_to_RIGHT:
        m = 0
    else:
        m = Ncol - 1
     
    if BOT_to_TOP:
        n = Nrow - 1
    else:
        n = 0
      
    counter = init_value
    s[n,m] = counter
    
    while (counter - init_value) < (Nrow*Ncol - 1):
        
        if LEFT_to_RIGHT:
            if m == (Ncol-1):
                if BOT_to_TOP:
                    n -= 1
                else:
                    n += 1
                LEFT_to_RIGHT = False
            else:
                m += 1
        else:
            if m == 0:
                if BOT_to_TOP:
                    n -= 1
                else:
                    n += 1
                LEFT_to_RIGHT = True
            else:
                m -= 1
        counter += 1
        s[n,m] = counter
    return s

def vertical_order(Nrow, Ncol, BOT_to_TOP, LEFT_to_RIGHT, init_value):
    s = np.zeros((Nrow, Ncol), dtype=int)
    
    if BOT_to_TOP:
        n = Nrow - 1
    else:
        n = 0
        
    if LEFT_to_RIGHT:
        m = 0
    else:
        m = Ncol - 1
    
    counter = init_value
    s[n,m] = counter
    
    while (counter - init_value) < (Nrow*Ncol - 1):
        
        if BOT_to_TOP:
            if n == 0:
                if LEFT_to_RIGHT:
                    m += 1
                else:
                    m -= 1
                BOT_to_TOP = False
            else:
                n -= 1
        else:
            if n == (Nrow-1):
                if LEFT_to_RIGHT:
                    m += 1
                else:
                    m -= 1
                BOT_to_TOP = True   
            else:
                n += 1
        
        counter += 1
        s[n,m] = counter
    return s