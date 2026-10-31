number=int(input("Enter the number of unit convertor:"))

print("\n1.Meter to centimeter")
print("2.Meter to milimeter")
print("3.centimeter to meter")
print("4.milimeter to centimeter\n")

opinion=input("Enter your unit convertor (1,2,3,4):")

if opinion=="1":
    print(number*100)

elif opinion=="2":
    print(number*1000)

elif opinion=="3":
    print(number/100)

elif opinion=="4":
    print(number/1000)

else:
    print("Invalid opinion")