num = int(input("Hasta que numero quieres  llegar: "))
for i in range(1,num+1):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
        i+= 1
    elif(i % 5 == 0):
        print("Buzz")
        i+= 1
    elif(i % 3 == 0 ):
        print("Fizz")
        i+= 1
    else:
        print(i)
        i+= 1
print("Fin")