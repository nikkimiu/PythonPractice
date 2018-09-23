def get_result2(a,b):
    firstword=len(a)
    secondword=len(b)
    if firstword>secondword:
        return firstword
    else:
        return secondword
print("1.", get_result2("Mollycoddle","cat"))
print("1.", get_result2("yishan","charlotte"))
print("1.", get_result2("","1"))