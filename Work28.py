a = int(input())
b = int(input())
 
 
def res_sum(a, b):
    if b == 0:
        return a
    return res_sum(a+1, b-1)
 
 
print(res_sum(a, b))