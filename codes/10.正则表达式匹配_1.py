#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配

# @lc code=start

# Finite state machine solution
# Referred to: https://leetcode-cn.com/problems/regular-expression-matching/solution/yi-bu-dao-wei-zhi-jie-an-zheng-ze-biao-da-shi-de-s/
# finite state machine nodes
class Node:

        # shows class variables
        def __init__(self):
            # char
            self.char = ''
            # parent node
            self.par = None
            # children dictionary
            # {key: list(nodes)}
            self.children = {}
            # if is end of fsm
            self.end = False
            # nullable
            self.null = 1
        
        # add node to children
        def append(self, c, node):
            if c not in self.children:
                self.children[c] = []
            for n in self.children[c]:
                if n == node:
                    return
            self.children[c].append(node)

class Solution:

    # recursively generate finite state machine
    def genPattern(self, node, pattern, index):

        # base case: if reach end
        # set last node as end
        # return if can be null
        if len(pattern) == index:
            node.end = True
            return node.null

        # find next and do recursion
        current = pattern[index]

        # if next is *
        # next is current
        # add self to children
        if current == '*':
            node.null = 0
            node.append(node.char, node)
            nextNode = node
        # else
        # create new node and init
        else:
            newNode = Node()
            newNode.char = current
            newNode.par = node
            nextNode = newNode
            node.append(current, newNode)

        # recursion
        # return if next is nullable
        result = self.genPattern(nextNode, pattern, index+1)

        # if next can be null
        # cur can also be end
        if result == 0:
            node.end = True

        # if current is nullable
        # fix fsm
        parent = node
        while parent.par is not None:
            if parent.null == 0:
                parent.par.append(nextNode.char, nextNode)
                parent = parent.par
            else:
                break

        # if par can be end
        return node.null + result
    
    # recursively check if fsm matches current result
    def check(self, node, string, index):

        # if reach end of string and can end here
        # return True
        if len(string) == index:
            return node.end

        # array of possible moves
        children = node.children.get('.', []).copy()
        for n in node.children.get(string[index], []):
            children.append(n)

        # recursively check array
        for n in children:
            result = self.check(n, string, index+1)
            if result:
                return True

        return False

    def isMatch(self, s: str, p: str) -> bool:
        # dummy node
        start = Node()
        start.char = '>'
        self.genPattern(start, p, 0)
        return self.check(start, s, 0)

# @lc code=end

