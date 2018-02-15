'''
Created on May 12, 2017
'''
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mimeDict = {}

for i in range(n):
    ext, mt = input().split()
    # store input in a dictionary with lowercase for extension
    mimeDict[ext.lower()] = mt

for i in range(q):
    fname = input().lower()  # get the file name in lowercase

    if fname.rfind(".") >= 0:
        # get the ext from the filename
        s = fname[fname.rfind(".") + 1:len(fname)]
        if s in mimeDict:
            print(mimeDict[s])  # return the MIME type
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
