from functools import reduce


def find_gcf_two_numbers(a, b):
    while b:
        a, b = b, a % b
    return a


def find_gcf_three_numbers(a, b, c):

    gcf_ab = find_gcf_two_numbers(a, b)

    final_gcf = find_gcf_two_numbers(gcf_ab, c)

    return final_gcf

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factor(equation,equation1,num0):
    factor_list = list(factors(abs(equation)))
    while len(factor_list) > 0:
        if float(equation1) == float(factor_list[0])+ float(factor_list[-1]):
            return f"{int(factor_list[0])}, {int(factor_list[-1])}"
        elif float(equation1) == - float(factor_list[0]) - float(factor_list[-1]):
            return f"-{factor_list[0]}, -{factor_list[-1]}"
        elif float(equation1) == - float(factor_list[0]) + float(factor_list[-1]):
            return f"-{factor_list[0]}, {factor_list[-1]}"
        elif float(equation1) == + float(factor_list[0]) - float(factor_list[-1]):
            return f"{factor_list[0]}, -{factor_list[-1]}"
        else:
            pass
        del factor_list[0]
        del factor_list[-1]
    return "Prime"


def factor_trinomials(equation):
    equation = equation.replace(" ", "")
    equation = equation.replace("+", "s+")
    equation = equation.replace("0-", "s-")
    equation = equation.replace("1-", "s-")
    equation = equation.replace("2-", "s-")
    equation = equation.replace("3-", "s-")
    equation = equation.replace("4-", "s-")
    equation = equation.replace("5-", "s-")
    equation = equation.replace("6-", "s-")
    equation = equation.replace("7-", "s-")
    equation = equation.replace("8-", "s-")
    equation = equation.replace("9-", "s-")
    equation = equation.replace("x-", "s-")
    num0, num1, num2 = equation.split("s")
    test = float(num0) * float(num2)
    print(float(num1))
    print(test)
    return factor(test, num1,num0)


print(factor_trinomials("-2+4+6"))

