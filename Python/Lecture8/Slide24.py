def get_discount_message(amount,rate):
    discount=amount*rate/100
    var1 = "% discount:$"
    return str(rate)+var1+str(discount)
answer=get_discount_message(25,10)
print (answer)

