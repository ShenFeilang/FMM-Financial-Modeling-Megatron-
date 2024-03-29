import json

import pandas as pd
import random
from cigarQuestionGenerator_q1_q5 import corpList2021, corpList2022, corpListSummary2022, optionalCorpList,stdOplCorpList, stringToNumAndUnit

def checkOplExists (optionalCorpList, curcorp):
    for oplC in optionalCorpList:
        if not str(curcorp).find(oplC) == -1:
            return True
    return False

q4DataList = []
noIndus = True
for elem in corpListSummary2022:
    # description = ''
    # if float(elem['公司一类烟税利占比'][:len(elem['公司一类烟税利占比'])-1]) > float(elem['行业一类烟税利占比均值'][:len(elem['行业一类烟税利占比均值'])-1]):
    #     description = '公司一类烟税利占比高于行业均值'
    # else:
    #     description = '公司一类烟税利占比低于行业均值'
    if elem['主体'] == 'nan':
        continue
    if noIndus:
        noIndus = False
        q4DataList.append({'行业整体': {
            "年度": elem["前一年度"],
            '收入': elem['前一年行业整体收入'],
            '销售成本': elem['前一年行业销售成本'],
            '原料成本': elem['前一年行业原料成本'],
            '辅料成本': elem['前一年行业辅料成本'],
            # '能源成本': elem['前一年行业能源成本'],
            # '人力成本': elem['前一年行业人力成本'],
            # '制造成本': elem['前一年行业制造成本'],
            '销售成本占收入比重': elem['前一年行业销售成本占收入比重'],
            '原料成本率': elem['前一年行业原料成本率'],
            '辅料成本率': elem['前一年行业辅料成本率'],
            # '能源成本率': elem['前一年行业能源成本率'],
            # '人力成本率': elem['前一年行业人力成本率'],
            # '制造成本率': elem['前一年行业制造成本率'],
            # '其中：燃料动力': 'BV', '其中：职工薪酬': 'BX', '其中：制造费用': 'BZ'

        }})
        q4DataList.append({'行业整体': {
            "年度": elem["年度"],
            '收入': elem['行业整体收入'],
            '销售成本': elem['行业销售成本'],
            '原料成本': elem['行业原料成本'],
            '辅料成本': elem['行业辅料成本'],
            # '能源成本': elem['行业能源成本'],
            # '人力成本': elem['行业人力成本'],
            # '制造成本': elem['行业制造成本'],
            '销售成本占收入比重': elem['行业销售成本占收入比重'],
            '原料成本率': elem['行业原料成本率'],
            '辅料成本率': elem['行业辅料成本率'],
            # '能源成本率': elem['行业能源成本率'],
            # '人力成本率': elem['行业人力成本率'],
            # '制造成本率': elem['行业制造成本率'],
        }})

    q4DataList.append(
        {elem['主体']: {
            # '主体': elem['主体'],
            "年度": elem["前一年度"],
            '收入': elem['前一年收入'],
            '销售成本': elem['前一年主体销售成本'],
            '原料成本': elem['前一年主体原料成本'],
            '辅料成本': elem['前一年主体辅料成本'],
            # '能源成本': elem['前一年主体能源成本'],
            # '人力成本': elem['前一年主体人力成本'],
            # '制造成本': elem['前一年主体制造成本'],
            '销售成本占收入比重': elem['前一年主体销售成本占收入比重'],
            '原料成本率': elem['前一年主体原料成本率'],
            '辅料成本率': elem['前一年主体辅料成本率'],
            # '能源成本率': elem['前一年主体能源成本率'],
            # '人力成本率': elem['前一年主体人力成本率'],
            # '制造成本率': elem['前一年主体制造成本率'],
            # '其中：燃料动力': 'BV', '其中：职工薪酬': 'BX', '其中：制造费用': 'BZ'

            # '评价': "暂定行业整体形势向好，税利、卷烟结构整体提升；工业税利、利润增幅高于去年同期。2023年1-6月份，工业税利4080亿元,同比增加276亿元,增长8.30%。工业利润1313亿元,同比增加49亿元, 增长7.56%"
    }})
    q4DataList.append(
        {elem['主体']: {
            # '主体': elem['主体'],
            "年度": elem["年度"],
            '收入': elem['收入'],
            '销售成本': elem['主体销售成本'],

            '原料成本': elem['主体原料成本'],

            '辅料成本': elem['主体辅料成本'],
            # '能源成本': elem['主体能源成本'],
            # '人力成本': elem['主体人力成本'],
            # '制造成本': elem['主体制造成本'],
            '销售成本占收入比重': elem['主体销售成本占收入比重'],
            '原料成本率': elem['主体原料成本率'],
            '辅料成本率': elem['主体辅料成本率'],
            # '能源成本率': elem['主体能源成本率'],
            # '人力成本率': elem['主体人力成本率'],
            # '制造成本率': elem['主体制造成本率'],
            # '评价': "暂定行业整体形势向好，税利、卷烟结构整体提升；工业税利、利润增幅高于去年同期。2023年1-6月份，工业税利4080亿元,同比增加276亿元,增长8.30%。工业利润1313亿元,同比增加49亿元, 增长7.56%"
    }})

# print(q4DataList)

def buildQ4Summary(indus, corpdata, curcorp,keylist):
    resList = []
    res = '数据显示，'
    try:
        if float(corpdata[keylist[0]][:-1]) > float(indus[keylist[0]][:-1]):
            res = res + str(curcorp) + keylist[0] + corpdata[keylist[0]] + '高于行业'+ indus[keylist[0]] + '的平均水平'
        else:
            res = res + str(curcorp) + keylist[0] + corpdata[keylist[0]] + '低于行业'+ indus[keylist[0]] + '的平均水平'
        resList = [res]
        res = res + '，其中'
    except:
        res = res + '无法比较' + keylist[0]
        resList.append(res)
        resList = []
        for i in range(0,len(keylist)):
            resList.append('')
        return res, resList
    # aboveAvgList = []
    # belowAvgList = []
    for i in range(1, len(keylist)):
        curkey = keylist[i]
        if corpdata[curkey][:-1] == '非法分母' or indus[curkey][:-1] == '非法分母':
            continue
        if float(corpdata[curkey][:-1]) >= float(indus[curkey][:-1]):
            # aboveAvgList.append(curkey)
            needAppend = str(curkey) + '高于行业均值'
            res += needAppend
            resList.append(str(needAppend))
            res += '，'
        elif float(corpdata[curkey][:-1]) == float(indus[curkey][:-1]):
            needAppend = str(curkey) + '与行业均值持平'
            res += needAppend
            resList.append(str(needAppend))
            res += '，'
        else:
            # belowAvgList.append(curkey)
            needAppend = str(curkey) + '低于行业均值'
            res += needAppend
            resList.append(str(needAppend))
            res += '，'
    if res[len(res)-1] == '，':
        res = res[:-1] + '。'
    # if len(aboveAvgList)>0:
    #     needAppend = '、'.join(aboveAvgList)
    #     # res = res + '、'.join(aboveAvgList)
    #     if len(aboveAvgList) == 1:
    #         needAppend = needAppend + '高于行业均值'
    #     else:
    #         needAppend = needAppend + '均高于行业均值'
    #     resList.append(str(needAppend))
    #     res = res + needAppend
    # if len(belowAvgList)>0:
    #     if len(aboveAvgList)>0:
    #         res = res + '，'
    #     needAppend = '、'.join(belowAvgList)
    #     if len(aboveAvgList)==1:
    #         needAppend += '低于行业均值'
    #     else:
    #         needAppend += '均低于行业均值'
    #     resList.append(str(needAppend))
    #     res += needAppend
    # res = res + '。'
    return res, resList

def build3Steps(curcorp, curyear, item, smData, cmpData, oneSummary):
    cmpItemNum, cmpItemUnit, cmpItemPower = stringToNumAndUnit(cmpData[item])
    smItemNum, smItemUnit, smItemPower = stringToNumAndUnit(smData[item])
    if float(cmpItemNum)*cmpItemPower > float(smItemNum) * smItemPower:
        reasonStr = cmpData[item] + ' > ' + smData[item]
    elif float(cmpItemNum)*cmpItemPower == float(smItemNum) * smItemPower:
        reasonStr = cmpData[item] + ' = ' + smData[item]
    else:
        reasonStr = cmpData[item] + ' < ' + smData[item]
    res =   '找到' + str(curcorp) + str(curyear) + '年的' + item + \
            str(cmpData[item]) + '，' \
            '相比行业整体' + str(curyear) + '年的'+item+ \
            str(smData[item]) +\
            '，因为'+reasonStr+'，所以我输出: ' \
            '"'+oneSummary+'"\n'
    return res
def buildQA4CoT(curyear, curcorp, curdata, QA4SummaryList,compairQuestion,compairList):
    stepOne = build3Steps(curcorp, curyear, compairList[0], curdata[0]['行业整体'], curdata[1][curcorp],
                          QA4SummaryList[0])
    stepTwo = build3Steps(curcorp, curyear, compairList[1], curdata[0]['行业整体'], curdata[1][curcorp],
                          '其中，'+QA4SummaryList[1])
    stepThree = build3Steps(curcorp, curyear, compairList[2], curdata[0]['行业整体'], curdata[1][curcorp],
                            QA4SummaryList[2])
    QA4CoT =    'A：分析过程：给定数据包含'+str(curyear)+'年行业整体和'+str(curcorp)+'的数据。' \
                '要分析'+str(curcorp) + '的' + compairQuestion +'，我需要将'+str(curcorp)+str(curyear)+'年的'+ \
                '、'.join(compairList)+'分别与行业整体'+str(curyear)+'年的'+'、'.join(compairList)+'进行比较。' \
                '我用3个步骤来分析这个问题：\n' \
                'Step1: ' + stepOne +\
                'Step2: ' + stepTwo + \
                'Step3: ' + stepThree
    return QA4CoT


dataset_QA4 = []

# '原料成本率': elem['前一年行业原料成本率'],
# '辅料成本率': elem['前一年行业辅料成本率'],
# '能源成本率': elem['前一年行业能源成本率'],
# '人力成本率': elem['前一年行业人力成本率'],
# '制造成本率': elem['前一年行业制造成本率'],
for idx in range(2,len(q4DataList)):
# for curcorp in corpList2022:
    elem = q4DataList[idx]
    for key in elem:
        curcorp = key
        curyear = elem[key]['年度']
    if curyear == 2021:
        curdata = [q4DataList[0],elem]
    else:
        curdata = [q4DataList[1],elem]
    # preyear = 2021
    if str(curcorp) == 'nan':
        continue
    if (checkOplExists(stdOplCorpList,curcorp)):
        continue
    # if curcorp.find('烟草行业十九') == -1:
    #     continue
    # if not optionalCorpList.__contains__(str(curcorp)):
    #     print(curcorp)
    #     continue
    notuse = 0
    # elem[curcorp]['销售成本占收入比重']
    # q1DataList=[{},{}]

    splitString = '\n\n所以，分析结论是：\n'
    keylist = ['销售成本占收入比重','原料成本率','辅料成本率']
    QA4Summary, QA4SummaryList = buildQ4Summary(curdata[0]['行业整体'],elem[curcorp],curcorp,keylist)
    if QA4Summary.find('无法比较') != -1:
        continue
    QA4CoT = '分析过程：给定数据包含'+str(curyear)+'年行业整体和'+str(curcorp)+'的数据。' \
                 '取出我司（'+str(curcorp)+'）在当前年度（'+str(curyear)+'年）的销售成本占收入比重的值，与当前年度（'+str(curyear)+'年）行业的销售成本占收入比重的值对比' \
                 '若公司的成本占收入比重高于行业的成本占收入比重，输出：' \
                 '"数据显示，'+str(curcorp)+'销售成本占收入比重xx%，高于行业yy%的平均水平"，' \
                 '否则输出：' \
                 '"数据显示，'+str(curcorp)+'销售成本占收入比重xx%，低于行业yy%的平均水平"。' \
                 '再取出我司（'+str(curcorp)+'）在当前年度（'+str(curyear)+'年）的原料成本率、辅料成本率，与当前年度（'+str(curyear)+'年）行业的对应数值值做对比' \
                 '根据比较结果，若公司xx成本率高于行业xx成本率，输出：' \
                 '"其中xx成本率高于行业均值"' \
                 '若公司yy成本率低于行业yy成本率，输出：' \
                 '"yy成本率低于行业均值"。'
    # print(QA4SummaryList)
    compairQuestion = '运行成本与行业对标情况'
    compairList = ['销售成本占收入比重','原料成本率','辅料成本率']
    QA4CoT = buildQA4CoT(curyear, curcorp, curdata, QA4SummaryList,compairQuestion,compairList)
    dataset_QA4.append({
            "id": idx,
            "conversations": [{
                "from": "human",
                "value": 'Q：我司（'+str(curcorp)+'）部分数据如下：' + str(curdata) + '\n请分析我司（'+ str(curcorp)+'）的'+compairQuestion + '。\nA：对以上数据的分析过程和结论是：\n'
            },
                {"from": "gpt",
                 # "value": splitString + QA4Summary
                 "value": QA4CoT + splitString + QA4Summary
                 }]
        })
# idxList = list(range(0, len(dataset_QA4)))
# trainIdxList = random.sample(idxList, k=int(len(dataset_QA4)*0.85))
# tcount = 0
# vcount = 0
# trainList = []
# valList = []
# for i in range(0, len(dataset_QA4)):
#     try:
#         trainIdxList.index(i)
#         trainList.append(dataset_QA4[i])
#         tcount = tcount + 1
#     except:
#         vcount = vcount + 1
#         valList.append(dataset_QA4[i])
# print('问题四训练和验证数量')
# print('train:')
# print(tcount)
# print('val:')
# print(vcount)
# with open('问题四/dataset_QA4_Train.json', 'w', encoding='utf-8') as f:
#     json.dump(trainList, f, indent=0, ensure_ascii=False)   # 格式同q1DataList
# with open('问题四/dataset_QA4_Validation.json', 'w', encoding='utf-8') as f:
#     json.dump(valList, f, indent=0, ensure_ascii=False)  # 格式同q1DataList
# with open('问题四/dataset_QA4.json', 'w', encoding='utf-8') as f:
#     json.dump(dataset_QA4, f, indent=0, ensure_ascii=False)   # 格式同q1DataList
# sss