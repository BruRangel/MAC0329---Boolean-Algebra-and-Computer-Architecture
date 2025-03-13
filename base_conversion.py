def base_b_para_10(num: int, b: int):
    aux = num
    res = 0
    index = 0
    while aux > 0:
        #print(aux)
        res += (aux % 10) * pow(b, index)
        #print(res)
        index += 1
        #print(index)
        aux //= 10
    return res

num = 1011
base = 2
print(f"A conversao do num {num} na base {base} para base 10 eh: {base_b_para_10(num, base)}")

def base_10_para_b(num: int, b: int):
    aux = num
    res = 0
    index = 0
    while aux > 0:
        res += (aux % b) * pow(10, index)
        index += 1
        aux //= b
    return res

num = 107
base = 2
print(f"A conversao do num {num} na base 10 para base {base} eh: {base_10_para_b(num, base)}")

def base_a_para_b(num: int, a: int, b: int):
    aux = num
    res = 0
    index = 0
    while aux > 0:
        res += (aux % b) * pow(a, index)
        index += 1
        aux //= b
    return res

num = 107
base_o = 10
base_d = 2
print(f"A conversao do num {num} na base {base_o} para base {base_d} eh: {base_a_para_b(num, base_o, base_d)}")
