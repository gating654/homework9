def test(name, *assessments, c="Успеваемость студента"):
    print(name)
    print("Оценки:", *assessments)
    print(c)

test("Denis", 5, 4, 3, 4, 5)

def factorial(n):
    f = 1
    for i in range(0, n):
        f = (i + 1) * f
    print(f)

factorial(5)