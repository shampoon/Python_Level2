from collections import defaultdict
s1 = 'A2'
s2 = 'C4F'
dec_to_hex = {0: '0', 1: '1', 2: '2',  3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
              12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11
              , 'C': 12, 'D': 13, 'E': 14, 'F': 15}


class hex_nums():
    def __init__(self, hex_num):
        self.hex_num = hex_num

    def unpack(num1, num2):
        dec_val = defaultdict(int)
        i = 1
        for char in num1[::-1]:
            dec_val[1] += hex_to_dec[char] * 16 ** (i - 1)
            i += 1
        i = 1
        for char in num2[::-1]:
            dec_val[2] += hex_to_dec[char] * 16 ** (i - 1)
            i += 1
        return dec_val[1], dec_val[2]

    def pack(num):
        if num < 16:
            return dec_to_hex[num]
        else:
            remainder = num % 16
            res = hex_nums.pack(num // 16) + dec_to_hex[remainder]
            return res

    def __add__(self, other):
        n1, n2 = hex_nums.unpack(self.hex_num, other.hex_num)
        return hex_nums.pack(n1 + n2)

    def __mul__(self, other):
        n1, n2 = hex_nums.unpack(self.hex_num, other.hex_num)
        return hex_nums.pack(n1 * n2)


hex = hex_nums(s1)
hex2 = hex_nums(s2)
print(hex + hex2)
print(hex * hex2)
