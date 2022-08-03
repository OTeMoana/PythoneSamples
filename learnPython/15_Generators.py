

def Fibo_generic():
    b = 1
    a = 2

    for i in range(7):



        a = a + b

        b = a - b

        yield a


for i in Fibo_generic():
    print("Ось моя булава", i)