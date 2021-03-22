def calculator():
    try:
        num = float(input("Start calculator\nEnter a number\n"))
        while True:
            sign = input()
            if sign == '=':
                print(num)
                break
            if sign in ('+', '-', '*', '/', '**', '//', '%'):
                x = float(input())
                if sign == '+':
                    num += x
                elif sign == '-':
                    num -= x
                elif sign == '**':
                    num **= x
                elif sign == '*':
                    num *= x
                elif sign == '//':
                    num //= x
                elif sign == '%':
                    num %= x
                elif sign == '/':
                    num /= x
            else:
                raise Exception
    except ValueError:
        print("Entered sequence is not a number, try again!")
    except ZeroDivisionError:
        print("You can't divide by zero")
    except Exception:
        print("Unsupported operation!")


calculator()
