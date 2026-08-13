class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
         return False 
        else:
         invertido = int(str(x)[::-1]) # É o mesmo fundemento das listas, porem em uma string (lista de caracte) como se pegasse um pedaço da lista com List2=List1[1:2] no caso pegando do final para o começo, invertendo a string.
         return x == invertido

#   Gemini melhorando a solução do LeetCode 9 - Palindrome Number
    # class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #    s = str(x)
    #   return s == s[::-1]