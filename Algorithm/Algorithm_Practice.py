from logging import exception
from operator import index
from time import time
from functools import lru_cache
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

#切割棒子，每次切花费cost_per_cut, 总共有lengths数组内不通长度的棒子，切成长度相同的短棒子，
#切完后剩余扔了，每单位棒子给sale_price，求最大利润。
def max_profit(self, cost_per_cut: int, sale_price: int, lengths: list) -> int:
    # write your code here
    profit = 0
    for l in range(1, max(lengths)):
        cut_num = 0
        sale_num = 0
        for i in lengths:
            temp_cut = (lambda x, y : x//y if x%y != 0 else x//y - 1)(i,l)
            cut_num += temp_cut
            sale_num += i//l
        temp_profit = sale_price * sale_num * l - cut_num * cost_per_cut
        if temp_profit >= profit:
            profit = temp_profit
    return profit
#time: 285ms, store: 5.97mb rank: 38.1%
#暴力穷举
#考虑可能近似公约数可能存在更贱简略的算法进行解答。

#在给定的数组中，找到出现次数最多的数字。
#出现次数相同时，返回数值最小的数字。
def find_number(self, array: list) -> int:
    # Write your code here.
    import collections
    max_num = 0
    counter = collections.Counter(array)
    answer = 0
    max_number = 0
    for key, value in counter.items():
        if value > max_number:
            max_number = value
            answer = key
        elif value == max_number and key < answer:
            answer = key
    return answer
#大佬解法

def find_number(self, array: list) -> int:
    # Write your code here.
    max_num = 0
    for i in sorted(array, reverse = 1):
        if array.count(i) >= array.count(max_num):
            max_num = i
    return max_num
#我的解法，时间复杂度贼高，我就是게憨憨。。。
#collections库真好用，涨见识了。

#给定一个由N个整数组成的数组A，一次移动，我们可以选择此数组中的任何元素并将其替换为任何值。数组的振幅是数组A中的最大值和最小值之间的差。返回通过执行最多三次替换之后数组A的最小振幅。
#输入:A = [-9, 8, -1]输出: 0解释：可以将 -9 和 8 替换成-1，这样所有元素都等于 -1，所以振幅是0
#输入:A = [14, 10, 5, 1, 0]输出: 1解释：为了实现振幅是1，我们可以将 14，10，5 替换成 1 或者 0
#输入:A = [11, 0, -6, -1, -3, 5]输出: 3解释：可以将11，-6，5都换成-2

def minimum_amplitude(a: list) -> int:
    # write your code here
    temp_list = sorted(a)
    if len(temp_list) <= 4:
            return 0
    num_abs = lambda x, y: abs(temp_list[x] - temp_list[y])
    num_range = [(x, x-4) for x in range(0,4)]
    return min([num_abs(x,y) for x,y in num_range])
#time: 101ms, store: 6.47mb rank: 77.7%
#思路错了卡壳了好久，。

#DL's code
def minimum_amplitude(a: list) -> int:
    if len(a) <= 4:
        return 0
    a.sort()
    res = float('inf')
    for i in range(4):  # must 4, not 3
        res = min(res, a[-1-i] - a[3-i]) # a[N-1-i] is the same as a[-1-i], but much slower
    return res
#思路就是这样的。

#给定一个整数数组，请算出让所有元素相同的最小步数。每一步你可以选择一个元素，使得其他元素全部加1。
#输入:[3, 4, 6, 6, 3]，输出:7
def array_game(arr: list) -> int:
        # write your code here
        min_num = min(arr)
        num = 0
        for i in arr:
            if i == min_num:
                continue
            num += (i - min_num)
        return num
#time: 142ms, store: 14.53mb rank: 93.5%
#看了题解发现逆向思维，max - min思路

def two_sum_v_i_i(self, nums: list, target: int) -> list:
    # write your code here
    temp_list = []
    for i in range(len(nums)):
        left_num = target - nums[i]
        if left_num in nums and (loc := nums.index(left_num)) > i:
            temp_list.append([i, loc])
    return temp_list

#删除链表中等于给定值 val 的所有节点。
#输入：head = 1->2->3->3->4->5->3->null, val = 3
#输出：1->2->4->5->null
#输入：head = 1->1->null, val = 1
#输出：null
"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

def remove_elements(head, val: int):
    # head: ListNode
    # write your code here
    re_head = head
    while head is not None:
        if head.val == val:
            re_head = head.next
        elif head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
                continue
        head = head.next
    return re_head
#time: 81ms, store: 7.25mb rank: 99.8%
#该题通过率仅24%，不忍滑稽一下~~~
#不过也思考了很长时间，
#题解：
#核心问题是出现指定值后进行链表后置操作，
#同时也要考虑开端和next的next的value值出现指定值/None的情况。

#给一个n*m大小的矩阵，寻找矩阵中所有比邻居（上下左右，对角也算，不考虑边界，即8个）都严格大的点。返回一个n*m大小的矩阵，如果原矩阵中的点比邻居都严格大，则该置为1，反之为0。
'''
输入:
    1 2 3
    4 5 8
    9 7 0
输出:
    0 0 0
    0 0 1
    1 0 0
'''
def highpoints(self, grid: list) -> list:
    # write your code here
    row = len(grid)
    col = len(grid[0])
    # -1,-1 -1,0 -1,1     0,-1 0,1        1,-1 1,0 1,1
    num = lambda x, y:[(x, y) for x, y in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]]
    num_range = lambda a, b : [(x, y) for x,y in num(a, b) if x in range(col) and y in range(row)]
    re_list = [[0 for i in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            num_list = [grid[x][y] for x, y in num_range(i, j)]
            if num_list == [] or grid[i][j] > max(num_list):
                re_list[i][j] = 1
    return re_list
#time: 387ms, store: 7.35mb rank: 1.20%
#全列表推导式，笑死我了哈哈哈。。。
#思路并无错误，看了rank上游代码，一堆for循环，并不pythonic，懒得放在这里了。
#这道题很喵~~~

#给您一个字符串形式的C ++文件（每行是一个字符串），我们希望您在注释行中找到“ Google”。如果注释行中有“ Google”，则返回true，否则返回false。
#C++有两种注释方式，一种是单行注释 //，代表着//后面的本行内容均为注释，另一种是多行注释，/* 和*/ 这两者之间的部分均为注释。
'''
输入: 
    S = ["#include<bits/stdc++.h>","using namespace std;","//Google test","int main(){","return 0;","}"]
输出: 
    true
输入: 
    S = ["#include<bits/stdc++.h>","using namespace std;","int main(){","int Google = 0","return 0;","}"]
输出: 
    false
说明: 
    google不在注释行内。
'''
def find_google(self, s: list) -> bool:
    # Write your code here.
    index_ = lambda x, y:y.index(x)
    note_statue = 0
    for i in s:
        if '//' in i:
            if 'Google' in i and index_('//', i) < index_('Google', i):
                return True
            continue
        elif '/*' in i:
            note_statue = 1
            if 'Google' in i and index_('/*', i) < index_('Google', i):
                return True
        elif '*/' in i:
            note_statue = 0
        elif note_statue == 1 and 'Google' in i:
            return True
    return False
#https://www.lintcode.com/problem/1883/
def TopkKeywords(k, keywords, reviews):
    temp_list = []
    key_sort = sorted(keywords)
    for i in key_sort:
        temp_count = 0
        for j in reviews:
            if i in j or i.capitalize() in j:
                temp_count += 1
        temp_list.append((i, temp_count))
    order = lambda x: x[1]
    temp_list.sort(key = order, reverse = True)
    print(temp_list)
    re_list = []
    if len(temp_list) > k:
        for x in range(k):
            re_list.append(temp_list[x][0]) 
    else:
        for x in range(len(temp_list)):
            re_list.append(temp_list[x][0]) 
    return re_list
#这道题懒得copy了。。。
#列表删除指定个数个元素后，使列表长度重复度最高。
#输入：
    [1,1,1,2,2,3]
    2
#输出：
    2
def min_item(ids: list, m: int) -> int:
    # write your code here
    from collections import Counter
    count = sorted(Counter(ids).values(), reverse = True)
    if count == [1]:
        return 0
    while count and count[-1] <= m:
        value = count.pop()
        m -= value
    return len(count)
#time: 162ms, store: 18.11mb rank: 67.7%
#为保证运行时间，使用HASH的字典，典型的空间换时间，贪婪算法。

#链表系列
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。你应该保留两部分内链表节点原有的相对顺序。
'''
输入：
    list = 1->4->3->2->5->2->null
    x = 3
输出：
    1->2->2->4->3->5->null
'''
def partition(head, x: int):
    # write your code here
    left, right = ListNode(0), ListNode(0)
    now, right_str= left, right
    while head:
        if head.next is None:
            right.next = None; break
        elif head.val < x:
            left.next = head; left = left.next
        else:
            right.next = head; right = right.next
        head = head.next
    left.next = right_str.next
    return now.next
#time: 102ms, store: 6.02mb rank: 10.0%
#思路：
# 1，分别创建前置链表和后置链表后进行连接。
# 2，也可以进行冒泡排序，不过时间复杂度不是太友好。
# 3，最直接可以转换为数组后进行处理后重新整合为链表。

#给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
'''
    输入 1->2->3->4->5->null
    输出 3->4->5->null
'''
def middle_node(head: ListNode) -> ListNode:
    # write your code here.
    re = now = head
    num1 = num2 = 0
    if head.next is None:
        return head
    while now.next:
        if num1 // 2 <= num2:
            now, num1 = now.next, num1 + 1
            continue
        num2 +=1; num1 += 1
        re, now = re.next, now.next
    return re.next
#time: 81ms, store: 5.82mb rank: 98.0%
#快慢指针问题
def middle_node(self, head: ListNode) -> ListNode:
    # write your code here.
    fastPointer = head
    slowPointer = head
    while fastPointer and fastPointer.next:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next
    return slowPointer
#大佬的这种写法就比较清晰了。。。

# 给定一个字符串str，返回字符串中字母顺序最大的而且同时在字符串中出现大写和小写的字母。
# 如果不存在这样的字母，返回‘~‘
'''
    输入:"aAbBcD"
    输出:'B'
'''
def find_letter(str_: str) -> str:
    # Write your code here.
    return max(temp) if (temp := [x for x in str_.upper() if chr(ord(x)+32) in str_ and x in str_]) != [] else '~'
# python, 喵哉！
# 更加简练的思路是每一小步骤内比较大小并进行保留，
# 相对来说时间复杂度会更加精妙。

# 统计字符串中出现大于2的组合次数（大于2时看做1/2两种情况）。
# 输入： S = "bbaa"
# 输出： 4 解释：答案为 "bbaa", "bba","baa","ba"
# 输入： S = "helllllooo"
# 输出： 4 解释： 答案为 "hello", "helo","heloo","helloo"
def stretch_word(s: str) -> int:
    # write your code here
    from itertools import groupby
    temp_list = [x for x in groupby(s) if len(list(x[1])) > 1]
    return pow(2, len(temp_list))
# itertools.groupby class 类似于SQL中的group by 分组条件。

#求给定范围内最大索引对问题
'''
输入: 
    A = [1, 4, 6, 8], B = [1, 2, 3, 5], K = 12
输出:
    [2, 3]
'''
#https://www.lintcode.com/problem/1797/solution/56682
def optimal_utilization(a: list, b: list, k: int) -> tuple:
        # write your code here
        list1, list2 = [x for x in a if x <= k], [y for y in b if y <= k]
        if list1 == [] or list2 == []: return []
        re_index, num = (0, 0), 0
        for i in range(len(list1)):
            for j in range(len(list2) - 1, -1, -1):
                if list1[i] + list2[j] <= k and list1[i] + list2[j] > num:
                    re_index, num = (i, j), list1[i] + list2[j]
        x, y = re_index
        if y != 0 and list2[y] == list2[y-1]:
            while y != 0 and list2[y] == list2[y-1]: y -= 1
            re_index = (x, y)
        return re_index

#https://www.lintcode.com/problem/44/description
#求目标列表的子列表的最小之和
'''
    Input -> [1,-1,-2,1]
    Output -> -3, [-1, -2]
    Input -> [1,-1,-2,1,-4]
    Output -> -6, [-1, -2, 1, -4]
'''
def min_sub_array(nums: list[int]) -> int:
    # write your code he
    if not nums or len(nums) == 0:
        return 0
    max_sum, min_sum = 0, float('inf')
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        min_sum = min(min_sum, total - max_sum)
        max_sum = max(max_sum, total)
    return min_sum
#纠结了好久，但暴力不可取；
# max_sum -> i之前最大的子列表之和
# total -> 0到i的总和
# min_sum -> 目标
 
# 没事干的华哥又想吃鸭头了。
# 已知华哥有 `budget` 毛钱；每个鸭头要`cost` 毛钱；
# 老板看华哥吃的贼香，于是想出来个促销方法赚华哥小钱钱：
#       每买一个鸭头给1个积分，每`exchange`个积分能换一个鸭头；
# 问总共有多少小鸭鸭要倒霉。
'''
for example:
    budget -> 6, cost -> 2, exchange -> 2,
    the rusult -> 5.
'''
def buy_beverage(budget: int, cost: int, exchange: int) -> int:
# write your code here
    init_num = budget // cost
    @lru_cache
    def recur(num: int) -> int:
        if num < exchange:
            return 0
        return num // exchange + recur(num % exchange + num // exchange)
    return recur(init_num) + init_num
# 结果：华哥吃了太多鸭头，生病住院了2333。。。

# https://www.lintcode.com/problem/615/
# 做了一天，吐了。。
# 深度搜索，
def can_finish(num_courses: int, prerequisites: list) -> bool:
        # write your code here
    from collections import defaultdict
    import copy
    temp_dict = defaultdict(set)
    for i in prerequisites:
        temp_dict[i[0]].add(i[1])
    def recur(left_set:set, num:int):
        #print(num, left_set,temp_dict[num])
        if left_set & temp_dict[num] != set():
            return False
        temp = True
        for i in temp_dict[num]:
            temp_left_set = copy.copy(left_set)
            temp_left_set.add(num)
            temp = temp and recur(temp_left_set, i) if temp_dict[num] != set() else True
        return temp
    re = True
    temp_dict2 = dict(temp_dict)
    for i in temp_dict2.keys():
        re = re and recur(set([i]), i)
    return re
# 正解 -> 拓扑排序
def canFinish(numCourses, prerequisites):
    # Write your code here
    from collections import deque
    edges = {i: [] for i in range(numCourses)}
    degrees = [0 for i in range(numCourses)] 
    for i, j in prerequisites:
        edges[j].append(i)
        degrees[i] += 1
    queue, count = deque([]), 0
    for i in range(numCourses):
        if degrees[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        count += 1

        for x in edges[node]:
            degrees[x] -= 1
            if degrees[x] == 0:
                queue.append(x)
    return count == numCourses

# https://www.lintcode.com/problem/287/solution/59133
# 区间贪心算法
# 可进行优化
def get_minium_vision_ward(pos: list[list[int]], l: int) -> int:
    # write your code here
    pos_sorted = sorted(pos, key = lambda x: x[0]*10 - x[1]*0.01)
    if pos_sorted[0][0] != 0: return -1
    pos_selected = [pos_sorted[0], pos_sorted[0]]
    for i in pos_sorted:
        if pos_selected[-1][1] >= l: break
        elif i[0] <= pos_selected[-2][1] and i[1] > pos_selected[-1][1]:
            pos_selected[-1] = i
        elif i[0] > pos_selected[-1][0] and i[1] > pos_selected[-1][1] and i[0] <= pos_selected[-1][1]:
            pos_selected.append(i)
        elif i[0] > pos_selected[-1][1]: return -1
    return lens if (lens := len(pos_selected)) <= len(pos) else -1