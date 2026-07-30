from typing import List


class vector:
    def __init__(self, vec: List) -> None:
        vec = self.vec
        n = len(vec)

    def scaler_addition(v, k):
        return i + k for i in v 


    def dot_product(v,k):
        if len(v)!=len(k):
            raise ValueError("Error: Length of the vectors should be the same")
        dot=0
        for i in range(len(v)):
            dot+=v[i]*k[i]
        return dot
    def cross_product(v,k):
        if len(v) !=3 or len(k) !=3 :
             raise ValueError("Error: The length of the vectors shoule be 3")
        if  type(v)!=list or type(k)!=list:
            raise ValueError("Error: The type is not list")
        prod=[]
        for i in range(3):
            if i==0:
                prod.append((v[1]*k[2])-(v[2]*k[1]))            
        
            elif i==1:
                prod.append((v[2]*k[0])-(v[0]*k[2]))
            else :
                 prod.append((v[0]*k[1])-(v[1]*k[0]))
        return prod


    
