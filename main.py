
def main(expression:str):
    values = expression.split()

    if len(values) == 3 and int(values[0]) in range(1, 11) and int(values[2]) in range(1, 11):
        a = int(values[0])
        b = int(values[2])

        calc = {
            "+": a + b,
            "/": a / b,
            "*": a * b,
            "-": a - b
        }

        print(str(int(calc[values[1]])))

    else:
        raise Exception('недопустимое выражение')

main(input())