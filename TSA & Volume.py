# To calculate Total Surface Area and Volume of a
# cylinder,sphere,cone depending upon the user's choice

print("1. Cylinder")
print("2. Sphere")
print("3. Cone")

pi = 3.14
choice = int(input("Enter your choice  (1, 2, or 3): "))
if choice == 1:
    r = float(input("Enter radius of cylinder: "))
    h = float(input("Enter height of cylinder: "))
    TSA = 2 * pi * r * h + 2 * pi * r * r
    Vol = pi * r * r * h
    print("Total Surface Area =", round(TSA, 2), "sq. units")
    print("Volume =", round(Vol, 2), "cu. units")

elif choice == 2:
    r = float(input("Enter radius of sphere: "))
    TSA = 4 * pi * r * r
    Vol = 4 / 3 * pi * r * r * r
    print("Total Surface Area =", round(TSA, 2), "sq. units")
    print("Volume =", round(Vol, 2), "cu. units")

elif choice == 3:
    r = float(input("Enter radius of cone: "))
    h = float(input("Enter height of cone: "))
    l = (r * r + h * h) ** 0.5
    TSA = pi * r * l + pi * r * r
    Vol = pi * r * r * h / 3
    print("Total Surface Area =", round(TSA, 2), "sq. units")
    print("Volume =", round(Vol, 2), "cu. units")
else:
    print("!!! Invalid Choice !!!")