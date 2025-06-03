def encode(x):
    y = bin(x)
    if x > 0:
        return y.replace('0b1','+')
    else:
        return y.replace('-0b1','-')