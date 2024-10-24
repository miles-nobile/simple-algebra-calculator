x = -1
test = "2*(2+3)/1"
test = test.replace(" ","")
test = test.replace("+","s+")
test = test.replace("-","s-")
test = test.replace("*","a*")
test = test.replace("/","a/")
symple = test.split("s")
print(symple)
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
    float()
    answer = answer + float(part)
print(answer)
