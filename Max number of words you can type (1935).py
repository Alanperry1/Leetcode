class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=set(brokenLetters)
        words=text.split()
        count=0
        for i in words:
            if not any(a in c for a in i):
                count+=1
        return count
