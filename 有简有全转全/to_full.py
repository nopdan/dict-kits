""" 
Description: 
    把有简有全的码表转为全码表（反向出简不出全了属于是）
    顺序会被打乱，要小心了
Author: 单单 <cxprcn@gmail.com>
"""

from typing import List, Dict

# 有简有全的码表

fMB = input("码表路径：")  # 码表路径
fRes = input("保存路径：")  # 保存路径
with open(fMB, encoding="utf-8") as f:
    lines = f.readlines()
    di: Dict[str, List[str]] = {}
    for line in lines:
        wc = line.strip("\n").split("\t")
        if len(wc) != 2:
            continue
        w, c = wc[0], wc[1]
        if len(di.get(w, [])) == 0:
            di[w] = [c]
        else:
            for i in range(len(di[w])):
                if c.startswith(di[w][i]):  # 如果已有词是当前词的简码，替换
                    # print("type: 0", c, di[w][i])
                    di[w][i] = c
                    break
                elif c.endswith(di[w][i]):  # 如果当前的词是已有词的简码，跳过
                    # print("type: 1", c, di[w][i])
                    break
            else:
                di[w].append(c)
                # print("type: 2", di[w])

# 保存
with open(fRes, "w", encoding="utf-8") as f:
    for key, value in di.items():
        for code in value:
            f.write(f"{key}\t{code}\n")
