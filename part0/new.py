import string

def convert_base(num, from_base=10, to_base=10):
    n = int(str(num), from_base)
    alphabet = string.digits + string.ascii_uppercase
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]

print(convert_base(num=273, from_base=10, to_base=16))
print(convert_base(num=273, from_base=10, to_base=2))
