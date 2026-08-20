# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Caso base 1: se list1 estiver vazia, o resultado Ã© a list2
        if not list1:
            return list2
        
        # Caso base 2: se list2 estiver vazia, o resultado Ã© a list1
        if not list2:
            return list1
        
        # Passo recursivo:
        if list1.val <= list2.val:
            # list1 Ã© menor, entÃ£o ela vem primeiro.
            # O 'next' dela vai receber o resultado de mesclar o restante.
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2 Ã© menor, entÃ£o ela vem primeiro.
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2