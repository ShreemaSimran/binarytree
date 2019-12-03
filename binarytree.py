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
  return a

    def search(a,n,low,high):
      if(high>=low):
        mid=low+high/2
        count=0
        if(a[num]==n):
          print('Position is',num)
        elif(a[mid]>n):
          for i in range(0,mid-1):
            if i == n:
              count++
              print('position is',count)
        elif(a[mid]<n):
          count=mid
          for i in range(mid,high):
            if i == n:
              count++
              print('position is',count)
        
      

 root = Node(20)
 root.left = Node(15)
 root.right = Node(25)
 root.left.left = Node(10)
 root.left.right = Node(18)
 root.right.left = Node(22)
 root.right.right = Node(28)
 root.left.left.left = Node(5)
 root.left.left.right = Node(11)
 root.left.right.left = Node(16)
 root.left.right.right = Node(19)
 root.right.left.left = Node(21)
 root.right.left.right = Node(23)
 root.right.right.left = Node(21)
 root.right.right.right = Node(23)
 num = 15
 print('Enter the node to be traversed')
 n = int(input())
 a = postorder(root)
 search(a, n,0,num-1)
 
