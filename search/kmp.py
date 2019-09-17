
# coding: utf-8

# In[26]:


# 计算字符串的前缀数组
def prefix_table(string):
    table = [None] * len(string)
    table[0] = 0
    # i从第二个开始比较，因为第一个前缀已经确定为0, j表示当前子串最后一个字符
    j, i = 0, 1
    while i < len(table):
        # 如果相等就记录
        if string[i] == string[j]:
            j += 1
            table[i] = j
            i += 1
        else:
            if j > 0:
                j = table[j - 1]
            else:
                table[i] = j
                i += 1
    return table
    pass
table = prefix_table("ababcabaa")
print(table)


# In[27]:


# 前缀表移位
def move_prefix_table(table):
    if not table:
        return
    for i in range(len(table)-1, 0, -1):
        table[i] = table[i-1]
    table[0] = -1
    return table
table = move_prefix_table(table)
print(table)


# In[50]:


# kmp字符串匹配算法实现
def kmp(text, pattern):
    # 计算前缀表
    prefix = move_prefix_table(prefix_table(pattern))
    # text[i] - 长度m
    # pattern[j] - 长度n
    i, j, m, n = 0, 0, len(text), len(pattern)
    if m < n:
        print("not match any pattern")
    while i < m:
        # 找到匹配
        if j == n - 1 and text[i] == pattern[j]:
            print("found pattern at %d\n"%(i-j))
            # 往前寻找下一次匹配
            j = prefix[j]
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            # 待匹配字符串回溯到对应的前缀表位置
            j = prefix[j]
            # 遇到-1，待匹配和匹配字符串都右移一位
            if j == -1:
                i += 1
                j += 1
    pass

text = """全部劳动时间社会科学友情教育生活事业智慧爱情真理成功道德理想人生心理团结较高级复杂的劳动，是这样一种劳动力的表现，这种劳动力比较普通的劳动力需要较高的教育费用，它的生产需要花费较多的劳动时间。因此，具有较高的价值。"""
print("\ntext:\n"+text)
pattern = '劳动'
print("\npattern:\n"+ pattern)
print('\n')
kmp(text,pattern)
                

