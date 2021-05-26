my_gen = (n  for n in range(0,16) if n % 2 != 0)
def generate():
    for n in my_gen:
        yield n
#for i in range(17):
    #print(next(generate())) // вывод всего списка чисел , без клонирования принт
print(next(generate()),next(generate()))
