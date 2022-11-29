# Implementation of Towers of Hanoi using Python in Recursive pattern

def Towers_of_Hanoi(n, a , b , c):
    if n >= 1:
        Towers_of_Hanoi(n-1 , a , c , b)
        print("Move Top Disk from tower" , a , "to top of tower" , b)
        Towers_of_Hanoi(n-1 , c , b , a)

Towers_of_Hanoi(3 , 1 , 2 , 3)


