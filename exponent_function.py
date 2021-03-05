def expo(base, exponent):
    res=1
    for i in range(exponent):
        res*=base
    return res

#inbuilt exponent
print(2**3)
print(expo(3,4))