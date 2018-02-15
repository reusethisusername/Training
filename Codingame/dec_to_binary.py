'''
Created on May 10, 2017
'''

# function to convert Decimal to Binary

# Binary to Decimal conversion

#
# def binToDec(binNum):
#     decNum = 0
#     power = 0
#     while binNum > 0:
#         decNum += 2**power * (binNUm % 10)
#         binNUm //= 10
#         power += 1
#     return decNum
#
# # Decimal to Binary conversion
#
#
# def DecToBin(decNum):
#     binNum = 0
#     power = 0
#     while decNum > 0:
#         binNum += 10**power * (decNUm % 2)
#         decNUm //= 2
#         power += 1
#     return binNum

# Generic conversion


def convert(fromNum, fromBase, toBase):
    toNum = 0
    power = 0
    while fromNum > 0:
        toNum += fromBase**power * (fromNum % toBase)
        fromNum //= toBase
        power += 1
    return toNum


print(str(convert(111, 2, 10)))
