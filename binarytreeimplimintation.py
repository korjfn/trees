class Treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = Treenode("r")
nodea = Treenode("a")
nodeb = Treenode("b")
nodec = Treenode("c")
noded = Treenode("d")
nodee = Treenode("e")
nodef = Treenode("f")
nodeg = Treenode("g")
nodez = Treenode("z")

root.left = nodea
root.right = nodeb
nodea.left = nodec
nodea.right = noded
nodeb.left = nodee
nodeb.right = nodef
nodef.left = nodeg
noded.right = nodez

print("root.right.left.data: ", root.right.left.data)
print(nodeb.right.left.data)