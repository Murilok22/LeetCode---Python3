#Estrutura de Pilha (Stack)
class Solution:
    def isValid(self, s: str) -> bool:
        # Se for Ã­mpar,Ã© invÃ¡lido
        if len(s) % 2 != 0:
            return False

        # DicionÃ¡rio de pares (fechamento: abertura)
        mapeamento = {')': '(', '}': '{', ']': '['}
        pilha = []

        for char in s:
            if char in mapeamento:
                # Ã um caractere de fechamento
                # Pega o topo da pilha (ou um valor genÃ©rico se estiver vazia)
                topo = pilha.pop() if pilha else '#' 
                # pop para retirar o ultimo caractere da pilha
                # o if para saber se esta ou nÃ£o vazia 
                # o else '#' e para nÃ£o quebrar ao pegar a lista vazia 

                if mapeamento[char] != topo:
                    return False
            else:
                # Ã um caractere de abertura, adiciona na pilha
                pilha.append(char)

        return len(pilha) == 0