#WRITE YOUR CODE IN THIS FILE

def close10(x, y):
    if abs(x - 10) > abs (y - 10):
        return y
    elif abs(x - 10) == (y - 10):
        return 0
    else:
        return x
print (close10(9, 50))
print (close10(8, 12))
print (close10(50, 9))