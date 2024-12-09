x = -1
test = "2(+2)+2"
test = test.replace(" ","")
test = test.replace("+","s+")
test = test.replace("-","s-")
test = test.replace("*","a*")
test = test.replace("/","a/")
test = test.replace("(","a*(")
test = test.replace(")","p)a*")
test = test.replace("+a*","+")
test = test.replace("-a*","-")
test = test.replace("a*s+","s+")
test = test.replace("a*s-","s-")
test = test.replace("/a*","/")
test = test.replace("a*a/","a/")
test = test.replace("*a*","a*")
print(test)
test1 = test.split("(")
test2 = []
y = -1
for test3 in test1:
    test2.extend(test3.split(")"))

print(test2)

symple = test.split("s")

print(symple)
print()
id = []
solve = 1.0
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
        id.insert(x,part)
print(id)
answer = 0
for part in id:
    answer = answer + float(part)
print(answer)

def pemdas(equation):
    x = -1
    id = []
    equation = equation.replace(" ", "")
    equation = equation.replace("+", "s+")
    equation = equation.replace("-", "s-")
    equation = equation.replace("*", "a*")
    equation = equation.replace("/", "a/")

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