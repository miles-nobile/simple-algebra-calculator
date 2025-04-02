from fractions import Fraction

global solved, color


def print_num(num):
    num = float(num)
    if num.is_integer():
        return int(num)
    else:
        return Fraction(num).limit_denominator()


def find_slope_from_point_equation():
    global slope
    global printSlope
    global rize
    global run
    rize = y1 - y
    run = x1 - x
    slope = rize / run
    if not slope.is_integer():
        printSlope = Fraction(slope).limit_denominator()


def standard_equation(a, b, c):
    global solved
    if b > 0:
        solved = f"{a}x +{b}y = {c}"
    elif b < 0:
        solved =f"{a}x {b}y = {c}"


def point_slope_equation(slope, yIntercept, equals="y"):
    global solved
    if yIntercept > 0 and slope.is_integer() and yIntercept.is_integer():
        solved = f"{equals} = {int(slope)}x +{int(yIntercept)}"
    elif yIntercept == 0.0 and slope.is_integer():
        solved = f"{equals} = {int(slope)}x"
    elif yIntercept < 0.0 and slope.is_integer() and yIntercept.is_integer():
        solved = f"{equals} = {int(slope)}x {int(yIntercept)}"
    elif yIntercept > 0 and not slope.is_integer() and yIntercept.is_integer():
        solved = f"{equals} = {Fraction(slope).limit_denominator()}x +{int(yIntercept)}"
    elif yIntercept == 0.0 and not slope.is_integer():
        solved = f"{equals} = {Fraction(slope).limit_denominator()}x"
    elif yIntercept < 0.0 and not slope.is_integer() and yIntercept.is_integer():
        solved = f"{equals} = {Fraction(slope).limit_denominator()}x {int(yIntercept)}"
    elif yIntercept > 0 and not slope.is_integer() and not yIntercept.is_integer():
        solved = f"{equals} = {Fraction(slope).limit_denominator()}x +{Fraction(yIntercept).limit_denominator()}"
    elif yIntercept < 0.0 and not slope.is_integer() and not yIntercept.is_integer():
        solved = f"{equals} = {Fraction(slope).limit_denominator()}x {Fraction(yIntercept).limit_denominator()}"


def x_to_y_converter(programNumber=1, slope1=0.0, yIntercept1=0.0, ):
    global fOfx
    run = True
    print("Type stop to exit\n")
    if programNumber == 1:
        fOfxIn = input("f(x) = ")
    while run:
        try:
            xIn = input("x = ")
            if xIn == "stop":
                run = False
                programNumber = 0

            else:
                xIn = float(xIn)

            if programNumber == 0:
                print("good bye!")
                run = False

            if programNumber == 1:
                fOfx = fOfx.replace(" ", "")
                slope, yIntercept = fOfx.split("x")
                if slope == "":
                    slope = "1"
                if yIntercept == "":
                    yIntercept = "0"
                yIntercept = float(yIntercept)
                slope = float(slope)
                print("test")
                print(f"y = {(slope * xIn) + yIntercept}")

            if programNumber == 2:
                print(f"y = {(slope1 * xIn) + yIntercept1}")


        except:
            print("test")


def pair_sort(pair="0,0", programNumber=0, pair1="0,0"):
    global x
    global y
    global x1
    global y1
    global pairSuccess

    pairReplace = pair.replace("(", "")
    pairReplace = pairReplace.replace(")", "")
    pairReplace = pairReplace.replace(" ", "")
    x, y = pairReplace.split(",")
    x = float(x)
    y = float(y)

    pairReplace = pair1.replace("(", "")
    pairReplace = pairReplace.replace(")", "")
    pairReplace = pairReplace.replace(" ", "")
    x1, y1 = pairReplace.split(",")
    x1 = float(x1)
    y1 = float(y1)
    pairSuccess = True


def slope_find(rize="0", run="1"):
    global slope
    global success
    try:
        rize = float(rize)
        run = float(run)
        slope = rize / run
        success = True
    except ZeroDivisionError:
        print("run can't be 0")
        success = False
        point_slope_to_slope_intercept()
    except:
        print("Please type in valid rize and run like rize = 2 and run = 1")
        point_slope_to_slope_intercept()
        success = False


def transformation_equation(gOfx, fOfx):
    global slope
    global yIntercept
    global transformationSuccess

    gOfx = gOfx.replace(" ", "")
    gOfx = gOfx.replace("(", "")
    gOfx = gOfx.replace("x", "")
    gOfx = gOfx.replace("f", "")
    parenthesesIn, parenthesesOut = gOfx.split(")")
    if parenthesesIn.__contains__("/"):
        parenthesesIn = Fraction(parenthesesIn).numerator / Fraction(parenthesesIn).limit_denominator().denominator
    if parenthesesOut.__contains__("/"):
        parenthesesOut = Fraction(parenthesesOut).numerator / Fraction(
                parenthesesOut).limit_denominator().denominator

    fOfx = fOfx.replace(" ", "")
    slope, yIntercept = fOfx.split("x")
    if slope == "":
        slope = "1"
    if slope.__contains__("/"):
        slope = Fraction(slope).numerator / Fraction(slope).limit_denominator().denominator

    if yIntercept == "":
        yIntercept = "0"
    if yIntercept.__contains__("/"):
        yIntercept = Fraction(yIntercept).numerator / Fraction(yIntercept).limit_denominator().denominator

    yIntercept = float(yIntercept)
    slope = float(slope)

    if parenthesesIn.startswith("+") or parenthesesIn.startswith("-"):
        amount = float(parenthesesIn)
        yIntercept = (slope * amount) + yIntercept
        point_slope_equation(slope, yIntercept, "g(x)")

    elif parenthesesOut.startswith("+") or parenthesesOut.startswith("-"):
        amount = float(parenthesesOut)
        yIntercept = amount + yIntercept
        point_slope_equation(slope, yIntercept, "g(x)")

    elif parenthesesIn.startswith("*"):
        parenthesesIn = parenthesesIn.replace("*", "")
        amount = float(parenthesesIn)
        slope = slope * amount
        point_slope_equation(slope, yIntercept, "g(x)")

    elif parenthesesOut.startswith("*"):
        parenthesesOut = parenthesesOut.replace("*", "")
        amount = float(parenthesesOut)
        slope = slope * amount
        yIntercept = yIntercept * amount
        point_slope_equation(slope, yIntercept, "g(x)")


def point_slope_to_slope_intercept(pair, slope_in):
    # used so the calculations aren't repeated
    global pairSuccess
    global success
    global solved
    global color
    color ="grey"
    success = False
    pairSuccess = False
    try:
        pair_sort(pair, 1)
    except:
        color = "red"
        solved = "Please type in a\n valid ordered pair"
        return
    try:
        slope = Fraction(slope_in).limit_denominator()
        slope = slope.numerator/slope.denominator
    except:
        color = "red"
        solved = "Please type in a\n valid slope"

        return


    yIntercept = (-x * slope) + y
    point_slope_equation(slope, yIntercept)


def find_slope_from_point(point, point1):
    global pairSuccess
    global solved
    global color
    color = "grey"
    pairSuccess = False
    try:
        pair_sort(point, 2, point1, )
    except:
        color = "red"
        solved = "Please type in\n valid ordered pairs"
        return
    try:
        find_slope_from_point_equation()
    except:
        solved = "The slope is undefined"
        return
    yIntercept = (-x * slope) + y
    point_slope_equation(slope, yIntercept)


def transformation(f_ofx, g_ofx):
    global color, solved
    color = ("grey")
    try:
        transformation_equation(g_ofx, f_ofx)
    except:
        color = "red"
        solved = f"Please type in valid\n slope intercept equations"
        return


def standard_to_slope_intercept(equation):
    global color, solved
    color = "grey"
    try:
        equation = equation.replace(" ", "")
        equation = equation.replace("y", "")
        left, right = equation.split("=")
        x, y = left.split("x")
        if right == "":
            var = right == 0.0

        y = float(y)
        yIntercept = float(right) / y
        slope = -float(x) / y
        point_slope_equation(slope, yIntercept)

    except:
        color = "red"
        solved = f"Please type in a\n valid standard equation"
        return


def slope_intercept_to_standard(equation):
    global color, solved
    color = "grey"
    try:
        equation = equation.replace(" ", "")
        x, yIntercept = equation.split("x")
        if yIntercept == "":
            var = yIntercept == 0.0
        elif yIntercept.__contains__("/"):
            yIntercept = Fraction(yIntercept).numerator / Fraction(yIntercept).limit_denominator().denominator
        else:
            yIntercept = float(yIntercept)
        y = 1.0

        if x.__contains__("/"):
            x = Fraction(x).numerator / Fraction(x).limit_denominator().denominator

        x = -float(x)
        if not x.is_integer():
            fraction = Fraction(x)
            x = fraction.limit_denominator().denominator * x
            y = fraction.limit_denominator().denominator * y
            yIntercept = fraction.limit_denominator().denominator * yIntercept

        if not yIntercept.is_integer():
            fraction = Fraction(yIntercept)
            x = fraction.limit_denominator().denominator * x
            y = fraction.limit_denominator().denominator * y
            yIntercept = fraction.limit_denominator().denominator * yIntercept
        if x < 0:
            x = -x
            y = -y
            yIntercept = -yIntercept
        standard_equation(x, y, yIntercept)

    except:
        color = "red"
        solved = f"Please type in a valid\n slope intercept equation"
        return


def intercept_find(f_ofx):
    global color, solved
    color = "grey"
    y = ""
    try:
        f_ofx = f_ofx.lower()
        f_ofx = f_ofx.replace(" ", "")
        f_ofx = f_ofx.replace("f(x)=", "")
        x, y = f_ofx.split("x")

        if y == "": y = 0.0
        else:
            y = Fraction(y).numerator/Fraction(y).limit_denominator().denominator
        x = Fraction(x).numerator / Fraction(x).limit_denominator().denominator
    except:
        color = "red"
        solved = f"Please type in a valid\n slope intercept equation"
        return

    solved = f"y intercept: {print_num(y)}\nx intercept: {print_num(y / -x)}"


def emdas(equation):
    id = []
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
            id.insert(x, part)
    answer = 0
    for part in id:
        if part == "": part = "0"
        if str(part).__contains__("^"):
            try:
                part2, part1 = part.split("^")
            except:
                part1 = "2"
            if part1 == "": part1 = "2"
            part = float(part2) ** float(part1)
        answer = answer + float(part)
    return answer


def pemdas(equation):
    global color, solved
    try:
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
                    solves = solves + str(emdas(piece))
                else:
                    solves = solves + piece
            half = half + solves
        color ="grey"
        solved = str(emdas(half))
    except:
        color ="red"
        solved = "Please type in a valid\n pemdas equation"




def hasNum(string):
    for part in string[:]:
        part = str(part)
        if part.isdigit(): return True
    return False


def x_emdas(equation):
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


def x_pemdas(equation):
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
                parentheseslist = x_emdas(piece)
                solves = solves + f"{float(parentheseslist[0]) * distributelist1[timesrun]}" + f"s+{parentheseslist[1] * distributelist1[timesrun]}x"
                solves =solves.replace("+-","-")
                timesrun = timesrun + 1
            else:
                solves = solves + piece
        half = half + solves

    return x_emdas(half)


def solve_x(equation):
    global color, solved
    try:
        left,right = equation.split("=")

        left, leftX = x_pemdas(left)
        right, rightX = x_pemdas(right)

        leftX = float(leftX) - float(rightX)
        right = float(right) - float(left)

        answer = right/leftX

        color = "grey"
        solved = f"x = {answer}"

    except:
        color = "red"
        solved = "Please type in a valid\n equation"



