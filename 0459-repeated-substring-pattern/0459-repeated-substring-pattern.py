class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Se s for composta por um padrÃ£o repetido, 
        # ela necessariamente aparecerÃ¡ no meio de (s + s) 
        # excluindo a primeira e a Ãºltima letra.
        return s in (s + s)[1:-1]

