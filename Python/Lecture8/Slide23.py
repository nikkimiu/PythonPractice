def get_discount(amount,rate):
    discount=amount*rate/100
    return discount
answer=get_discount(25,10)
print ('%.2f' % answer)
