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
def two_sum(self, numbers: list, target: int) -> list:
        # write your code here
        for i in range(len(numbers)):
            if (left := (target - numbers[i])) in numbers:                    
                return [i, numbers.index(left, i + 1)]
#time: 81ms, store: 5.90mb rank: 95.4%

#给定一张用二维数组表示的网格地图，其中1表示陆地单元格，0表示水域单元格。网格地图中的单元格视为水平/垂直相连（斜向不相连）。这个网格地图四周完全被水域包围着，并且其中有且仅有一个岛（定义为一块或多块相连的陆地单元格）。这个岛不包含湖（定义为不和外围水域相连的水域单元格）。一个地图单元格是边长为1的一个正方形；网格地图是一个矩形，并且它的长和宽不超过100。你要做的是求出这个岛的周长。
# [ [0,1,0,0],
#   [1,1,1,0],
#   [0,1,0,0],
#   [1,1,0,0] ]
#   答案:16

class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def island_perimeter(self, grid: list) -> int:
        # Write your code here
        lost_count = 0
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    for x, y in [(x,y) for x,y in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)) if x in range(0,len(grid)) and y in range(0, len(grid[x]))]:
                        if grid[x][y] == 1:
                            lost_count += 1
        print(perimeter, lost_count)
        return perimeter - lost_count
#logic: need reduce the lost_side_lenght when increase one side length.
#time: 102ms, store: 6.29mb rank: 40.5%

#有一排 26 个彩灯，编号从 0 到 25，现在给出了一系列控制指令来控制这些彩灯的开关。
#一开始这些彩灯都是关闭的，然后指令将逐条发出。
#在每条指令operation[i]中含有两个整数 operation[i][0], operation[i][1]。
#在接收到一条指令时，标号为 operation[i][0] 的彩灯会亮起，直到第 operation[i][1] 秒的时候熄灭。当灯熄灭后，下一条指令将#会发出。也就是说，任何时候只会有一盏灯亮着。
#其中第一条指令将在第0秒的时候发出，并被立刻执行。
#你的任务是找到哪个彩灯单次亮起的时间最长。
#输入：
#[[0,2],[1,5],[0,9],[2,15]]
#输出：
#'c'
#说明：
#operation = `[[0, 2], [1, 5], [0, 9], [2, 15]]`
#在第0秒的时候，接收到指令`[0, 2]`，此时标号为 0 的灯亮起，第 2 秒的时候熄灭。此时 0号灯 的单次亮起时间为`2-0 = 2` 秒。
#在第2秒的时候，接收到指令`[1, 5]`，此时标号为 1 的灯亮起，第 5 秒的时候熄灭。此时 1号灯 的单次亮起时间为 `5-2 = 3` 秒。
#在第5秒的时候，接收到指令`[0, 9]`，此时标号为 0 的灯亮起，第 9 秒的时候熄灭。此时 0号灯 的单次亮起时间为 `9-5 = 4` 秒。
#在第9秒的时候，接收到指令`[2, 15]`，此时标号为 2 的灯亮起，第 15 秒的时候熄灭。此时 2号灯 的单次亮起时间为 `15-9 = 6` #秒。
#所以单次亮起的最长时间为 `max(2, 3, 4, 6) = 6` 秒，是标号为 `2` 的彩灯。

#**你需要返回一个小写英文字母代表这个编号。`如 'a' 代表 0，'b' 代表 1，'c' 代表 2 ... 'z' 代表 25。`**所以你的答案应该是`'c'`
class Solution:
    """
    @param operation: A list of operations.
    @return: The lamp has the longest liighting time.
    """
    def longest_lighting_time(self, operation: list) -> str:
        # write your code here
        temp_dict = {}
        temp_fun = lambda x: operation[x][1] - operation[x-1][1] if x > 0 else operation[x][1]
        for i in range(len(operation)):
            if operation[i][0] not in temp_dict:
                temp_dict[operation[i][0]] = temp_fun(i)
            else:
                temp_dict[operation[i][0]] = max(temp_fun(i), temp_dict[operation[i][0]])
        get_keys = lambda d, value: [k for k,v in d.items() if v == value]
        return chr(get_keys(temp_dict, max([value for _, value in temp_dict.items()]))[0] + 97)
#time: 204ms, store: 21.6mb rank: 21.8%
#I misunderstand the topic once again.~_~|| 

#给定一个列表，该列表中的每个元素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。
#输入：列表 = [[1,1],2,[1,1]]
#输出：[1,1,2,1,1]

def flatten(self, nestedList):
        # Write your code here
        temp_list = []
        for i in nestedList:
            if isinstance(i, list):
                temp_list.extend(flatten(i))
            else:
                temp_list.append(i)
        return temp_list
#time: 1125ms, store: 18.2mb rank: 55.8%
#endless recursive.

#other version without recursive
def flatten(self, nestedList):
    # Write your code here
    if isinstance(nestedList, int):
        return [nestedList]
    
    ret = []
    while len(nestedList) > 0:
        current = nestedList.pop(0)
        if isinstance(current, int):
            ret.append(current)
        else:
            nestedList = current + nestedList
    return ret
#may it'll be better than mine.