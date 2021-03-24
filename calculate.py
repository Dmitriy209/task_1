yournumber = float(input("Введите число: "))
operator=[0]
while operator[0] != '=':
    operator = input().split()
    if operator[0] == '+':
        yournumber=yournumber+float(operator[1])
        print (yournumber)
    elif operator[0] == '-':
        yournumber=yournumber-float(operator[1])
        print(yournumber)
    elif operator[0] == '*':
        yournumber=yournumber*float(operator[1])
        print(yournumber)
    elif operator[0] == '/':
        yournumber=yournumber/float(operator[1])
        print(yournumber)
    elif operator[0] == '//':
        yournumber=yournumber//float(operator[1])
        print(yournumber)
    elif operator[0] == '%':
        yournumber=yournumber%float(operator[1])
        print(yournumber)
    elif operator[0] == '**':
        yournumber=yournumber**float(operator[1])
        print(yournumber)
    elif operator[0] == '=':
        break
    else:
        print ("Не корректный ввод.")
        quit()
print('Ваше число: ', yournumber)
