
class Solution:
    def naive_string_matching(self, text: str, pattern: str) -> bool:
        n = len(text)
        m = len(pattern)
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break 
                    
            if match: 
                return True
        return False  

    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()  
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and len(words[j]) <= len(words[i]):  
                    if self.naive_string_matching(words[i], words[j]):
                        substrings.add(words[j]) 
        return list(substrings) 