class Solution:
    def reverseWords(self, s: str) -> str:

        if not isinstance(s, str):
            return ""
        

        word = s.split()  
        print(word)
        reversed_word = word[::-1]  
        print(reversed_word)
        reversed_sentence = ' '.join(reversed_word)  
        
        return reversed_sentence


