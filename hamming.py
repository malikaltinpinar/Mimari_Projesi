def is_power_of_two(n):
    return n != 0 and (n & (n - 1)) == 0

def calculate_parity_positions(data_length):
    r = 0
    while (2 ** r) < (data_length + r + 1):
        r += 1
    return r

def insert_parity_bits(data):
    r = calculate_parity_positions(len(data))
    j = 0
    k = 1
    result = ''
    for i in range(1, len(data) + r + 1):
        if is_power_of_two(i):
            result += '0'
        else:
            result += data[j]
            j += 1
    return result, r

def calculate_parity_bits(encoded, r):
    n = len(encoded)
    encoded = list(encoded)
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & pos and j != pos:
                parity ^= int(encoded[j - 1])
        encoded[pos - 1] = str(parity)
    return ''.join(encoded)

def generate_hamming_code(data):
    encoded, r = insert_parity_bits(data)
    encoded = calculate_parity_bits(encoded, r)
    return encoded

def introduce_error(codeword, position):
    if position < 1 or position > len(codeword):
        raise ValueError("Pozisyon geçersiz!")
    codeword = list(codeword)
    codeword[position - 1] = '1' if codeword[position - 1] == '0' else '0'
    return ''.join(codeword)

def calculate_syndrome(codeword):
    n = len(codeword)
    r = calculate_parity_positions(n)
    syndrome = 0
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & pos:
                parity ^= int(codeword[j - 1])
        if parity:
            syndrome += pos
    return syndrome

def correct_error(codeword, syndrome):
    if syndrome == 0:
        return codeword
    codeword = list(codeword)
    index = syndrome - 1
    codeword[index] = '1' if codeword[index] == '0' else '0'
    return ''.join(codeword)
