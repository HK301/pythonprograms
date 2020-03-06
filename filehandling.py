f = open(r"division.py", "rb")
f1 = open(r"division2.py","wb")
for data in f:
    f1.write(data)