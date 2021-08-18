"""
Author: 单单 <cxprcn@gmail.com>
"""

# 读取全拼词库
f = open(r"词库.txt", "r", encoding="utf-8")
qp = f.readlines()
f.close()

## 选择分隔符
split_qp = " "

# 读取全拼-双拼映射
f = open(r"全拼-双拼映射表.txt", "r", encoding="utf-8")
f_data = f.readlines()
f.close()

# 选择双拼码表格式 1:整句，2:定长
form = 1
## form=1 选择分隔符
split_sp = "'"

## form=2 三字词格式(1: a1a2b1c1，2: a1b1c1c2)：
form2 = 1

# 保存双拼词库
f = open(r"双拼词库.txt","w",encoding="utf-8")


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
        print("双拼码表格式错误：",form)
        break
f.close()
