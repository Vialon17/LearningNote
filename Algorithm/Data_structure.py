class TreeNode:
    '''
    create a binary Tree.
    '''
    def __init__(self, val, left_child = None, right_child = None):
        '''
        val -> can be any type value;\n
        left,right child should be a `TreeNode` type.
        '''
        self._val = val
        self._left = left_child
        self._right = right_child
        if left_child is not None and not isinstance(left_child, TreeNode):
            raise TypeError('the child should be a TreeNode.')
        if right_child is not None and not isinstance(right_child, TreeNode):
            raise TypeError('the child should be a TreeNode.')

    @property
    def val(self):
        return self._val
    
    @val.setter
    def val(self, change_val):
        self._val = change_val

    @val.deleter
    def val(self):
        raise Exception("Can't delete the tree value key.")
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right

class Node:
    '''
    create a linked list
    '''

    def __init__(self, val, next = None) -> None:
        self._val = val
        self.next = next
        if next is not None and not isinstance(next, Node):
            raise TypeError('the next should be a chain node.')

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, change_val) -> None:
        self._val = change_val

        
if __name__ == '__main__':
    pass