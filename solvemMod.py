

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
    equation = equation.replace("a*(", "d|(")
    equation = equation.replace("a/(", "a/1d|(")
    equation = equation.replace("s+(", "s+1d|(")
    equation = equation.replace("s-(", "s-1d|(")
    equation = equation.replace("0(", "0d|(")
    equation = equation.replace("1(", "1d|(")
    equation = equation.replace("2(", "2d|(")
    equation = equation.replace("3(", "3d|(")
    equation = equation.replace("4(", "4d|(")
    equation = equation.replace("5(", "5d|(")
    equation = equation.replace("6(", "6d|(")
    equation = equation.replace("7(", "7d|(")
    equation = equation.replace("8(", "8d|(")
    equation = equation.replace("9(", "9d|(")
    equation = equation.replace(")a*", ")|d")
    equation = equation.replace(")a/", ")|d1a/")
    equation = equation.replace(")s+", ")|d1s+")
    equation = equation.replace(")s-", ")|d1s-")
    equation = equation.replace(")0", ")|d0")
    equation = equation.replace(")1", ")|d1")
    equation = equation.replace(")2", ")|d2")
    equation = equation.replace(")3", ")|d3")
    equation = equation.replace(")4", ")|d4")
    equation = equation.replace(")5", ")|d5")
    equation = equation.replace(")6", ")|d6")
    equation = equation.replace(")7", ")|d7")
    equation = equation.replace(")8", ")|d8")
    equation = equation.replace(")9", ")|d9")
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
    equation = " " + equation + " "
    distribute = equation.split("|")
    equation =""
    for part in distribute:
        part = part.split("s")
        for piece in part:
            piece = piece.split("a")
            for number in piece:
                if number.__contains__(" ("):
                    distributelist.append(1.0)
                if number.__contains__(") "):
                    distributelist.append(1.0)
                if number.__contains__("d"):
                    numbers = number.replace("d","")
                    distributelist.append(float(numbers))
                if not number.__contains__("d"):
                    equation = equation + number
    length = len(distributelist)
    step = 0
    distributelist1 = []
    while length >= 1:
        distributelist1.append(distributelist[step] * distributelist[step + 1])
        step = step +2
        length = length - 2

    equation = equation.replace(" ", "")
    equation = equation.replace("+", "s+")
    equation = equation.replace("-", "s-")
    equation = equation.replace("*", "a*")
    equation = equation.replace("/", "a/")
    parentheses = equation.split("(")
    timesrun = 0
    for part in parentheses:
        solves = ""
        part =  part.split(")")
        x = x + 1
        for piece in part:

            if piece.__contains__("p"):
                piece = piece.replace("p", "")
                parentheseslist = emdas(piece)
                solves = solves + f"{float(parentheseslist[0]) * distributelist1[timesrun]}" + f"s+{parentheseslist[1] * distributelist1[timesrun]}x"
                solves =solves.replace("+-","-")
                timesrun = timesrun + 1
            else:
                solves = solves + piece
        half = half + solves

    return emdas(half)


def solvex(equation):
    left,right = equation.split("=")

    left, leftX = pemdas(left)
    right, rightX = pemdas(right)

    leftX = float(leftX) - float(rightX)
    right = float(right) - float(left)

    answer = right/leftX

    return f"x = {answer}"


print(solvex(input("equation:\n")))