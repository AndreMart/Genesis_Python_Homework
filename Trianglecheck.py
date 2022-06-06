def is_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

def triangle_type(a,b,c):
    if a==b and b==c:
        print('Треугольник Равносторонний')
    elif a==b or b==c or a==c:
        print('Треугольник Равнобедренний')
    elif a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b:
        print("Треугольник Прямоугольный")
    else:
        print('Треугольник Неравносторонний')

a = int(input("Сторона a = "))
b = int(input("Сторона b = "))
c = int(input("Сторона c = "))

if is_triangle(a, b, c):
    triangle_type(a, b, c)
else:
    print('Треугольник составить невозможно.')