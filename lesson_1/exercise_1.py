a=int(input("Введите целое число"))
max=0
while a>0:
    b=a%10
    if b>=max: max=b
    a//=10
print(max)
