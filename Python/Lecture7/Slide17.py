def get_result3(a):
    length=len(a)
    firstword=a[0]
    lastword=a[length-1]
    return (lastword+firstword).upper()
print ("1", get_result3( "Crudivore"))
