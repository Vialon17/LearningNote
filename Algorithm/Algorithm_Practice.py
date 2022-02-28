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


if __name__ == '__main__':
    time_start = time()
    #1
    list1 = [23, 65, 4, 5, 1, 78, 3]
    #2
    s = "pns(i(bhbi)kj()kojs(tzanmj)rxmsl(zkl(i(ggqqeyo)bxht((auwsuuyhzb)cq((jabbcui))cpe(jj))(snd(a(mpe(ooe)ggjp))((k)iudv)acfk(kl(vagyd)c)r)))(y)i)k)))b)))q)(s))kxoy()kg)zbpyk)(ish()yc)ljjc()((qm(hec(zb((d)qvl(stob)y)s)rj)(f)zyf()(uw)dwjuryn)r()qegnfef()hm()nos(zb((suu))eudvoei)(p)ebmqqv)fooe)uiqs)t(ggcuh(uc))"
    print(bracket_check3(s))
    #for _ in range(999999):
    #    bracket_check2(s)
    time_end = time()
    print('time cost -> %s' % (time_end - time_start))