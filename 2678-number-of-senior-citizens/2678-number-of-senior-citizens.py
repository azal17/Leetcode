class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        
        for i in details:
            
            age= i[11:13]
            
       
            if age.isdigit():
                a = int(age)
                if a > 60:
                    cnt += 1
        
        return cnt