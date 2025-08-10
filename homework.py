
def eo() :

    n1 = 192
    n2 = 72

    if n1 ^ 1 == n1 + 1 :
        print("even")
        if (n1 & n2) :
            print(n1 ^ n2 )
            return True
    
    else :
        print("odd")
        print(n1 | n2)
        return False
    
eo()