import math

easynumber = int(input("Введите простое число: "))
if easynumber<2:
    print("Введите больше 1")
    quit()
elif easynumber==2:
    print(easynumber, "Это простое число")
    quit()
i = 2
limit = int(math.sqrt(easynumber))
while i<=limit:
    if easynumber % i==0:
        print(easynumber, "Это не простое число")
        quit()
    i+=1
print(easynumber, "Это простое число")

