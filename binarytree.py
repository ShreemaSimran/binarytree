class Node:
  def __init__(self,key):
    self.left = None
    self.right = None
    self.val = key
 a = list()
 
 def postorder(root):
  if root:
    postorder(root.left)
    postorder(root.right)
    a.append(root.val)
    def search(n):
      low=0
      high=num
      while(low>0 and high<num)
      if(a[num//2]==n):
        print('found at',num//2)
      else
        if(a[num//2]>n):
          high=num//2
        else:
          low=num//2
        

 root = Node(1)
 root.left = Node(2)
 root.right = Node(3)
 root.left.left = Node(4)
 root.left.right = Node(5)
 root.right.right = Node(7)
 root.right.left = Node(6)
 root.left.left.left = Node(8)
 root.left.left.right = Node(9)
 root.left.left.left.left = Node(10)
 root.left.left.left.right = Node(11)
  num = 10
 print('Enter the node to be traversed')
 n = int(input())
 postorder(root)
 search(n)
 
