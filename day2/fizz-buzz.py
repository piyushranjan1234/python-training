for x in range(1,30):
    if x % 15==0:
        print("fizzbuzz")
        continue
    elif x % 3 == 0:
        print("fizz")
        continue
    elif x % 5 == 0:
        print("buzz")
        continue
    print(x)