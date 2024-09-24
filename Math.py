

def pairSort(pair = "0,0",pair1 = "0,0"):
    global x
    global y
    global x1
    global y1
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

    except:
        print("Please type in valid ordered pairs like (2,8) or -4,0")
        test()
        success = False


def test():
    # used so the calculations aren't repeated
    global success
    success = True
    # gets info
    pair = input("Point = ")
    rize = input("Rize = ")
    run = input("Run = ")

    pairSort(pair)

    if success:
        print(f"x = {x} y = {y}")
    success = True

test()




