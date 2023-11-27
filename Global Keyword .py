a=5
def globalvaluechange():
     global a
     a=10
print("before call a=;",a)
globalvaluechange()
print("after call a=",a)

