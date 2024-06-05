def sum_of_powers(num:int)->int:
    total=0
    while num>0:
        digit=num%10
        total+=digit**2
        num=num//10
    return total
def is_happy(num:int)->bool:
    i=0
    while i<200:
        if num==1:
            return True
        sum=sum_of_powers(num)
        i+=1
    return False