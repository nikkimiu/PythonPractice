def get_discount(amount,rate):
    discount=amount*rate/100
    return discount

def get_discount_message(amount,rate):
    discount=amount*rate/100
    var1 = "% discount:$"
    return str(rate)+var1+str(discount)

def print_docket(price, rate):
    print ("Original Price","$", price)
    answer1=get_discount_message(price,rate)
    print (answer1)
    answer2=get_discount(price,rate)
    print("Price ", "$", price-answer2)

print_docket(657,15)    