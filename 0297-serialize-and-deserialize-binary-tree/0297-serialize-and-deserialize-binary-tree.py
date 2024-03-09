# Definition for a binary tree node.
#class TreeNode(object):
 #   def __init__(self, x):
  #      self.val = x
   #    self.right = None

class Codec:

    def serialize(self, root):
        s=""
        queue=[]
        queue.append(root)
        while queue:
            node=queue.pop(0)
            if node==None:
                s+='#,'
            else:
                s=s+str(node.val)+","
            if node!=None:
                queue.append(node.left)
                queue.append(node.right)
        return s
        

    def deserialize(self, data):
        if len(data)==0:
            return None
        values=data.split(",")
        if values[0]=='#':
            return None
        values.pop()
        queue=[]
        root=TreeNode(values[0])
        queue.append(root)
        i=0
        while queue:
            node=queue.pop(0)
            i+=1
            if values[i]=='#':
                node.left=None
            else:
                node.left=TreeNode(int(values[i]))
                queue.append(node.left)
            i+=1
            if values[i]=='#':
                node.right=None
            else:
                node.right=TreeNode(int(values[i]))
                queue.append(node.right)
        return root
                
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))