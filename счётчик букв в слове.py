i = "абвгдеёжзийклмнопрстуфхцчшщыьэюя"
x = str(input("введите слово: "))
print("в слове " + x + ":")
bukvai = [2,3,4]
for y in i:
    count = 0
    for b in x:
        if y == b:
            count +=1
    if count == 1:
        print(count, "буква " + y)
    elif count in bukvai:
        print(count, "буквы " + y)
    elif count >0:
        print(count, "букв " + y)
        