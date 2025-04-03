from functools import reduce

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

print(list(factors(20)))
def factor_trinomials(equation,equation1):
    factor_list = list(factors(equation))
    while len(factor_list) >= 1:
        if float(equation1) == float(factor_list[0])+ float(factor_list[-1]):
            return f"{factor_list[0]}, {factor_list[-1]}"
        else:
            pass


print(factor_trinomials(12,13))