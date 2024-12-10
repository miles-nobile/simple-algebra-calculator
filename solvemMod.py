

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

    return str(emdas(half))

print(pemdas(input("Equation:\n")))