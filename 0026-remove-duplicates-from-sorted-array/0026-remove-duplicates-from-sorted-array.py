class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # O primeiro elemento sempre Ã© Ãºnico, entÃ£o comeÃ§amos a 
        # preencher a partir da posiÃ§Ã£o 1.
        k = 1 
        
        # Percorremos do segundo elemento atÃ© o fim
        for i in range(1, len(nums)):
            # Se o nÃºmero atual for diferente do anterior, Ã© um novo nÃºmero Ãºnico!
            if nums[i] != nums[i - 1]:
                # Colocamos ele na posiÃ§Ã£o 'k' da lista original
                nums[k] = nums[i]
                # Aumentamos o contador de Ãºnicos
                k += 1
        
        # Retornamos a quantidade de nÃºmeros Ãºnicos encontrados
        return k