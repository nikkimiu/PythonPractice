def get_result1(a,b,c):
    sum=a+b+c
    largest=max(a,b,c)
    smallest=min(a,b,c)
    middle=sum-largest-smallest
    answer=largest+middle
    return answer
    
print("1.", get_result1(1, 2, 3))
print("2.", get_result1(11,12,3))
print("3.", get_result1(6,2,5))
