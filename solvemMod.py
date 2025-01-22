

def has_num(string):
    for part in string[:]:
        part = str(part)
        if part.isdigit(): return True

    return False


def x_emdas(equation):
    global xDivide
    id = []
    rightX = []
    symple = equation.split("s")
    x = -1
    for part in symple:
        x = x + 1
        if part.__contains__("a"):
            part = part.split("a")
            solve = ""
            for piece in part:
                if piece.__contains__("x") and not has_num(piece): piece = piece.replace("x", "1x")
                if piece.__contains__("x") is not solve.__contains__("x"):
                    if not piece.__contains__("*") and not piece.__contains__("/"): solve = str(piece)
                    elif piece.__contains__("*"):
                        piece = piece.replace("*", "")
                        if piece.__contains__("^"):
                            try:
                                part2, part1 = piece.split("^")
                            except:
                                part1 = "2"
                            if part1 == "": part1 = "2"
                            piece = float(part2) ** float(part1)
                        piece = piece.replace("x", "")
                        solve = solve.replace("x", "")
                        solve = f"{float(solve) * float(piece)}x"
                    elif piece.__contains__("/"):
                        piece = piece.replace("/", "")
                        if piece.__contains__("^"):
                            try:
                                part2, part1 = piece.split("^")
                            except:
                                part1 = "2"
                            if part1 == "": part1 = "2"
                            piece = float(part2) ** float(part1)
                        if solve.__contains__("x"):
                            solve = solve.replace("x","")
                            solve = f"{float(solve) / float(piece)}x"
                        else:
                            piece = piece.replace("x","")
                            xDivide = True
                            solve = f"{float(solve) / float(piece) }x"

                else:
                    if not piece.__contains__("*") and not piece.__contains__("/"):
                        if piece.__contains__("^"):
                            try:
                                part2, part1 = piece.split("^")
                            except:
                                part1 = "2"
                            if part1 == "": part1 = "2"
                            piece = float(part2) ** float(part1)
                        solve = str(float(piece))
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
            if solve.__contains__("x"):
                rightX.insert(x, solve)
            else:
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
        if not has_num(part):
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


def x_pemdas(equation):
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
    equation = equation.replace(")0", "p)a*0")
    equation = equation.replace(")1", "p)a*1")
    equation = equation.replace(")2", "p)a*2")
    equation = equation.replace(")3", "p)a*3")
    equation = equation.replace(")4", "p)a*4")
    equation = equation.replace(")5", "p)a*5")
    equation = equation.replace(")6", "p)a*6")
    equation = equation.replace(")7", "p)a*7")
    equation = equation.replace(")8", "p)a*8")
    equation = equation.replace(")9", "p)a*9")
    equation = equation.replace(")", "p)")
    equation = equation.replace("+a*", "+")
    equation = equation.replace("-a*", "-")
    equation = equation.replace("a*s+", "s+")
    equation = equation.replace("a*s-", "s-")
    equation = equation.replace("/a*", "/")
    equation = equation.replace("*a/", "/")
    equation = equation.replace("a*a*", "a*")
    parentheses = equation.split("(")
    for part in parentheses:
        solves = ""
        part =  part.split(")")
        x = x + 1
        for piece in part:

            if piece.__contains__("p"):
                piece = piece.replace("p", "")
                solves = solves + str(x_emdas(piece))
            else:
                solves = solves + piece
        half = half + solves

    return x_emdas(half)


def solve_x(equation):
    global xDivide
    xDivide = False
    left,right = equation.split("=")

    left, leftX = x_pemdas(left)
    right, rightX = x_pemdas(right)

    leftX = float(leftX) - float(rightX)
    right = float(right) - float(left)

    if not xDivide:
        answer = right/leftX

    else:
        answer =  leftX/right

    return f"x = {answer}"


print(solve_x("5=2/x*2"))

