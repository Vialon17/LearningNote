from logging import exception
from operator import index
from time import time
#请在 solution.py 里完善代码，实现以下函数功能：

    #get_len：返回输入列表的长度
    #get_max：返回输入列表的最大元素值
    #get_min：返回输入列表的最小元素值
    #pop_list：返回输入列表删除最后一个元素值后的结果

#这些函数都只有一个参数 list_in。
def get_max(list_in :list) -> str:
    max_ = list_in[0]
    for i in list_in:
        if max_ < i:
            max_ = i
        continue
    return max_

#描述

#你将得到一个由小写字母 a-z ，左括号 '(' 和右括号 ')' 构成的字符串 s。
#你的任务是删除尽可能少的括号，使得 s 里面的括号匹配。
#你需要返回删除括号后的字符串。
#由于答案可能会有很多，所以你只需要返回任意一个正确答案。

#例如："()", "(())", "()()", "(())()" 是括号匹配的字符串， 而 ")(", "(()", "()()(", "()())" 则是括号不匹配的字符串。 s = "a(b(c(de)fgh)"

def bracket_check(str_in: str) -> str:
    str_list = [i for i in str_in]
    str_left = []
    str_right = []
    for i in range(len(str_list)):
        if str_list[i] == '(':
            str_left.append(i)
        if str_list[i] == ')':
            str_right.append(i)
        continue
    if len(str_left) == len(str_right):
        return str_in
    else:
        if len(str_left) > len(str_right):
            for _ in range(len(str_left) - len(str_right)):
                str_left.pop()
        else:
            for _ in range(len(str_right) - len(str_left)):
                str_right.pop()
    lens_begin = min(str_left + str_right) + 1
    lens_end = max(str_left + str_right) + 1
    return str_in[lens_begin : lens_end]
#return -> b(c(de)fgh)

def bracket_check2(s : str) -> str:
    #from collections import deque
    left_bracket_index = []
    right_bracket_index = []
    s_temp = [x for x in s]
    for i in range(len(s)):
        if s[i] == '(':
            left_bracket_index.append(i)
        if s[i] == ')':
            right_bracket_index.append(i)
        continue
    if len(left_bracket_index) == len(right_bracket_index): return s
    if len(left_bracket_index) > len(right_bracket_index):
        min_index = right_bracket_index
        for _ in range(len(min_index)):
            temp = min(min_index)
            temp_leftindex_list = []
            for i in left_bracket_index:
                if i > temp: continue
                temp_leftindex_list.append(i)
            left_bracket_index.remove(max(temp_leftindex_list))
            right_bracket_index.remove(temp)
        index_mark = left_bracket_index
    else:
        min_index = left_bracket_index
        for _ in range(len(min_index)):
            temp = min(min_index)
            temp_rightindex_list = []
            for i in right_bracket_index:
                if i > temp: continue
                temp_rightindex_list.append(i)
            right_bracket_index.remove(max(temp_rightindex_list))
            left_bracket_index.remove(temp)
        index_mark = left_bracket_index
    for i in index_mark:
        #print('delete the index -> {0} value -> {1}'.format(i, s_temp[i]))
        s_temp.remove(s[i])
    #print('Completed mession.')
    return ''.join(s_temp)
#return -> ab(c(de)fgh)
## after read the stack, i'm a fool,hah
def bracket_check3(s: str) -> str:
    s_temp = [x for x in s]
    temp_stack = []
    right_bracker = []
    for i in range(len(s_temp)):
        if s_temp[i] == '(':
            temp_stack.append(i); continue
        if s_temp[i] == ')':
            if len(temp_stack) != 0:
                temp_stack.pop(); continue
            else:
                right_bracker.append(i); continue
    print(temp_stack)
    print(right_bracker)
    if len(temp_stack) != 0 or len(right_bracker) != 0:
        for x in range(len(temp_stack)):
            s_temp.pop(temp_stack[x] - x)
        for y in range(len(right_bracker)):
            s_temp.pop(right_bracker[y] - y)
    return ''.join(s_temp)        
# time: 167ms, store: 7.12mb

#大佬代码
# time: 61ms, store: 5.55mb
def removeParentheses(self, s: str) -> str:
    # write your code here.
    res = list(s)
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                res[i] = ''

    while stack:
        index = stack.pop()
        res[index] = ''

    return ''.join(res)
#评价：
#我是傻逼，自作多情多使用了一个right_bracker参数和运算空间。。。

#给出一棵二叉树，返回其节点值的后序遍历。
#输入：二叉树 = {1,2,3}
#输出：[2,3,1]
class Solution:

    from typing import List
    # I havn't download the lincode lib.
    # from lintcode import TreeNode

    """
    Definition of TreeNode:
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left, self.right = None, None
    """

    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root) -> List[int]:
        # root is a TreeNode type from Lintcode lib
        # write your code here
        if root is None:
            return []
        else:
            return Solution.postorder_traversal(self,root.left) + Solution.postorder_traversal(self,root.right) + [root.val]
#time: 102ms, store: 5.87mb rank: 6.8% 卧槽？

#有1000个桶，有且仅有一个桶里面装了毒药，其他的都装了水。
#这些桶从外面看上去完全相同。
#如果一只猪喝了毒药，它将在15分钟内死去。
#在一个小时内，至少需要多少只猪才能判断出哪一个桶里装的是毒药呢？
#(假如一共有 n 个桶，只有一个桶装了毒药。一只猪将在喝完毒药 m 分钟后死去。
#你需要多少只猪才能在 p 分钟内找出那个装毒药的桶呢？)

def poor_pigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
    # Write your code here
    pow_num = 0
    base = (minutes_to_test // minutes_to_die + 1)
    if buckets < base:
            return pow_num
    while True:
        if  buckets <= pow(base, pow_num):
            return pow_num
        pow_num += 1
#time: 81ms, store: 5.96mb rank: 79.0%

#Big Guy's code
def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

# 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
# 输入： numbers = [15,2,7,11] , target = 9
# 输出： [1,2]
def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        for i in range(len(numbers)):
            if (left := (target - numbers[i])) in numbers:                    
                return [i, numbers.index(left, i + 1)]
#time: 81ms, store: 5.90mb rank: 95.4%




















# Dijkstra's algorithm
# Graph:
#       -> A (5)    -> C (4)    ->(3)
# start (B->A 8)  (A->D 2)(C ->D 6)  End
#       -> B (2)    -> D (7)    ->(1)
class Graph:
    '''
    Params: Graph -> dict, vertexs -> list 
    '''
    def __init__(self, graph : dict, vertexs : list):
        self.graph = graph
        self.vertexs = vertexs

    @property
    def show(self):
        return self.graph
    
    def addvertex(self, vertex: str) -> int:
        if not isinstance(vertex, str):
            raise TypeError('Need str type.')
        self.vertexs.append(vertex)
        self.graph[vertex] = {}
        return self.vertexs.index(vertex)
    
    def addpath(self, start_vertex, end_vertex, value : int) -> int:
        if start_vertex not in self.vertexs:
            raise Exception('Start Vertex not in this Graph, Please Check!')
        self.graph[start_vertex][end_vertex] = int(value)
        if end_vertex not in self.vertexs:
            self.vertexs.append(end_vertex)
        return value

    def value(self, start_vertex : str, end_vertex : str) -> int:
        if start_vertex not in self.graph or end_vertex not in self.graph[start_vertex]:
            raise Exception('Path Error!')
        return self.graph[start_vertex][end_vertex]
    
def dijk():
    Dijk = Graph(
        {'start':{'A': 5, 'B': 2}, 
         'A':{'C': 4, 'D': 2},
         'B':{'A': 8, 'D': 7},
         'C':{'D': 6, 'end': 3},
         'D':{'end': 1},
         'end':{}
         }, 
        ['start', 'A', 'B', 'C', 'D', 'end']
        )
    cost = {'end': 1000}
    path = {}

if __name__ == '__main__':
    time_start = time()
    #1
    #list1 = [23, 65, 4, 5, 1, 78, 3]
    #2
    #s = "pns(i(bhbi)kj()kojs(tzanmj)rxmsl(zkl(i(ggqqeyo)bxht((auwsuuyhzb)cq((jabbcui))cpe(jj))(snd(a(mpe(ooe)ggjp))((k)iudv)acfk(kl(vagyd)c)r)))(y)i)k)))b)))q)(s))kxoy()kg)zbpyk)(ish()yc)ljjc()((qm(hec(zb((d)qvl(stob)y)s)rj)(f)zyf()(uw)dwjuryn)r()qegnfef()hm()nos(zb((suu))eudvoei)(p)ebmqqv)fooe)uiqs)t(ggcuh(uc))"
    #print(bracket_check3(s))
    #for _ in range(999999):
    #    bracket_check2(s)

    
    
    time_end = time()
    print('time cost -> %s' % (time_end - time_start))