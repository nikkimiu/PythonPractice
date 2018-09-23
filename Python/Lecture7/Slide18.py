#print(20 / 3)
#print(20 % 3)
#print (20 // 3)
def required_boxes(a,b):
    answer=a//b
    remainder=a%b
    if remainder>0:
        return answer+1
    else:
        return answer

boxes_needed1 = required_boxes (20,25)
boxes_needed2 = required_boxes (20,3)
print("1.", "Boxes:", boxes_needed1)
print("2.", "Boxes:", boxes_needed2)
