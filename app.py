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


#Function 3 - Detecting abnormal temperatures
def temperature_check(x,char):
    if (char == "C" or char == "c"):
        if (x > 35 and x < 37.5):
            print("The patient's temperature is normal")
        if (x < 35):
            print("The patient is hypothermic")
        if(x > 37.5):
            print("The patient is hyperthermic")
    elif (char == "F" or char == "f"):
        if (x > 97 and x < 99):
            print("The patient's temperature is normal")
        if (x < 97):
            print("The patient is hypothermic")
        if(x > 99):
            print("The patient is hyperthermic")
    else:
        print("Invalid units entered please enter temperature in degrees C or degrees F")


#Example of function use
temperature_check(98,"f")