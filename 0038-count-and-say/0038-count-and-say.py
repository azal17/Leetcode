class Solution:
    def countAndSay(self,n: int) -> str:
        current_sequence = "1"

        for _ in range(1, n):
            next_sequence = []
            count = 1

            for i in range(1, len(current_sequence)):
                if current_sequence[i] == current_sequence[i - 1]:
                    count += 1
                else:
                  
                    next_sequence.append(str(count))
                    next_sequence.append(current_sequence[i - 1])
                    count = 1  
            next_sequence.append(str(count))
            next_sequence.append(current_sequence[-1])

            current_sequence = ''.join(next_sequence)
        
        return current_sequence

        