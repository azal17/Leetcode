class Solution:
    def kmps(self,pattern: str):
        m = len(pattern)

        kmp = [0]*m

        i = 1
        length = 0
        while i<m:
            if pattern[i] == pattern[length]:
                length +=1
                kmp[i] = length
                i+=1
            else:
                if length != 0:
                    length = kmp[length -1]
                else:
                    kmp[i] = 0
                    i += 1
        return kmp
    def kmp(self, word: str, pattern:str):
        n = len(word)
        m = len(pattern)
        lps =  self.kmps(pattern)

        i= 0
        j =0
        while i <n:
            if pattern[j] == word[i]:
                i += 1
                j += 1
            if j == m :
                return True
            elif i<n and pattern[j] != word[i]:   
                if j != 0:
                    j = lps[j -1]
                else:
                    i +=1
        return False 

    def stringMatching(self, words: List[str]) -> List[str]:
        substring = set()
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and len(words[j]) <= len(words[i]):
                    if self.kmp(words[i], words[j]):
                        substring.add(words[j])
        return substring