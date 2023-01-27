import math

#Function 1 - Adding resistors in parallel
def parallel(arr):
    sum = 0
    for x in arr:
        sum += 1/x
    
    result = sum ** -1
    return result

#Example of function use
things = [330,1000,2200]
print(round(parallel(things), 3),"ohms")


#Function 2 - Calculating the voltage drop across resistors in series
def potential_divider(v,arr):
    total_resistance = sum(arr)
    voltage_drops = []
    for r in arr:
        voltage_drops = (r / total_resistance) * v
        print (voltage_drops,"v")


#Example of function use
resistors = [3000,1000]
potential_divider(9,resistors)

