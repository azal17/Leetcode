
class Solution:
    def minimumPushes(self, word: str) -> int:
       
        result = 0
        count = 0
 
        frequency = [0] * 26
        for char in word:
            frequency[ord(char) - ord('a')] += 1



        frequency.sort(reverse=True)
        for freq in frequency:
            if freq > 0:
                result += freq * (count // 8 + 1)
                count += 1
        
        return result


