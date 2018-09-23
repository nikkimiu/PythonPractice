def find_number_of_boxes(total):
    answer=total//10
    remainder=total%10
    if remainder>0:
        return answer+1
    else:
        return answer

def calculate_cost(boxes):
    if boxes>=6:
        cost=6*8+(boxes-6)*5
        return cost
    else:
        cost=boxes*8
        return cost

items=input("number of items ")
result1=find_number_of_boxes(int(items))
result2=calculate_cost(result1)
print(result2)
