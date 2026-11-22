x = '4.5'

d = x.isdigit()
n = x.isnumeric()
dec = x.isdecimal()

print(d)
print(n)
print(dec)


def is_float(numero: str) -> bool:
    try:
        float(numero)
        return True
    except:
        return False


f = is_float(x)
print(f)
