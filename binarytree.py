class Node:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.val = key
 
 def postorder(root):
  if root:
    postorder(root.left)
    postorder(root.right)
    print(root.val),
    
 root = Node(1)
 root.left = Node(2)
 root.right = Node(3)
 root.left.left = Node(4)
 root.left.right = Node(5)
 root.right.right = Node(6)
 root.right.left = Node(7)
 root.left.left.left = Node(8)
 root.left.left.right = Node(9)
 root.left.left.left.left = Node(10)
 root.left.left.left.right = Node(11)