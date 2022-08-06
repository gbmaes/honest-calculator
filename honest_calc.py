msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_ = ["Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]

operators = ["+", "-", "*", "/"]
memory = 0


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v3 == "*" and (v1 == 1 or v2 == 1):
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "-" or v3 == "+"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    try:
        x, oper, y = calc.split()
    except ValueError:
        print("Please print a valid equation")
        continue
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if oper in operators:
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
        else:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/":
                try:
                    result = x / y
                except ZeroDivisionError:
                    print(msg_3)
                    continue
            print(result)
            answer_4 = ""
            while answer_4 != "y" or answer_4 != "n":
                print(msg_4)
                answer_4 = input()
                if answer_4 == "y":
                    if is_one_digit(result):
                        msg_index = 0
                        answer_10 = ""
                        while answer_10 != "n":
                            print(msg_[msg_index])
                            answer_10 = input()
                            if answer_10 == "y" and msg_index < 2:
                                msg_index += 1
                                continue
                            elif answer_10 == "n":
                                break
                            else:
                                memory = result
                                break
                    else:
                        memory = result
                    break
                elif answer_4 == "n":
                    break
                else:
                    continue
        answer_5 = ""
        while answer_5 != "y" or answer_5 != "n":
            print(msg_5)
            answer_5 = input()
            if answer_5 == "y":
                break
            elif answer_5 == "n":
                break
            else:
                continue
        if answer_5 == "y":
            continue
        break
    else:
        print(msg_2)
