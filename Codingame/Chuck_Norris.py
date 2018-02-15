'''
Created on May 10, 2017
'''
import sys
import math


def convert(fromNum, fromBase, toBase):
    toNum = 0
    power = 0
    while fromNum > 0:
        toNum += fromBase**power * (fromNum % toBase)
        fromNum //= toBase
        power += 1
    return toNum


#message = input()
message = '%'
toCode = ""

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for l in message:
    bCode = convert(ord(l), 10, 2)  # binary code for one char
    toCode = str(toCode) + str(bCode).zfill(7)  # binary code for N chars


previous = toCode[0]
if toCode[0] == "1":
    codedMsg = "0 0"
else:
    codedMsg = "00 0"

for i in range(1, len(toCode)):
    if toCode[i] == previous:
        codedMsg = codedMsg + "0"
    elif toCode[i] == "1":
        codedMsg = codedMsg + " 0 0"
    elif toCode[i] == "0":
        codedMsg = codedMsg + " 00 0"
    previous = toCode[i]


print(codedMsg)
