#=
Author: 单单 <cxprcn@gmail.com>
QQGroup: 311818880
Introduction: 强大的词库制作工具
Description:
    lCiku是所有需要用到的码表路径，lRule是所有规则[2字词规则，3字词规则，……，多字词规则]
    每一条规则中，“数字+大写字母+小写字母”为一码，
    数字[1-9]表示所用码表序号(最多支持9个码表)
    大写字母[A-Y]表示第几个字，Z为最后一字
    小写字母[a-y]表示所用第几个编码，z为末码
=#

using DelimitedFiles

const lCiku = ["mb1.txt", "mb2.txt"] #需要用到的词库路径,最多10个
const lRule = ["1Aa1Ab1Ba1Bb", "1Aa1Ab1Ba1Ca", "1Aa1Ba1Ca1Za"] #造词规则
const wordsPath = "words.txt" #词库路径
const resPath = "result.txt" #保存路径

function getMb(mbPath) #读取并处理码表，处理成字典
    mb = readdlm(mbPath, '\n')
    themb = Dict{String,String}()
    @simd for i in mb
        temp = split(i, '\t')
        themb[temp[1]] = temp[2]
    end
    return themb
end

println("正在初始化……")
mbData = [] 
@simd for i in lCiku #生成码表列表 [码表1，码表2，]
    themb = getMb(i)
    push!(mbData, themb)
end

# 初始化
const t1 = [t for t = 1:25]
const t2 = split("ABCDEFGHIJKLMNOPQRSTUVWXY", "")
const t3 = split("abcdefghijklmnopqrstuvwxy", "")
const sRule2 = Dict{String,Int64}(zip(t2, t1))
const sRule3 = Dict{String,Int64}(zip(t3, t1))

#index(s,n) = s[nextind(s,0,n):nextind(s,0,n)]

function getCode(lword, rule) #通过词和规则获得编码
    code = ""
    for i in 1:3:length(rule) #分段，每段规则1个编码
        therule = rule[i:i+2] #规则
        a = parse(Int64, therule[1:1]) #转整型
        if therule[2:2] == "Z" #最后一个字
            b = length(lword)
        else
            b = sRule2[therule[2:2]]
        end
        x = mbData[a]
        try #获取编码
            y = lword[b]
            allcode = x[y]
            if therule[3:3] == "z"
                thecode = allcode[end]
            else
                thecode = allcode[sRule3[therule[3:3]]]
            end
            code *= thecode
        catch
            code = "#"
            break
        end
    end
    return code
end

println("正在编码")
wordsData = readdlm(wordsPath, '\n') #处理词库
fres = open(resPath, "w")
@simd for word in wordsData
    lword = split(word, "")
    if length(lword) > length(lRule) 
        rule = lRule[end] #长词
    else
        rule = lRule[length(lword)-1] #短词
    end
    code = getCode(lword, rule)
    write(fres, word, '\t', code, "\n") #写入文件
end
close(fres)
println("完成\n码表保存至 $resPath")
