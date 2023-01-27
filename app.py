import math

#Function 1 - Adding resistors in parallel
def parallel(arr):
    sum = 0
    for x in arr:
        sum += 1/x
    
    result = sum ** -1
    return result

#Example of function
things = [330,1000,2200]
print(round(parallel(things), 3),"ohms")
