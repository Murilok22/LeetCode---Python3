class Solution:
    def strStr(self, haystack: str, needle: str) -> int:    
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle: # Verifica se a substring do tamanho de 'needle' a partir do Ã­ndice 'i' Ã© igual a 'needle'
                return i
        return -1