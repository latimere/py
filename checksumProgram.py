print("enter provided download source checksum")
sourceCheckSum = input()
print("enter validation checksum")
validationCheckSum = input()
if sourceCheckSum == validationCheckSum:
    print("valid")
else:
    print("invalid")
