class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        new = n
        if new <0:
            new = -1*n
        while new:
            if new%2: #true for odd , 0 for even
                result = result * x
                new = new -1 
            else:
                x = x*x
                new = new//2
        if n<0:
            result = 1.0/result
        return result