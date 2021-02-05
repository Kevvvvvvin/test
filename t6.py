class BtreeNode(object):

    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Btree(object):
    def __init__(self,root=None):
        self.root=root
    def is_empty(self):
        return self.root is None
    def creat(self):
        s = input()
        if s =='#':
            return None
        treenode = BtreeNode(data = int(s))
        if self.root is None:
            self.root = treenode
        treenode.left= self.creat()
        treenode.right = self.creat()
    def inorder(self,root):
        s = []
        print(root.data)
        if root.left is not None:
            root.inorder(root.left)
        if root.data is not None:
            s.append(root.data)
        if root.right is not None:
            self.inorder(root.right)
        return s

tree=['2','1','','3','5']
bt = Btree()
bt.creat()
print(bt.inorder(bt.root))