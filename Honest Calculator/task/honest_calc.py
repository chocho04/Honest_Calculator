memory = 0
result = 0
msg = ""
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msgs = [msg_10, msg_11, msg_12]
msg_index = 0


def is_one_digit(number):
    if float(number).is_integer():
        return 10 > number > -10
    else:
        return False


def check(v1, v2, v3):
    global msg
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


def loop():
    global msg_index
    global memory
    print(msgs[msg_index])
    if input() == "y":
        if msg_index < 2:
            msg_index += 1
            loop()
        else:
            memory = result


while True:
    print("Enter an equation")
    x, oper, y = input().split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue
    if oper not in ["+", "-", "*", "/"]:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue
    check(x, y, oper)
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        if y == 0:
            print("Yeah... division by zero. Smart move...")
            continue
        else:
            result = x / y
    print(result)
    print("Do you want to store the result? (y / n):")

    if input() == "y":
        if is_one_digit(result):
            msg_index = 0
            loop()
        else:
            memory = result

    print("Do you want to continue calculations? (y / n):")
    if input() == "y":
        continue
    else:
        break
