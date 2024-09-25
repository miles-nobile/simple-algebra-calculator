

def pairSort(pair = "0,0",pair1 = "0,0"):
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
        test()
        pairSuccess = False

def slopeFind(rize = 0 ,run = 1):
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
        test()
    except:
        print("Please type in valid rize and run like rize = 2 and run = 1")
        test()
        success = False






def test():
    # used so the calculations aren't repeated
    global pairSuccess
    global success
    success = False
    pairSuccess = False

    # gets info
    pair = input("Point = ")
    pairSort(pair)

    if pairSuccess:
        rize = input("Rize = ")
        run = input("Run = ")
        slopeFind(rize,run)

    if pairSuccess and success:
        print(f"x = {x} y = {y}")

    pairSuccess = True

test()




