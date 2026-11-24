w=eval(input("Enter your weight(kg): "))
h=eval(input("Enter your height(ft): "))
meter=h*0.3048
total=w/meter**2
if total>=30:
    print("Obesity")
elif total<=29.5 and total>=24.5:
    print("Over weight")
elif total>=18.5 and total<=24.5:
    print("Healthy weight")
elif total<18.5:
    print("Under weight")
