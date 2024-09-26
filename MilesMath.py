from fractions import Fraction

def findSlopeFromPointEquation():
    global Slope
    global printSlope
    global rize
    global run
    rize = y1-y
    run = x1-x
    Slope = rize / run
    if not Slope.is_integer():
        printSlope = Fraction(Slope)


def pointSlopeEquation():
    yIntercept = (-x * slope) + y
    if (-x*slope)+y > 0 and slope.is_integer() and yIntercept.is_integer():
        print(f"y = {int(slope)}x +{int((-x * slope) + y)}")
    elif (-x*slope)+y == 0.0 and slope.is_integer():
        print(f"y = {int(slope)}x")
    elif (-x*slope)+y < 0.0 and slope.is_integer() and yIntercept.is_integer():
        print(f"y = {int(slope)}x {int((-x * slope) + y)}")
    elif (-x*slope)+y > 0 and not slope.is_integer() and yIntercept.is_integer():
        print(f"y = {Fraction(slope)}x +{int((-x * slope) + y)}")
    elif (-x*slope)+y == 0.0 and not slope.is_integer():
        print(f"y = {Fraction(slope)}x")
    elif (-x*slope)+y < 0.0 and not slope.is_integer() and yIntercept.is_integer():
        print(f"y = {Fraction(slope)}x {int((-x * slope) + y)}")
    elif (-x*slope)+y > 0 and not slope.is_integer() and not yIntercept.is_integer():
        print(f"y = {Fraction(slope)}x +{Fraction((-x * slope) + y)}")
    elif (-x*slope)+y < 0.0 and not slope.is_integer() and not yIntercept.is_integer():
        print(f"y = {Fraction(slope)}x {Fraction((-x * slope) + y)}")

def pairSort(pair = "0,0", programNumber = 0, pair1 = "0,0"):
    global x
    global y
    global x1
    global y1
    global pairSuccess
    try:
        pairReplace = pair.replace("(", "")
        pairReplace = pairReplace.replace(")", "")
        pairReplace = pairReplace.replace(" ", "")
        x,y = pairReplace.split(",")
        x = float(x)
        y = float(y)

        pairReplace = pair1.replace("(", "")
        pairReplace = pairReplace.replace(")", "")
        pairReplace = pairReplace.replace(" ", "")
        x1,y1 = pairReplace.split(",")
        x1 = float(x1)
        y1 = float(y1)
        pairSuccess = True

    except:
        print("Please type in valid ordered pairs like (2,8) or -4,0")
        if programNumber == 1:
            pointSlopeToSlopeIntercept()
        if programNumber == 2:
            findSlopeFromPoint()
        pairSuccess = False


def slopeFind(rize = "0" ,run = "1"):
    global slope
    global success
    try:
        rize = float(rize)
        run = float(run)
        slope = rize/run
        success = True
    except ZeroDivisionError:
        print("run can't be 0")
        success = False
        pointSlopeToSlopeIntercept()
    except:
        print("Please type in valid rize and run like rize = 2 and run = 1")
        pointSlopeToSlopeIntercept()
        success = False


def transformationEquation(gOfx,fOfx):
    global slope
    global yIntercept1
    try:
        gOfx = gOfx.replace(" ", "")
        gOfx = gOfx.replace("(", "")
        gOfx = gOfx.replace("x", "")
        gOfx = gOfx.replace("f", "")
        parenthesesIn, parenthesesOut = gOfx.split(")")

        fOfx = fOfx.replace(" ","")
        fOfx = fOfx.replace("+","")
        slope, yIntercept1 = fOfx.split("x")
        yIntercept1 = float(yIntercept1)
        slope = float(slope)
        if parenthesesIn.startswith("+"):
            amount = parenthesesIn.replace("+","")
            amount = float(amount)
            print(f"g(x) = {slope}x +{(slope * amount) + yIntercept1}")
        elif parenthesesIn.startswith("*"):
            print("change slope x")
        elif parenthesesIn.startswith("-"):
            print("right")
        elif parenthesesOut.startswith("+"):
            print("up")
        elif parenthesesOut.startswith("*"):
            print("change slope y")
        elif parenthesesOut.startswith("-"):
            print("down")
    except:
        print("test")


def pointSlopeToSlopeIntercept():
    # used so the calculations aren't repeated
    global pairSuccess
    global success
    success = False
    pairSuccess = False

    pair = input("Point = ")
    pairSort(pair,1)

    if pairSuccess:
        rize = input("Rize = ")
        run = input("Run = ")
        slopeFind(rize,run,)

    if pairSuccess and success:
        pointSlopeEquation()

    pairSuccess = True

def findSlopeFromPoint():
    global pairSuccess
    pairSuccess = False
    point = input("First point = ")
    point1 = input("Second point = ")
    pairSort(point,2, point1,)

    if pairSuccess:
        findSlopeFromPointEquation()
        print(f"The slope is {Slope}")
        if input("would you like to solve for slope intercept (yes/no): ") == "yes":
            slopeFind(rize,run)
            pointSlopeEquation()

def transformation():

    fOfx =input("f(x) = ")
    gOfx = input("g(x) = ")
    transformationEquation(gOfx,fOfx)
    print()

transformation()

