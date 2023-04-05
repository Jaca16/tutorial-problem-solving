print("Welcome to Jesse's calculator!")
print("Click 'ENTER' to continue")
print(" ")

num1 = float(input("input 1st number "))
num2 = float(input("input 2nd number "))


def add(num1, num2):
    ans = num1 + num2
    return ans


def sub(num1, num2):
    ans = num1 - num2
    return ans


def mul(num1, num2):
    ans = num1 * num2
    return ans


def div(num1, num2):
    ans = num1 / num2
    return ans


operation = str(input("What operation do you want to carry out?: \n('add' - addition)\n('sub' - subtraction)\n('mul' "
                      "- multiplication)\n('div' - division)\n"))
if operation == "add":
    print(add(num1, num2))
elif operation == "sub":
    print(sub(num1, num2))
elif operation == "mul":
    print(mul(num1, num2))
elif operation == "div":
    print(div(num1, num2))
else:
    print("Error! Not a valid operation")
