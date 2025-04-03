from functools import reduce
from fractions import Fraction


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
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factor(equation,equation1,num0, gcf):
    factor_list = list(factors(abs(equation)))
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
    equation = equation.replace("^2", "")
    equation = equation.replace("x", "")
    num0, num1, num2 = equation.split("s")
    gcf = gcf_three_numbers(int(num0),int(num1),int(num2))
    num0 = int(num0) / gcf
    num1 = int(num1) / gcf
    num2 = int(num2) / gcf
    test = float(num0) * float(num2)
    test = int(test)
    return factor(test, num1, num0, gcf)


print(factor_trinomials("2x^2+8x+6"))

