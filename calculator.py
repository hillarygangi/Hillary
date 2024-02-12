x = float(input("Enter firstnumber:"))
z = float(input("Enter secondnumber:"))
opperators = input("Enter operator")
if opperators =="+":
    print("Result is:", x+z)
elif opperators =="-":
    print("Result is:", x-z)
elif opperators =="*":
    print("Result is:", x*z)
elif opperators =="/":
    print("Result is:", x/z)
else:
    print("Invalid operator")


