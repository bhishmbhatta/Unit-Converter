number = int(input("Enter the number: "))

print("\n1. Meter to centimeter")
print("2. Meter to millimeter")
print("3. Centimeter to meter")
print("4. Millimeter to centimeter\n")

opinion = input("Choose conversion (1, 2, 3, 4): ")

if opinion == "1":
    print(number * 100)

elif opinion == "2":
    print(number * 1000)

elif opinion == "3":
    print(number / 100)

elif opinion == "4":
    print(number / 10)

else:
    print("Invalid choice")
