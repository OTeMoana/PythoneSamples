


def dist(a, b):
    c = (a * a + b * b) ** 0.5
    print(f"В пропах: {c:4.2f}")
    c *= 5
    print(f"В метрах: {c:4.2f}")


while 1:
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        dist(a, b)
    except:
        print()
