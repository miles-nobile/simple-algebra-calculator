

def hasNum(string):
    for part in string[:]:
        part = str(part)
        if part.isdigit(): return True

    return False


def emdas(equation):
    id = []
    rightX = []
    symple = equation.split("s")
    x = -1
    for part in symple:
        x = x + 1
        if part.__contains__("a"):
            part = part.split("a")
            for piece in part:
                if not piece.__contains__("*") and not piece.__contains__("/"):
                    if piece.__contains__("^"):
                        try:
                            part2, part1 = piece.split("^")
                        except:
                            part1 = "2"
                        if part1 == "": part1 = "2"
                        piece = float(part2) ** float(part1)
                    solve = float(piece)
                elif piece.__contains__("*"):
                    piece = piece.replace("*", "")
                    if piece.__contains__("^"):
                        try:
                            part2, part1 = piece.split("^")
                        except:
                            part1 = "2"
                        if part1 == "": part1 = "2"
                        piece = float(part2) ** float(part1)
                    solve = solve * float(piece)
                elif piece.__contains__("/"):
                    piece = piece.replace("/", "")
                    if piece.__contains__("^"):
                        try:
                            part2, part1 = piece.split("^")
                        except:
                            part1 = "2"
                        if part1 == "": part1 = "2"
                        piece = float(part2) ** float(part1)
                    solve = solve / float(piece)
            id.insert(x, solve)
        else:
            if part.__contains__("x"):
                rightX.insert(x, part)
            else:
                id.insert(x, part)
    numSolve = 0
    xSolve = 0

    for part in rightX:
        part = part.replace("x","")
        if not hasNum(part):
            part = part + "1"
        if str(part).__contains__("^"):
            try:
                part2, part1 = part.split("^")
            except:
                part1 = "2"
            if part1 == "": part1 = "2"
            part = float(part2) ** float(part1)
        xSolve = xSolve + float(part)

    for part in id:
        if part == "": part = "0"
        if str(part).__contains__("^"):
            try:
                part2, part1 = part.split("^")
            except:
                part1 = "2"
            if part1 == "": part1 = "2"
            part = float(part2) ** float(part1)
        numSolve = numSolve + float(part)
    return numSolve,xSolve


def pemdas(equation):
    half = ""
    x = -1
    equation = equation.replace(" ", "")
    equation = equation.replace("+", "s+")
    equation = equation.replace("-", "s-")
    equation = equation.replace("*", "a*")
    equation = equation.replace("/", "a/")
    equation = equation.replace("0(", "0a*(")
    equation = equation.replace("1(", "1a*(")
    equation = equation.replace("2(", "2a*(")
    equation = equation.replace("3(", "3a*(")
    equation = equation.replace("4(", "4a*(")
    equation = equation.replace("5(", "5a*(")
    equation = equation.replace("6(", "6a*(")
    equation = equation.replace("7(", "7a*(")
    equation = equation.replace("8(", "8a*(")
    equation = equation.replace("9(", "9a*(")
    equation = equation.replace(")0", ")a*0")
    equation = equation.replace(")1", ")|1d")
    equation = equation.replace(")2", ")a*2")
    equation = equation.replace(")3", ")a*3")
    equation = equation.replace(")4", ")a*4")
    equation = equation.replace(")5", ")a*5")
    equation = equation.replace(")6", ")a*6")
    equation = equation.replace(")7", ")a*7")
    equation = equation.replace(")8", ")a*8")
    equation = equation.replace(")9", ")a*9")
    equation = equation.replace(")", "p)")
    equation = equation.replace("+a*", "+")
    equation = equation.replace("-a*", "-")
    equation = equation.replace("a*s+", "s+")
    equation = equation.replace("a*s-", "s-")
    equation = equation.replace("/a*", "/")
    equation = equation.replace("*a/", "/")
    equation = equation.replace("a*a*", "a*")
    distributelist = []
    testlist = []
    distribute = equation.split("|")
    equation =""
    for part in distribute:
        part = part.split("s")
        for piece in part:
            piece = piece.split("a")
            for number in piece:
                if number.__contains__("d"):
                    numbers = number.replace("d","")
                    distributelist.append(numbers)
                if not number.__contains__("d"):
                    equation = equation + number
    print(equation)
    print(distributelist)
    parentheses = equation.split("(")
    for part in parentheses:
        solves = ""
        part =  part.split(")")
        x = x + 1
        for piece in part:

            if piece.__contains__("p"):
                piece = piece.replace("p", "")
                solves = solves + str(emdas(piece))
            else:
                solves = solves + piece
        half = half + solves

    return emdas(half)

def sloveX(equation):
    left,right = equation.split("=")

    left, leftX = pemdas(left)
    right, rightX = pemdas(right)

    leftX = float(leftX) - float(rightX)
    right = float(right) - float(left)

    answer = right/leftX

    return f"x = {answer}"


print(sloveX("5=(1)1+x"))