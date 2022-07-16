fahrenheitArr = [0, 40, 80, 120, 160, 200]
celciusArr = [0, 20, 40, 60, 80]
#Celsius to Fahrenheit conversion
def get_celcius(f):
    c = ((int(f)-32)*5)/9
    float(c)
    return format(c, '.2f')
#Fahrenheit to Celsius conversion
def get_fahrenheit(c):
    f = ((int(c)*9)/5)+32
    float(f)
    return f
#for loops
for f in fahrenheitArr:
    print(f'{f} Fahrenheit = {get_celcius(f)} Celsius')
for c in celciusArr:
    print(f'{c} Celsius = {get_fahrenheit(c)} Fahrenheit')