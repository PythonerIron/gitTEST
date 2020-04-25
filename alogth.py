'''

编写一个截取字符串的函数，输入为一个字符串和字节数，输出为按字节截取的字符串。但是要保证汉字不被截半个，如"我ABC"4，应该截为"我AB"，
输入"我ABC汉DEF"6，应该输出为"我ABC"而不是"我ABC+汉的半个"。
注意：这里说4个字节（4b）确实输出的是‘我AB‘,所以说这里应该是编码是GBK
'''


# def get_answer():
#     while True:
#         try:
#             string, len_defined = input().strip().split(',')
#             return_str = ''
#             len_total = 0
#             for i in string:
#                 len_total += len(i.encode('gbk'))
#                 print()
#                 if len_total <= int(len_defined):
#                     return_str += i
#             print(return_str)
#         except:
#             break
#
# if __name__ == '__main__':
#         get_answer()
# print('我'.encode('gbk'))
# print('我'.encode('unicode_escape'))
# print('我'.encode('utf8'))
# c = b'\xce\xd2'
# print(c.decode('gbk'))

# def get_last_string(s):
#     s1 = s.strip().split(' ')
#     print(s1)
#     for i in s1:
#         print(i)
#     s2 = s.strip().split()
#     print(s2)
#     for i in s2:
#         print(i)
#     # print(s1)
#     s11 = s1[-1]
#     # print(len(s11))
#     return len(s11)
# if __name__ == '__main__':
#     print(get_last_string('XSUWHQ'))

'''
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。

'''

# def get_sort():
#     s = input('多少行数据？')
#     l = list()
#     for i in range(int(s)):
#         _i = input('字符串：')
#         l.append(_i)
#     l.sort()
#     return l
# if __name__ == '__main__':
#     t = get_sort()
#     for i in t:
#         print(i)

# def get_sort(strings):
#     lis = strings.strip().split(' ')
#     s = lis[0]
#     l = lis[1:int(s)+1]
#     l.sort()
#     return l
# if __name__ == '__main__':
#     strings = input('')
#     t = get_sort(strings)
#     for i in t:
#         print(i)

# def get_sort(strings):
#     lis = strings.strip().split(' ')
#     s = lis[0]
#     l = lis[1:int(s) + 1]
#     l.sort()
#     return l
#
#
# if __name__ == '__main__':
#     strings = input('')
#     for i in range(int(strings)):
#         _i = input('')
#         strings += ' '
#         strings += _i
#     t = get_sort(strings)
#     for i in t:
#         print(i)
def get_sushu(m,n):

    sushu = list()

    for i in range(m, n+1):

        for j in range(2, i):
            if i % j == 0:
                break
        else:
            sushu.append(i)
    return len(sushu)
if __name__ == '__main__':
    print(get_sushu(1,1000))

class Solution():
    def get(self,s):
        a = set(s)
        return len(a)

a = Solution()
print(a.get('asssss'))


class Solution:
    # 返回合并后列表
    def Merge(self, list1,list2):
        # write code here
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        root = ListNode(0)
        first=root
        while list1 and  pHead2:
            val1=list1.val
            val2=pHead2.val
            if val1<=val2:
                root.next=ListNode(val1)
                pHead1=list1.next
            else:
                root.next=ListNode(val2)
                pHead2=pHead2.next
            root=root.next
        if list1:
            root.next=list1
        if pHead2:
            root.next=list2
        return first.next

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        p = pHead1
        q = pHead2
        h = new_head = ListNode(None)
        while p and q:
            if p.val <= q.val:
                h.next = p
                p = p.next
            else:
                h.next = q
                q = q.next
            h = h.next
        if p:
            h.next = p
        if q:
            h.next = q
        return new_head.next
