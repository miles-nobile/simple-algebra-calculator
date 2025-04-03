from functools import reduce
from fractions import Fraction


def hasNum(string):
    for part in string[:]:
        part = str(part)
        if part.isdigit(): return True
    return False


def denomator(x): return Fraction(x).limit_denominator().denominator


def numerator(x): return Fraction(x).limit_denominator().numerator


def find_gcf_two_numbers(a, b):
    while b:
        a, b = b, a % b
    return a


def gcf_three_numbers(a, b, c):

    gcf_ab = find_gcf_two_numbers(a, b)

    final_gcf = find_gcf_two_numbers(gcf_ab, c)

    return final_gcf

def factors(n):
    return list(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factor(equation,equation1,num0, gcf):
    factor_list = list(factors(abs(equation)))
    factor_list.sort()
    while len(factor_list) > 1:
        if gcf > 1:
            if float(equation1) == float(factor_list[0])+ float(factor_list[-1]):
                return f"{gcf}({numerator(float(num0)/float(factor_list[0]))}x + {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x + {denomator(float(num0)/float(factor_list[-1]))})"
            elif float(equation1) == - float(factor_list[0]) - float(factor_list[-1]):
                return f"{gcf}({numerator(float(num0)/float(factor_list[0]))}x - {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x - {denomator(float(num0)/float(factor_list[-1]))})"
            elif float(equation1) == - float(factor_list[0]) + float(factor_list[-1]):
                return f"{gcf}({numerator(float(num0)/float(factor_list[0]))}x - {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x + {denomator(float(num0)/float(factor_list[-1]))})"
            elif float(equation1) == + float(factor_list[0]) - float(factor_list[-1]):
                return f"{gcf}({numerator(float(num0)/float(factor_list[0]))}x + {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x - {denomator(float(num0)/float(factor_list[-1]))})"
            else:
                pass
            del factor_list[0]
            del factor_list[-1]
        else:
            if float(equation1) == float(factor_list[0])+ float(factor_list[-1]):
                return f"({numerator(float(num0)/float(factor_list[0]))}x + {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x + {denomator(float(num0)/float(factor_list[-1]))})"
            elif float(equation1) == - float(factor_list[0]) - float(factor_list[-1]):
                return f"({numerator(float(num0)/float(factor_list[0]))}x - {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x - {denomator(float(num0)/float(factor_list[-1]))})"
            elif float(equation1) == - float(factor_list[0]) + float(factor_list[-1]):
                return f"({numerator(float(num0)/float(factor_list[0]))}x - {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x + {denomator(float(num0)/float(factor_list[-1]))})"
            elif float(equation1) == + float(factor_list[0]) - float(factor_list[-1]):
                return f"({numerator(float(num0)/float(factor_list[0]))}x + {denomator(float(num0)/float(factor_list[0]))})({numerator(float(num0)/float(factor_list[-1]))}x - {denomator(float(num0)/float(factor_list[-1]))})"
            else:
                pass
            del factor_list[0]
            del factor_list[-1]
    return "Prime"


def factor_trinomials(equation):
    equation = equation.replace(" ", "")
    equation = equation.replace("+", "s+")
    equation = equation.replace("0-", "0s-")
    equation = equation.replace("1-", "1s-")
    equation = equation.replace("2-", "2s-")
    equation = equation.replace("3-", "3s-")
    equation = equation.replace("4-", "4s-")
    equation = equation.replace("5-", "5s-")
    equation = equation.replace("6-", "6s-")
    equation = equation.replace("7-", "7s-")
    equation = equation.replace("8-", "8s-")
    equation = equation.replace("9-", "9s-")
    equation = equation.replace("x-", "xs-")
    equation = equation.replace("^2", "")
    equation = equation.replace("^", "")
    equation = equation.replace("x", "")
    num0, num1, num2 = equation.split("s")
    if not hasNum(num0): num0 = 1
    if not hasNum(num1): num1 = 1
    gcf = gcf_three_numbers(int(num0),int(num1),int(num2))
    gcf = abs(gcf)
    num0 = int(num0) / gcf
    num1 = int(num1) / gcf
    num2 = int(num2) / gcf
    test = float(num0) * float(num2)
    test = int(test)
    return factor(test, num1, num0, gcf)


print(factor_trinomials(input("equation:\n")))

