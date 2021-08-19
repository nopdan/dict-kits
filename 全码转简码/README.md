# 出简不出全

## 介绍
全码码表转出简不出全。  

## 使用说明
- 可选调词频
- 可改参数：
```python
fMB = 'mb.txt'  # 码表路径
fRes = 'result.txt'  # 保存路径
lenCode_limit = {1: 2, 2: 2, 6: 99}  # 1简2重，2简2重，3|4|5简1重
isFreq = True  # 是否按照词频重新排序 True|False
fFreq = 'word_freq.txt'  # 词频路径
```

## 使用须知
- 使用utf8无BOM编码
- 码表格式`字词\t编码`
- 词频格式`字词\t词频`

