name=input("enter name\n")
age=input("enter age\n")

print(f"hello {name}")

if int(age) > 18:
    print(f"{name} is eligible for vote")

else:
    print(f"{name} is not eligible for vote")