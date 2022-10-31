'''Exercise 5.2'''

def convert_temp(temp = 0.00, Fahrenheit = False):
    while Fahrenheit == False:
        if temp < -273.15:
            return None
        else:
            f = (9/5)*temp + 32
            f = round(f, 2)
            return f

    while Fahrenheit == True:
        if temp < -459.67:
            return None
        else:
            c = (5/9)*(temp - 32)
            c = round(c, 2)
            return c  


# def convert_temp_2(fahrenheit = 0.00):
#   while fahrenheit > 0.00:
#     c = (5/9)*fahrenheit - 32
#     round (c, 2)
#     return c
#   return None

print(convert_temp(68, Fahrenheit = True))
#convert_temp(20)