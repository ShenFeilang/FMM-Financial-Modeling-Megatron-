import json

import pandas as pd
import random
# from cigarQuestionGenerator import corpList2021, corpList2022, corpListSummary2022
from cigarQuestionGenerator_q1_q5 import corpList2021, corpList2022, corpListSummary2022, \
    ctypeList2022, taxProfitByCorpAndCigarett, \
    taxProfitPerBoxByCorpAndCigarett, new_df2022, corpType1, new_df2021, stringToNumAndUnit,optionalCorpList,stdOplCorpList,checkOplExists

# 问：分析一下我司一类烟与其他公司竞品的对比情况
# 答：从单箱税利来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；豪情、白狼、软富健略高于行业均值；其余10个产品均低于行业同价类产品。
# 从单箱利润来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；豪情、白狼、软富健与行业均值持平；其余10个产品均低于行业同价类产品。

# question5 = "分析一下我司一类烟与其他公司竞品的对比情况"
# answer5 = "单箱税利来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；" \
#           "豪情、白狼、软富健略高于行业均值；" \
#           "其余10个产品均低于行业同价类产品。从单箱利润来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；" \
#           "豪情、白狼、软富健与行业均值持平；其余10个产品均低于行业同价类产品。"
    # 第一名若高于行业平均，则有较大优势
    # 第二名是否略高于行业均值
    # 高于均值的产品，具有较大优势
    # 与行业均值持平，最后低于同价类产品


tpBigAdvantage = []  # 单箱税利有较大优势
tpOverAvg = []  # 略高于
# sameAvg = ""        # 持平
tpBelowAvg = []  # 低于行业同价类产品
opBigAdvantage = []  # 单箱利润有较大优势
opOverAvg = []  # 略高于
opBelowAvg = []  # 低于行业同价类产品
strForBigAdv = "与行业同价类产品相比具有较大优势；"
strForOverAvg = "略高于行业同价类产品；"
strForBelowAvg = "低于行业同价类产品；"
def buildQ5Ans(tpBigAdvantage, tpOverAvg,tpsimilarAvg, tpBelowAvg, strForBigAdv, strForOverAvg, strForSimilarAvg, strForBelowAvg, startStr):
    # if len(tpBigAdvantage) > 3:
    #     tpanswer5p1 = "、".join(tpBigAdvantage[:2]) + "等" + str(len(tpBigAdvantage)) + "个产品"
    # elif not len(tpBigAdvantage) == 0:
    #     tpanswer5p1 = "、".join(tpBigAdvantage) + "均"
    if len(tpBigAdvantage) > 0: # 无数量限制，全部生成
        tpanswer5p1 = "、".join(tpBigAdvantage)
    else:
        tpanswer5p1 = ""
    if not tpanswer5p1 == "":
        tpanswer5p1 = tpanswer5p1 + strForBigAdv

    # if len(tpOverAvg) > 3:
    #     tpanswer5p2 = "、".join(tpOverAvg[:2]) + "等" + str(len(tpOverAvg)) + "个产品"
    # elif not len(tpOverAvg) == 0:
    #     tpanswer5p2 = "、".join(tpOverAvg) + "均"
    if len(tpOverAvg) > 0:
        tpanswer5p2 = "、".join(tpOverAvg)
    else:
        tpanswer5p2 = ""
    if not tpanswer5p2 == "":
        tpanswer5p2 = tpanswer5p2 + strForOverAvg

    if len(tpsimilarAvg)>0:
        tpanser5psub2 = '、'.join(tpsimilarAvg)
    else:
        tpanser5psub2 = ''
    if not tpanser5psub2 == "":
        tpanser5psub2 = tpanser5psub2 + strForSimilarAvg

    # if len(tpBelowAvg) > 3:
    #     tpanswer5p3 = "、".join(tpBelowAvg[:2]) + "等" + str(len(tpBelowAvg)) + "个产品"
    # elif not len(tpBelowAvg) == 0:
    #     tpanswer5p3 = "、".join(tpBelowAvg) + "均"
    tpanswer5p3 = ''
    if len(tpBelowAvg)>0:
        tpanswer5p3 = '其余' + str(len(tpBelowAvg)) + '个产品'
        if len(tpBelowAvg)> 1:
            tpanswer5p3 += '均'
    #     tpanswer5p3 = '、'.join(tpBelowAvg)
    # else:
    #     tpanswer5p3 = ''
    if not tpanswer5p3 == "":
        tpanswer5p3 = tpanswer5p3 + strForBelowAvg
    # if not tpanswer5p3 == "":
    #     tpanswer5p3 = tpanswer5p3 + strForBelowAvg
    tpanswer5p123 = tpanswer5p1 + tpanswer5p2 + tpanser5psub2+ tpanswer5p3
    if not tpanswer5p123 == "":
        tpanswer5p123 = startStr + tpanswer5p123[:len(tpanswer5p123)-1] + "。"
    return tpanswer5p123


# 称谓： 单箱利润
# 列的英文编码： 'AH'
# [话术1，话术2，话术3]
# {year: 2022, }    # 同比，或者单一年份对比
# 单箱，或者其他非直接取数的特异公式
# 取值函数

normalScriptList = ["与行业同价类产品相比具有较大优势；", "略高于行业同价类产品；", "低于行业同价类产品；"]
listOfTPCCFilterdict = [{'year': 2022, 'corpName': '*', 'cigarName': '*', 'cigarType': '*', 'col': 'AI'}]
listOfColInLetters = [['AI','perbox'],['AK','sum']]  # ['某一列的字母',具体用哪个函数，0 表示用taxprofit,1表示用perbox函数]


# todo 遍历colList 进行同一主体，多个数据内容的生产
def forQ5(yearList = [2022], corpNameList = corpList2022, cigarNameList = ['*'], cigarTypeList = ctypeList2022, colList = ['AI'], funcName = 'sum'):
    for year in yearList:
        for corpName in corpNameList:
            for cigarName in cigarNameList:
                for cigarType in cigarTypeList:
                    for col in colList:
                        if funcName == 'sum':
                            aNumber = taxProfitByCorpAndCigarett(year = year, corpName=corpName, cigarName = cigarName, cigarType= cigarType, col = col)
                        else:
                            aNumber = taxProfitPerBoxByCorpAndCigarett(year = year, corpName=corpName, cigarName = cigarName, cigarType= cigarType, col = col)


lookuptable = {     # "表头": ['问题和回答的称谓', '列的英文编号', ['远高于平均的话术', '略高于平均的话术', '低于平均的话术'], [筛选条件]，[取值函数]]
    "单箱税利": 1,
    "单箱利润": 2,
    "税利": 3,
    '利润': 4,
    '产量（万支）': 5,
    '销量（万支）': 6,
    '主营业务收入': 7,
    '主营业务成本': 8,
    '应交增值税': 9,
    '主营业务税金及增加': 10,
    '主营业务利润': 11,
    '销售费用': 12,
    '管理费用': 13,
    '财务费用': 14,
    '销售成本费用率': 15,
    '营业利润': 16,
    '税利合计': 17,
    '生成成本': 18,
    '其中：原料': 19,
    '其中：主要材料': 20,
    '其中：燃料动力': 21,
    '其中：职工薪酬': 22,
    '其中：制造费用': 23,
    '其他入库产品': 24,
    '其他出库产品': 25,
    '库存产成品': 26,
    '卷烟牌号编码': 27,
    '产品类型编码': 28,
    '国内国外编码': 29,
    '是否爆珠': 30,
    '卷烟周长': 31
}





#分析一下我司一类烟与其他公司竞品的对比情况

# 主体：默认为“福建中烟工业有限责任公司”，如果话术中指定了具体主体，比如龙烟、厦烟，则以话术为准。
# 较大优势逻辑：（产品指标-行业均值）/|行业均值|*100% 大于行业均值20%
# 略高于行业均值逻辑：（产品指标-行业均值）/|行业均值|*100%  在5%---20%之间。
# 低于行业同价类逻辑：（产品指标-行业均值）<0
# 持平逻辑：（产品指标-行业均值）/|行业均值|*100%  0---5%之间
# 指标：
# 某个一类烟品牌单箱税利：C列卷烟名称为“***”的品牌，AL列的合计*5.
# 某个一类烟品牌单箱利润：C列卷烟名称为“***”的品牌，AI列的合计*5。
# 行业一类烟单箱税利：(D列产品价类为一类烟，AL列的合计*5)/D列产品价类为一类烟的行数。
# 行业一类烟单箱利润：(D列产品价类为一类烟，AI列的合计*5)/D列产品价类为一类烟的行数。
# 行业单箱税利：（取【AL，4】单元格数值*5）/总行数
# 行业单箱利润：取【AI，4】单元格数值*5/总行数


# '若xx品牌满足(xx品牌的单箱税利-行业均值)/abs(行业均值)*100%>20%，则输出：' \
# '"从单箱税利来看，xx品牌、xx品牌与行业同价类产品相比具有较大优势"，' \
# '若yy品牌5%<(yy品牌的单箱税利-行业均值)/abs(行业均值)*100%<20%，则输出：' \
# '"yy品牌、xx品牌略高于行业均值"，' \
# '若zz品牌0%<(zz品牌的单箱税利-行业均值)/abs(行业均值)*100%<5%，则输出' \
# '"zz品牌、zz品牌与行业均值持平"' \
# '记录满足(品牌的单箱税利-行业均值)<0的数量n，输出' \
# '"其余n个产品均低于行业平均水平"'
def buildQ5CoT(countOfcurCigarName,curt,curcorp,tpBigAdvantage,tpOverAvg,tpSimilarAvg,tpBelowAvg,opBigAdvantage, opOverAvg,opSimilarAvg, opBelowAvg,ccType,ctSYan):
    if str(curt)=='其他':
        curtYan = '其他烟'
    else:
        curtYan = str(curt)

    res720 =   'A：分析过程：\n我用2个步骤来分析这个问题：\n' \
                'Step1，我遍历我司('+str(curcorp)+')' \
                '今年的所有'+curtYan+'品牌，对这个品牌进行分组：' \
                '我找到这个品牌的单箱税利，和行业整体单箱税利的3个参考值依次进行比较：'
    if len(tpBigAdvantage) > 0:
        res720 += '、'.join(tpBigAdvantage)+'的单箱税利大于参考值A（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱税利参考值A'] + '），属于A组。'
    if len(tpOverAvg) > 0:
        res720 += '、'.join(tpOverAvg) + '的单箱税利在区间参考值A（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱税利参考值A']+'）和参考值B('+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱税利参考值B']+'）之间，属于B组。'
    if len(tpSimilarAvg)>0:
        res720 += '、'.join(tpSimilarAvg) + '的单箱税利在区间参考值B（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱税利参考值B']+'）和参考值C('+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱税利参考值C']+'）之间，属于C组。'
    if len(tpBelowAvg)>0:
        res720 += '、'.join(tpBelowAvg) + '的单箱税利小于参考值C（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱税利参考值C']+'），属于D组。\n'

    res720 += '我找到这个品牌的单箱利润，和行业整体单箱利润的3个参考值依次进行比较：'
    if len(opBigAdvantage) > 0:
        res720 +=  '、'.join(opBigAdvantage)+'的单箱税利大于参考值E（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱利润参考值E'] + '），属于E组。'
    if len(opOverAvg) > 0:
        res720 += '、'.join(opOverAvg) + '的单箱税利在区间参考值E（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱利润参考值E'] + '）和参考值F（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱利润参考值F']+'）之间，属于F组。'
    if len(opSimilarAvg) > 0:
        res720 += '、'.join(opSimilarAvg) + '的单箱税利在区间参考值F（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱利润参考值F'] + '）和参考值G（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱利润参考值G']+'）之间，属于G组。'
    if len(opBelowAvg) > 0:
        res720 += '、'.join(opBelowAvg) + '的单箱税利小于参考值G（'+ccType[0]["行业各类烟税利利润"][ctSYan+'单箱利润参考值G'] + '），属于H组。'
    res720 +=   'Step2，遍历每个组：'
    if len(tpBigAdvantage) > 0:
        res720 += '输出A组的所有品牌名，然后输出“单箱税利与行业同价类产品相比具有较大优势”，'
    if len(tpOverAvg) > 0:
        res720 += '输出B组的所有名牌名，然后输出“略高于行业同价类产品”，'
    if len(tpSimilarAvg) > 0:
        res720 += '输出C组的所有品牌名，然后输出“与行业均值持平”，'
    if len(tpBelowAvg) > 0:
        res720 += '最后数出D组的品牌个数'+str(len(tpBelowAvg))+'，输出“其余'+str(len(tpBelowAvg))+'个产品均低于行业同价类产品。'
    if len(opBigAdvantage) > 0:
        res720 += '输出E组的所有品牌名，然后输出“单箱利润与行业同价类产品相比具有较大优势”，'
    if len(opOverAvg) > 0:
        res720 += '输出F组的所有名牌名，然后输出“略高于行业同价类产品”，'
    if len(opSimilarAvg) > 0:
        res720 += '输出G组的所有品牌名，然后输出“与行业均值持平”，'
    if len(opBelowAvg) > 0:
        res720 += '最后数出H组的品牌个数' + str(len(opBelowAvg)) + '，输出“其余' + str(len(opBelowAvg)) + '个产品均低于行业同价类产品。\n'

    # '如果大于参考值A' + ccType["行业各类烟税利利润"][ctSYan + '单箱税利参考值A'] + '，' \
        # '如果小于参考值A' + ccType["行业各类烟税利利润"][ctSYan + '单箱税利参考值A'] + '且大于参考值B' +
# ccType["行业各类烟税利利润"][ctSYan + '单箱税利参考值B'] + '，把这个品牌归入B组，B组有：' + \
#  \
# '如果小于参考值B' + ccType["行业各类烟税利利润"][ctSYan + '单箱税利参考值B'] + '且大于参考值C' + \
# ccType["行业各类烟税利利润"][ctSYan + '单箱税利参考值C'] + '，把这个品牌归入C组，C组有：' + '、'.join(tpSimilarAvg) + '。' \
#                                                                                                                   '如果小于参考值C' + \
# ccType["行业各类烟税利利润"][ctSYan + '单箱税利参考值C'] + '，把这个品牌归入D组，D组有：' + '、'.join(tpBelowAvg) + '。' \
    # 我的分析过程：
    # 我用2个步骤来分析这个问题：
    # step1，我遍历我司()
    # 今年的所有一类烟品牌，对这个品牌进行分组：我找到这个品牌的单箱税利，和行业整体单箱税利的3个参考值依次进行比较，如果大于参考值A，把这个品牌归入A
    # 组，如果小于参考值A且大于参考值B，把这个品牌归入B组，如果小于参考值B且大于参考值C，把这个品牌归入C组，如果小于参考值C，把这个品牌归入D组。
    # step2，遍历每个组：输出A组的所有名牌名，然后输出“与行业同价类产品相比具有较大优势”，输出B组的所有名牌名，然后输出“略高于行业均值”，输出C组
    # 的所有品牌名，然后输出“与行业均值持平”，最后数出D组的品牌个数n，输出“其余n个产品均低于行业同价类产品”
    res = '分析过程：\n默认所提供的数据中的最近年份为今年。我司'+str(curcorp)+'今年的一类烟品牌一共有'+ str(countOfcurCigarName)+'个，' \
            '分别将每个'+str(curt)+'品牌的单箱税利依次与行业整体'+str(curt)+ '的单箱税利较大优势阈值、单箱税利略高阈值、单箱税利持平阈值进行比较，' \
            '并归类于较大优势组、略高于行业均值组、与行业均值持平组、低于行业均值组。' \
            '若行业整体'+str(curt)+ '的单箱税利<0：' \
            '行业的单箱税利较大优势阈值=(行业单箱税利)*(100-20)%，' \
            '行业的单箱税利略高阈值=(行业单箱税利)*(100-5)%，' \
            '行业的单箱税利持平阈值=(行业单箱税利)*(100)%。' \
            '若行业整体'+str(curt)+ '的单箱税利>0：' \
            '行业的单箱税利较大优势阈值=(行业单箱税利)*(100+20)%，' \
            '行业的单箱税利略高阈值=(行业单箱税利)*(100+5)%，' \
            '行业的单箱税利持平阈值=(行业单箱税利)*100%。' \
            '对于属于单箱税利较大优势组的xx品牌，输出：' \
            '"从单箱税利来看，xx品牌、xx品牌与行业同价类产品相比具有较大优势"，' \
            '对于属于单箱税利略高于行业均值组的yy品牌，输出：' \
            '"yy品牌、xx品牌略高于行业均值"，' \
            '对于属于单箱税利与行业均值持平组的zz品牌，输出：' \
            '"zz品牌、zz品牌与行业均值持平"，' \
            '统计属于单箱税利低于行业均值组的ww品牌数量，输出：' \
            '"其余n个产品均低于行业同价类产品"。' \
            '然后，再将每个'+str(curt)+'品牌的单箱利润依次与行业整体'+str(curt)+ '的单箱利润较大优势阈值、单箱利润略高阈值、单箱利润持平阈值进行比较，' \
            '并归类于较大优势组、略高于行业均值组、与行业均值持平组、低于行业均值组，以同样的方式输出。\n'
    return res720

countOfQ5 = 0
Q5A5List =[]
QA5noCoT = []
QA5Max = []
biggestLen = 0
biggestcorp = ''
for curyear in [2021,2022]:
    for curcorp in corpList2022:
        if checkOplExists(optionalCorpList+['行业标准','烟草行业十九家合计','nan'],curcorp):
            continue
        if checkOplExists(stdOplCorpList,curcorp):
            continue
        if curyear == 2022:
            curCTdata = new_df2022[new_df2022["所属公司"] == curcorp]
            corpT1Idx = 1
        else:
            curCTdata = new_df2021[new_df2021["所属公司"] == curcorp]
            corpT1Idx = 0
        for curt in ctypeList2022[1:]:     # 遍历不同类别的烟,这里过滤了nan
            ctStrYan = str(curt)
            if ctStrYan == '其他':
                ctStrYan = ctStrYan + '烟'
            curCT = curCTdata[curCTdata["产品价类"] == curt]
            curcorpType = []
            curcorpType.append({"行业各类烟税利利润": {
            '年度': curyear,
            ctStrYan + '税利': corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + '税利'],
            ctStrYan + '利润': corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + '利润'],
            ctStrYan + "单箱税利": corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + "单箱税利"],
            ctStrYan + '单箱利润': corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + '单箱利润'],
            ctStrYan + "单箱税利参考值A": corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + "单箱税利较大优势阈值"],
            ctStrYan + '单箱利润参考值E': corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + '单箱利润较大优势阈值'],
            ctStrYan + "单箱税利参考值B": corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + "单箱税利略高阈值"],
            ctStrYan + '单箱利润参考值F': corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + '单箱利润略高阈值'],
            ctStrYan + "单箱税利参考值C": corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + "单箱税利持平阈值"],
            ctStrYan + '单箱利润参考值G': corpType1[corpT1Idx]["行业各类烟税利利润"][ctStrYan + '单箱利润持平阈值'],

            # "一类烟单箱税利较大优势阈值": taxProfitPerBoxByCorpAndCigarett(year=2022,cigarType='一类烟',threshold=1.2),
            # '一类烟单箱利润较大优势阈值': taxProfitPerBoxByCorpAndCigarett(year=2022,cigarType='一类烟',col='AI',threshold=1.2),
            # "一类烟单箱税利略高阈值": taxProfitPerBoxByCorpAndCigarett(year=2022, cigarType='一类烟', threshold=1.05),
            # '一类烟单箱利润略高阈值': taxProfitPerBoxByCorpAndCigarett(year=2022, cigarType='一类烟', col='AI', threshold=1.05),
            # "一类烟单箱税利持平阈值": taxProfitPerBoxByCorpAndCigarett(year=2022, cigarType='一类烟'),
            # '一类烟单箱利润持平阈值': taxProfitPerBoxByCorpAndCigarett(year=2022, cigarType='一类烟', col='AI'),
            }})
            tpBigAdvantage = []   # 单箱税利有较大优势
            tpOverAvg = []        # 略高于
            tpSimilarAvg = []        # 持平
            tpBelowAvg = []       # 低于行业同价类产品
            opBigAdvantage = []     # 单箱利润有较大优势
            opOverAvg = []          # 略高于
            opSimilarAvg = []       # 持平
            opBelowAvg = []         # 低于行业同价类产品
            question5 = 'Q：烟草行业及我司（'+str(curcorp)+'）'+ctStrYan+'近两年的部分数据如下：\n' +json.dumps(curcorpType[0], ensure_ascii=False)
            # question5 = question5 + "请分析" + str(curcorp) + ctStrYan + "与其他公司竞品的对比情况"
            countOfcurCigarName = 0
            for curctName in curCT['卷烟名称']:       # 遍历同类、同公司、但是不同名称的烟
                curcorpType.append({
                    curctName: {
                        '年度': curyear,
                        '类别': curt,
                        "税利": taxProfitByCorpAndCigarett(corpName=curcorp, year=curyear, cigarName=curctName,
                                                           cigarType=curt),
                        "利润": taxProfitByCorpAndCigarett(corpName=curcorp, year=curyear, cigarName=curctName,
                                                                 cigarType=curt,col='AH'),
                        "单箱税利": taxProfitPerBoxByCorpAndCigarett(corpName=curcorp, year=curyear, cigarName=curctName,
                                                                     cigarType=curt),
                        "单箱利润": taxProfitPerBoxByCorpAndCigarett(corpName=curcorp, year=curyear, cigarName=curctName,
                                                                     cigarType=curt, col='AI'),
                    }
                })
                # ctStrYan = str(curt)
                # if ctStrYan == '其他':
                #     ctStrYan = ctStrYan + '烟'
                # if countOfcurCigarName < 6:
                question5 = question5 + json.dumps(curcorpType[len(curcorpType)-1], ensure_ascii=False)
                overallNum, overallunit, overallPower = stringToNumAndUnit(curcorpType[0]["行业各类烟税利利润"][ctStrYan + "单箱税利"])
                thisCiagrNum, thisCiagrUnit, thisCiagrPower = stringToNumAndUnit(curcorpType[len(curcorpType) - 1][curctName]["单箱税利"])
                overalltp = int(float(overallNum) * overallPower)
                thisCigtp = int(float(thisCiagrNum) * thisCiagrPower)
                if overalltp > thisCigtp:
                    tpBelowAvg.append(curctName)
                elif (overalltp < 0 and thisCigtp < 0.95*overalltp) or (overalltp>0 and round(thisCigtp/overalltp,2) < 1.05):
                    tpSimilarAvg.append(curctName)
                elif (overalltp < 0 and thisCigtp < 0.8*overalltp) or (overalltp>0 and round(thisCigtp/overalltp,2) < 1.2):
                    tpOverAvg.append(curctName)
                else:
                    tpBigAdvantage.append(curctName)
                overallNum, overallunit, overallPower = stringToNumAndUnit(curcorpType[0]["行业各类烟税利利润"][ctStrYan + "单箱利润"])
                thisCiagrNum, thisCiagrUnit, thisCiagrPower = stringToNumAndUnit(curcorpType[len(curcorpType) - 1][curctName]["单箱利润"])
                overallop = int(float(overallNum) * overallPower)
                thisCigop = int(float(thisCiagrNum) * thisCiagrPower)
                if overallop > thisCigop:
                    opBelowAvg.append(curctName)
                elif (overallop < 0 and thisCigop < 0.95*overallop) or (overallop>0 and thisCigop / overallop < 1.05):
                    opSimilarAvg.append(curctName)
                elif (overallop < 0 and thisCigop < 0.8*overallop) or (overallop>0 and thisCigop/overallop < 1.2):
                    opOverAvg.append(curctName)
                else:
                    opBigAdvantage.append(curctName)

                countOfcurCigarName = countOfcurCigarName + 1
            # answer5 = "单箱税利来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；" \
            #           "豪情、白狼、软富健略高于行业均值；" \
            #           "其余10个产品均低于行业同价类产品。" \
            #           "从单箱利润来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；" \
            #           "豪情、白狼、软富健与行业均值持平；" \
            #           "其余10个产品均低于行业同价类产品。"
            tpanswer5 = ""
            opanswer5 = ""
            startStr = "单箱税利来看，"
            strForBigAdv = "与行业同价类产品相比具有较大优势；"
            strForOverAvg = "略高于行业同价类产品；"
            strForSimilarAvg = '与行业均值持平；'
            strForBelowAvg = "低于行业同价类产品；"
            tpanswer5 = buildQ5Ans(tpBigAdvantage,tpOverAvg,tpSimilarAvg,tpBelowAvg,strForBigAdv,strForOverAvg, strForSimilarAvg,strForBelowAvg,"单箱税利来看，")
            opanswer5 = buildQ5Ans(opBigAdvantage, opOverAvg,opSimilarAvg, opBelowAvg, strForBigAdv, strForOverAvg, strForSimilarAvg, strForBelowAvg, "单箱利润来看，")
            splitString = '\n\n所以，分析结论是：\n'
            answer5 = tpanswer5 + opanswer5
            # tpBigAdvantage = []   # 单箱税利有较大优势
            # tpOverAvg = []        # 略高于
            # tpSimilarAvg = []        # 持平
            # tpBelowAvg = []       # 低于行业同价类产品
            # opBigAdvantage = []     # 单箱利润有较大优势
            # opOverAvg = []          # 略高于
            # opSimilarAvg = []       # 持平
            # opBelowAvg = []         # 低于行业同价类产品
            cot = buildQ5CoT(countOfcurCigarName,curt,curcorp,tpBigAdvantage,tpOverAvg,tpSimilarAvg,tpBelowAvg,opBigAdvantage, opOverAvg,opSimilarAvg, opBelowAvg,curcorpType,ctStrYan)
            # print(answer5)
            QAdic = {
                "id": countOfQ5,
                "conversations": [{
                    "from": "human",
                    "value": str(question5) + '\n分析一下我司('+str(curcorp)+'）'+ctStrYan+'与其他公司竞品的对比情况。\nA：对以上数据的分析过程和结论是：\n'
                },
                    {"from": "gpt",
                     # "value": splitString + str(answer5)
                     "value": cot + splitString + str(answer5)
                     }]
            }

            totalLen = (len(QAdic['conversations'][0]['value'])+len(QAdic['conversations'][1]['value']))
            if not answer5 == "":
                if totalLen < 8803:     #4036
                    if totalLen > biggestLen:
                        biggestLen = totalLen
                        biggestcorp = str(curcorp) + str(curyear)
                        QA5Max = [QAdic]
                    Q5A5List.append(QAdic)
                    QA5noCoT.append({
                        'instruction': str(question5) + '\n分析一下我司('+str(curcorp)+'）'+ctStrYan+'与其他公司竞品的对比情况。\nA：对以上数据的分析过程和结论是：\n',
                        'output': splitString + str(answer5)
                    })
            countOfQ5 = countOfQ5 + 1

with open('问题五/chatglm2_QA5Biggest.json', 'w', encoding='utf-8') as f:
    json.dump(QA5Max, f, indent=0, ensure_ascii=False)



#         with open('问题五/问题五_2022年分析一下' + str(curcorp) + str(curt) + '与其他公司竞品的对比情况.json', 'w', encoding='utf-8') as f:
#             json.dump(curcorpType, f, indent=0, ensure_ascii=False)  # 格式同q1DataList
# with open('问题五/单个烟的问答/vicuna_与其他公司竞品的对比情况.json', 'w', encoding='utf-8') as f:
#     json.dump(Q5A5List, f, indent=0, ensure_ascii=False)  # 格式同q1DataList
# print(len(Q5A5List))
# print("chekc Q5A5lISTchekc Q5A5lISTchekc Q5A5lISTchekc Q5A5lISTchekc Q5A5lISTchekc Q5A5lIST")
# print(biggestLen)
# print(biggestcorp)
# print('----------------biggestLenabove-----------------')
# idxList = list(range(0, len(Q5A5List)))
# QA5trainIdxList = random.sample(idxList, k=int(len(Q5A5List)*0.85))
# tcount = 0
# vcount = 0
# QA5trainList = []
# QA5valList = []
# for i in range(0, len(Q5A5List)):
#     try:
#         QA5trainIdxList.index(i)
#         QA5trainList.append(Q5A5List[i])
#         tcount = tcount + 1
#     except:
#         vcount = vcount + 1
#         QA5valList.append(Q5A5List[i])

