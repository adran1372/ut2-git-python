import random

num = random.randint(1,20)

while True:
    secreto = int(input("Intenta adivinar mi numero: "))
    if(secreto == num):
        print("Has ganado!!!")
        break;
    elif(secreto > num):
        print("El numero es mas pequeño")
    else:
        print("El numero es mayor")


