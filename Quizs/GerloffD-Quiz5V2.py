def reverser(num):
    reversed = 0
    while num > 0:
        digit = num % 10
        reversed = reversed * 10 + digit
        num //= 10  
    return reversed

def palindrome(num):
    for num in num_list:
        if num != reverser(num):  
            print(str(num)+ " False Palindrome")
        else:
             print(str(num)+ " True Palindrome")

num_list = [121,-121,10,0,1221,12321]
palindrome(num_list)