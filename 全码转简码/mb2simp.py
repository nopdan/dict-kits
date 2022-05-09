# -*- coding: utf-8 -*-
# Author: 单单 <cxprcn@gmail.com>
# Description: 全码码表转出简不出全码表

# 初始化数据

fMB = input("码表路径：")  # 码表路径
fRes = input("保存路径：")  # 保存路径
# lenCode_limit = {1: 2, 2: 1, 4: 99}  # 1简2重，2简2重，不指定为1重
lenCode_limit = eval("{" + input("规则：(例 1:2, 4:99)\n") + "}")  # 1简2重，2简2重，不指定为1重
if len(lenCode_limit) == 0:
    lenCode_limit = {1: 2, 4: 99}
isFreq = input("是否按照词频重新排序(False|True):")  # 是否按照词频重新排序 True|False
if isFreq == "True":
    fFreq = input("词频路径:")  # 词频路径

# 处理码表
word_codes = []
with open(fMB, "r", encoding="utf-8") as f:  # 载入码表
    lines = f.readlines()
    for i in lines:
        temp = i.strip("\n").split("\t")
        if len(temp) == 2:
            word_codes.append([temp[0], temp[1]])

# 排序
if isFreq:
    # 处理词频
    with open(fFreq, "r", encoding="utf-8") as f:  # 载入字词频表
        temp = f.readlines()
        freq = {}
        for i in temp:
            j = i.strip("\n").split("\t")
            freq[j[0]] = int(j[1])
    data = [[word, freq.get(word[0], 1)] for word in word_codes]
    data.sort(key=lambda x: x[1], reverse=True)
    word_codes = [i[0] for i in data]

# 出简不出全
codes = [i[1] for i in word_codes]
simpCodes = []
for code in codes:
    for i in range(len(code)):
        limit = lenCode_limit.get(i + 1, 1)
        theCode = code[: i + 1]
        if simpCodes.count(theCode) < limit or i == len(code) - 1:
            simpCodes.append(theCode)
            break

# 保存
with open(fRes, "w", encoding="utf-8") as f:
    for i in range(len(simpCodes)):
        f.write(f"{word_codes[i][0]}\t{simpCodes[i]}\n")
