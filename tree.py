class Tree :
    def __init__(self, value, left=None, right=None) :
        self.value = value
        self.left  = left
        self.right = right

    def __str__(self) :
        return str(self.value)

def printTree(tree):
    if tree == None: return
    print (tree.value, end = " "),
    printTree(tree.left)
    printTree(tree.right)

def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.value


print('-------------- criando os filhos da árvore ----------')
left = Tree(2)
right = Tree(3)
print(left)
print(right)
tree = Tree(1,left,right)
print('--------------------------------------------------------')
print('----------------------- imprimindo árvore --------------')
printTree(tree)
print()
print('--------------------------------------------------------')
print('------------------ soma dos valores árvore -------------')
print(total(tree))
print('--------------------------------------------------------')
