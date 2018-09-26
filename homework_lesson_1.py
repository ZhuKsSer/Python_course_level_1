
# coding: utf-8

# In[42]:


a=int(input("Введите целое число"))
max=0
while a>0:
    b=a%10
    if b>=max: max=b
    a//=10
print(max)


#  

# In[40]:


import math
print("Введите коэффициенты для квадратного уравнения (ax² + bx + c = 0).")
a=float(input("Введите первый коэффициент a: "))
b=float(input("Введите второй коэффициент b: "))
c=float(input("Введите третий коэффициент c: "))
discr=b**2 - 4 * a * c;
print("Дискриминант = ", discr)

if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
        
elif discr == 0:
        x3 = -b / (2 * a)
        print("Единственный корень x = ", x)
        
elif discr < 0:
        print("Дискриминант меньше нуля, соответсвенно корней нет.")


# In[43]:


x=int(input("Введите переменную 1: "))
y=int(input("Введите переменную 2: "))
x, y = y, x
print(x, y)

