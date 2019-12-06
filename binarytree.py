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
      while(high>=low):
        mid=low+high/2
        count=0
        if(a[high]==n):
          print('Position is',num+1)
        elif(a[mid]>n):
          for i in range(0,mid-1):
            if i == n:
              count++
              print('position is',count+1)
        elif(a[mid]<n):
          count=mid
          for i in range(mid,high):
            if i == n:
              count++
              print('position is',count+1)
       return -1
      

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
 root.right.right.left = Node(26)
 root.right.right.right = Node(30)
 num = 15
 print('Enter the node to be traversed')
 n = int(input())
 a = postorder(root)
 result=search(a, n,0,num-1,num)
 if(result == -1):
    print('Node is not present in the tree')
