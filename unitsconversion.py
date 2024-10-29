#kilometer to miles    mile =  km*0.6213
def kilo_miles(value):
    return value*0.6213
miles =  kilo_miles(12)
print("kilometeres in miles is", miles)
# celsius to faraheit  fahr = (cels * 9.0/5.0) + 32.0;
# f to C = C = ((f-32.0)* (5.0/9.0))

def celsius_fahrenheit(value):
    return (value*9.0/5.0) + 32.0
fahrenheit = celsius_fahrenheit(25)
print("celsius in fahrenheit is", fahrenheit)