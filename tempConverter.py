def celsius(t):
    fah=(t*9/5)+32
    
    print(f"Temperature in Fahrenheit: {fah:.2f}°F ")
    
def fahrenheit(t):
    cel=(t-32)*5/9
    
    print(f"Temperature in Celsius: {cel:.2f}°C ")
    
print("----------- Temperature Converter -------------")
print()
print("1.Celsius To Fahrenheit")
print("2.Fahrenheit To Celsius")
c=int(input("Enter Your Choice: "))
if c==1:
    print()
    t=int(input("Enter Temperature in Celsius : "))
    celsius(t)
elif c==2:
    print()
    t=int(input("Enter Temperature in Fahrenheit; "))
    fahrenheit(t)
else:
    print("Invalid Choice")
