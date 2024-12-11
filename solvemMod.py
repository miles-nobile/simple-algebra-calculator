

def emdas(equation):
    id = []
    symple = equation.split("ʂ")
    x = -1
    for part in symple:
        x = x + 1
        if part.__contains__("ą"):
            part = part.split("ą")
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
    equation = equation.replace("+", "ʂ+")
    equation = equation.replace("-", "ʂ-")
    equation = equation.replace("*", "ą*")
    equation = equation.replace("/", "ą/")
    equation = equation.replace("0(", "0ą*(")
    equation = equation.replace("1(", "1ą*(")
    equation = equation.replace("2(", "2ą*(")
    equation = equation.replace("3(", "3ą*(")
    equation = equation.replace("4(", "4ą*(")
    equation = equation.replace("5(", "5ą*(")
    equation = equation.replace("6(", "6ą*(")
    equation = equation.replace("7(", "7ą*(")
    equation = equation.replace("8(", "8ą*(")
    equation = equation.replace("9(", "9ą*(")
    equation = equation.replace(")0", "p)ą*0")
    equation = equation.replace(")1", "p)ą*1")
    equation = equation.replace(")2", "p)ą*2")
    equation = equation.replace(")3", "p)ą*3")
    equation = equation.replace(")4", "p)ą*4")
    equation = equation.replace(")5", "p)ą*5")
    equation = equation.replace(")6", "p)ą*6")
    equation = equation.replace(")7", "p)ą*7")
    equation = equation.replace(")8", "p)ą*8")
    equation = equation.replace(")9", "p)ą*9")
    equation = equation.replace(")", "p)")
    equation = equation.replace("+ą*", "+")
    equation = equation.replace("-ą*", "-")
    equation = equation.replace("ą*ʂ+", "ʂ+")
    equation = equation.replace("ą*ʂ-", "ʂ-")
    equation = equation.replace("/ą*", "/")
    equation = equation.replace("*ą/", "/")
    equation = equation.replace("ą*ą*", "ą*")
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

print(pemdas("1+3+(7*3)"))