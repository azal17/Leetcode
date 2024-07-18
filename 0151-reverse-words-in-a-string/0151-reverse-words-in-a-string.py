class Solution:
    def reverseWords(self, s: str) -> str:

        if not isinstance(s,str):
            return ''



        words = s.split()
        words.reverse()
        rev = ' '.join(words)

        return rev
       


