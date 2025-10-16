def reverser(num):
    reversed = 0
    while num > 0:
        digit = num % 10
        reversed = reversed * 10 + digit
        num //= 10 
    return reversed

t_list= []
f_list= []

def palindrome(num):
    for num in num_list:
        if num != reverser(num):  
            f_list.append(num)
        else:
            t_list.append(num)

num_list = [121,-121,10,0,1221,12321]
palindrome(num_list)

for num in f_list and t_list:
    if num in t_list:
        print(str(num) + " True palindrome.")
    elif num in f_list:
        print(str(num) + " False palindrome.")
    else:
        break