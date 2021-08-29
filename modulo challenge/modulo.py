def add_modulo(n):
    send_total = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            value = i + j
            while value >= n:
                value -= n
            temp.append(value)
        send_total.append(temp)

    return send_total

def multiply_modulo(n):
    send_total = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            value = i * j
            while value >= n:
                value -= n
            temp.append(value)
        send_total.append(temp)

    return send_total

def main():
    length = int(input("Enter length: "))
    add_mult = input("Enter 'M' for multiplication or 'A' for addition: ")

    if add_mult == 'M' or add_mult == 'm':
        modulo = multiply_modulo(length)
        for line in modulo:
            print(line)
    elif add_mult == 'A' or add_mult == 'a':
        modulo = add_modulo(length)
        for line in modulo:
            print(line)

if __name__ == '__main__':
    main()
