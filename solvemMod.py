def pemdas(equation):
    x = -1
    id = []
    equation = equation.replace(" ", "")
    equation = equation.replace("+", "s+")
    equation = equation.replace("-", "s-")
    equation = equation.replace("*", "a*")
    equation = equation.replace("/", "a/")
    equation = equation.replace("(", "a*(")
    equation = equation.replace(")", "p)a*")
    equation = equation.replace("+a*", "+")
    equation = equation.replace("-a*", "-")
    equation = equation.replace("a*s+", "s+")
    equation = equation.replace("a*s-", "s-")
    equation = equation.replace("/a*", "/")
    equation = equation.replace("a*a/", "a/")
    equation = equation.replace("*a*", "a*")
    perthases = equation.split("(")
    for 

    symple = equation.split("s")

    for part in symple:
        x = x + 1
        if part.__contains__("a"):
            part = part.split("a")
            for piece in part:
                if not piece.__contains__("*") and not piece.__contains__("/"):
                    solve = float(piece)
                elif piece.__contains__("*"):
                    piece = piece.replace("*", "")
                    solve = solve * float(piece)
                elif piece.__contains__("/"):
                    piece = piece.replace("/", "")
                    solve = solve / float(piece)
            id.insert(x, solve)
        else:
            id.insert(x, part)
    print(id)
    answer = 0
    for part in id:
        float()
        answer = answer + float(part)
    return answer

print(pemdas("2+2+2"))