def evenodd(n) :

    if n ^ 1 == n + 1 :
        return True
    
    else : 
        return False
    
n = int(input("Enter a number"))

if evenodd(n):
    print(n , "is Even")

else :
    print(n , "is  Odd")