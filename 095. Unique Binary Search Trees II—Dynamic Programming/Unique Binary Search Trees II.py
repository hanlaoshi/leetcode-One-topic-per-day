#----------------辰星preorder算法------------
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        null = None
        dp = [[] for nums in range(0, n + 1)]
        dp[0] = [[[null]]]*(n+1)
        dp[1] = [[[i + 1]] for i in range(0,n)]
        for nums in range(2, n + 1):        	
        	for start in range(0, n + 1 - nums):
        		dp[nums].append([])
        		for top in range(start, start + nums):        			
        			for left in dp[top - start][start]:        				
        				for right in dp[start + nums - top - 1][top + 1]:  
        					dp[nums][start].append([top + 1])      					
        					dp[nums][start][-1].extend(left)
        					dp[nums][start][-1].extend(right)
        return dp[n][0]
#----------------辰星TreeNode解法------------
# Definition for a binary tree node.
from pprint import pprint
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0 : return []
        dp = [[] for nums in range(0, n + 1)]
        dp[0] = [[None]]*(n+1)
        dp[1] = [[TreeNode(i)] for i in range(1,n + 1)]
        for nums in range(2, n + 1):            
            for start in range(0, n + 1 - nums):
                dp[nums].append([])
                for top in range(start, start + nums):  
                    for left in dp[top - start][start]:                        
                        for right in dp[start + nums - top - 1][top + 1]:                    
                            dp[nums][start].append(TreeNode(top + 1))                          
                            dp[nums][start][-1].left = left
                            dp[nums][start][-1].right = right
        #return dp[n][0]
        #仅为显示效果
        def list_node(node, l, n):
            if node.left:
                l.append(node.left.val)
                n -= 1
            elif n:
              l.append(node.left)
            if node.right:
                l.append(node.right.val)
                n -= 1
            elif n:
              l.append(node.right)
            if n and node.left:
                    n = list_node(node.left, l, n)
            if n and node.right:
                    n = list_node(node.right, l, n)
            return n
        rtn = []
        for node in dp[n][0]:
            l = [node.val]
            list_node(node, l , n-1)
            rtn.append(l)
        return rtn
if __name__ == '__main__':
  pprint(Solution().generateTrees(3))
#--------------------第二种-------------------------
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution(object):
   def generateTrees(self, n):
       """
       :type n: int
       :rtype: List[TreeNode]
       """
       if n == 0:
           return []
       return self.dfs(1,n)
       
   def dfs(self, b, e):#b,e为开始和结束数字
       if b > e:
           return [None]
       res = []
       for rootVal in range(b, e + 1):
           leftTree = self.dfs(b, rootVal - 1)
           rightTree = self.dfs(rootVal + 1, e)
           for i in leftTree:
                for j in rightTree:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    res.append(root)
       return res
 
if __name__ == '__main__':
    S= Solution()
   S.generateTrees(3)
