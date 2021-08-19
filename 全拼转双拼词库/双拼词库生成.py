# -*- coding: utf-8 -*-
# Author: 单单 <cxprcn@gmail.com>

# 初始化
fp_mb = r"词库.txt"  # 全拼码表路径
split_qp = " "  # 全拼音节选择分隔符
fp_map = r"全拼-双拼映射表.txt"  # 全拼-双拼映射文件路径
fp_res = r"双拼词库.txt"  # 保存路径

form = 1  # 双拼码表格式 1:整句，2:定长
split_sp = "'"  # form=1 分隔符
form2 = 1  # form=2 三字词格式(1: a1a2b1c1，2: a1b1c1c2)

# 读取全拼词库
f = open(fp_mb, "r", encoding="utf-8")
qp = f.readlines()
f.close()

# 读取全拼-双拼映射
f = open(fp_map, "r", encoding="utf-8")
f_data = f.readlines()
f.close()
di = {}
for line in f_data:
    a = line.strip("\n").split("\t")
    if len(a) == 2:
        di[a[0]] = a[1]


def gen(li: list[str], form2: int):
    le = len(li)
    if le == 2:
        r = li[0] + li[1]
    elif le == 3:
        if form2 == 1:
            r = li[0][0] + li[1][0] + li[2]
        else:
            r = li[0] + li[1][0] + li[2][0]
    elif le >= 4:
        r = li[0][0] + li[1][0] + li[2][0] + li[-1][0]
    else:
        r = li[0]
    return r


# 保存双拼词库
f = open(fp_res, "w", encoding="utf-8")

for line in qp:
    wc = line.strip().split("\t")
    if len(wc) != 2:
        continue
    c = wc[1].split(split_qp)
    if len(wc[0]) != len(c):  # 词长和音节长度不一
        continue
    sp = [di.get(i, "##") for i in c]
    if form == 1:
        f.write(wc[0] + "\t" + split_sp.join(sp) + "\n")
    elif form == 2:
        f.write(wc[0] + "\t" + gen(sp, form2) + "\n")
    else:
        print("双拼码表格式错误：", form)
        break
f.close()
