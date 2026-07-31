from typing import List

VectorType = List[float]

class Vector:
    def __init__(self, vec: VectorType) -> None:
        self.vec = vec
        self.n = len(self.vec)

    def scaler_addition(self, k: int | float) -> VectorType:
        """adds a scalar value `k` to each
        of the element of the vector"""
        return [i + k for i in self.vec]

    def dot_product(self, w: VectorType) -> float:
        """calculates the dot product
        `self.vec` and vector `w`"""
        assert len(self.vec) == len(w), "vectors should be in same length"
        return sum([i * j for i, j in zip(self.vec, w)])

    """
        
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
    """

# btw @wali we were doing it wrong so like i was not really like thinking while i started making it
# so can u see the formate i wrote it rn, like read it carefully how i am using self and vec and 
# how i am making the function, dont wory about the types (that is: VectorType and like hintings)
# and dont wory about the docstrings
# try to like refactor the `cross_produckt()` like how i did uppar pe 
# thankyou and sorry


    
