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
        printSlope = Fraction(Slope).limit_denominator()


def pointSlopeEquation(slope, yIntercept, equals ="y"):
    if yIntercept > 0 and slope.is_integer() and yIntercept.is_integer():
        print(f"{equals} = {int(slope)}x +{int(yIntercept)}")
    elif yIntercept == 0.0 and slope.is_integer():
        print(f"{equals} = {int(slope)}x")
    elif yIntercept < 0.0 and slope.is_integer() and yIntercept.is_integer():
        print(f"{equals} = {int(slope)}x {int(yIntercept)}")
    elif yIntercept > 0 and not slope.is_integer() and yIntercept.is_integer():
        print(f"{equals} = {Fraction(slope).limit_denominator()}x +{int(yIntercept)}")
    elif yIntercept == 0.0 and not slope.is_integer():
        print(f"{equals} = {Fraction(slope).limit_denominator()}x")
    elif yIntercept < 0.0 and not slope.is_integer() and yIntercept.is_integer():
        print(f"{equals} = {Fraction(slope).limit_denominator()}x {int(yIntercept)}")
    elif yIntercept > 0 and not slope.is_integer() and not yIntercept.is_integer():
        print(f"{equals} = {Fraction(slope).limit_denominator()}x +{Fraction(yIntercept).limit_denominator()}")
    elif yIntercept < 0.0 and not slope.is_integer() and not yIntercept.is_integer():
        print(f"{equals} = {Fraction(slope).limit_denominator()}x {Fraction(yIntercept).limit_denominator()}")


def xToYConverter(programNumber = 1,slope1=0.0,yIntercept1=0.0,):
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

            if programNumber ==0:
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
                print(f"y = {(slope*xIn)+yIntercept}")

            if programNumber == 2:
                print(f"y = {(slope1*xIn)+yIntercept1}")


        except:
            print("test")


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
    global yIntercept
    global transformationSuccess
    try:
        gOfx = gOfx.replace(" ", "")
        gOfx = gOfx.replace("(", "")
        gOfx = gOfx.replace("x", "")
        gOfx = gOfx.replace("f", "")
        parenthesesIn, parenthesesOut = gOfx.split(")")

        fOfx = fOfx.replace(" ","")
        slope, yIntercept = fOfx.split("x")
        if slope == "":
            slope = "1"
        if yIntercept == "":
            yIntercept = "0"
        yIntercept = float(yIntercept)
        slope = float(slope)

        if parenthesesIn.startswith("+") or parenthesesIn.startswith("-"):
            amount = float(parenthesesIn)
            yIntercept = (slope * amount) + yIntercept
            pointSlopeEquation(slope, yIntercept, "g(x)")

        elif parenthesesOut.startswith("+") or parenthesesOut.startswith("-"):
            amount = float(parenthesesOut)
            yIntercept = amount + yIntercept
            pointSlopeEquation(slope, yIntercept, "g(x)")

        elif parenthesesIn.startswith("*"):
            parenthesesIn = parenthesesIn.replace("*", "")
            amount = float(parenthesesIn)
            slope = slope * amount
            pointSlopeEquation(slope, yIntercept, "g(x)")

        elif parenthesesOut.startswith("*"):
            parenthesesOut = parenthesesOut.replace("*","")
            amount = float(parenthesesOut)
            slope = slope * amount
            yIntercept = yIntercept * amount
            pointSlopeEquation(slope, yIntercept, "g(x)")
        
        transformationSuccess = True
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
        yIntercept = (-x * slope) + y
        pointSlopeEquation(slope, yIntercept)

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
    global transformationSuccess
    transformationSuccess = False
    
    fOfx =input("f(x) = ")
    gOfx = input("g(x) = ")
    transformationEquation(gOfx,fOfx)
    if transformationSuccess and input("Would you like to use x to y converter(yes/no): ") == "yes":
        xToYConverter(2, slope, yIntercept)


def standardToSlopeIntercept():
    equation = input("Equation in standard form: ")
    try:
        equation =equation.replace(" ","")
        equation =equation.replace("y","")
        left,right = equation.split("=")
        x,y = left.split("x")
        y = float(y)
        yIntercept = float(right)/y
        slope = -float(x)/y
        pointSlopeEquation(slope, yIntercept)

    except:
        print("test")

