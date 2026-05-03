def to_decimal(number, base):
    return int(number, base)


def from_decimal(number, base):
    if base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 16:
        return hex(number)[2:]
    elif base == 10:
        return str(number)
    else:
        raise ValueError("Unsupported base")