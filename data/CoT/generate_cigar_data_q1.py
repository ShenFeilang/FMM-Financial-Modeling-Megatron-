import random
import json
import pandas as pd

from cigarQuestionGenerator_q1_q5 import calDif, calDifRate, corpListSummary2022, stdOplCorpList,stringToNumAndUnit

df2021 = pd.read_excel("中国烟草总公司202112量本利.xlsx",dtype=str)
df2022 = pd.read_excel("中国烟草总公司202212量本利.xlsx",dtype=str)

def checkOplExists (optionalCorpList, curcorp):
    for oplC in optionalCorpList:
        if not str(curcorp).find(oplC) == -1:
            return True
    return False

def directFromExcel(year,colName,row):
    if year == 2022:
        tarData = df2022
    else:
        tarData = df2021
    resNum = int(float(tarData[colName][row]))
    if resNum > 1000000 or resNum < -1000000:
        resStr = str(int(resNum/10000))+'万元'
    else:
        resStr = str(int(resNum)) + '元'
    return resStr

q1DataList = []
for elem in corpListSummary2022:
    if checkOplExists(stdOplCorpList, elem['主体']):
        preRawbaseNumTP, preRawunitTP, preRawpowerTP = stringToNumAndUnit(elem['前一年税利'])
        RawbaseNumTP, RawunitTP, RawpowerTP = stringToNumAndUnit(elem['税利'])
        baseNumTP, unitTP, powerTP = stringToNumAndUnit(elem['税利同比增加'])
        baseNumTPR, unitTRP, powerTPR = stringToNumAndUnit(elem['税利同比增长率'])
        preRawbaseNumP, preRawunitP, preRawpowerP = stringToNumAndUnit(elem['前一年利润'])
        RawbaseNumP, RawunitP, RawpowerP = stringToNumAndUnit(elem['利润'])
        baseNumP, unitP, powerP = stringToNumAndUnit(elem['利润同比增加'])
        baseNumPR, unitPR, powerPR = stringToNumAndUnit(elem['利润同比增长率'])
        q1DataList.append([
    {elem['主体']:
        {
            '年度': 2021,
            # '税利': df2021["税利合计"][2],
            # '利润': df2021["营业利润"][2],
            '税利': preRawbaseNumTP + preRawunitTP,
            '税利同比增加': str(int(round(float(baseNumTP)*random.uniform(0.7,1.4),0))) + unitTP,
            '税利同比增长率': str(round(float(baseNumTPR)*random.uniform(0.7,1.4),2)) + '%',
            '利润': preRawbaseNumP + preRawunitP,
            '利润同比增加': str(int(round(float(baseNumP)*random.uniform(0.7,1.4),0))) + unitP,
            '利润同比增长率': str(round(float(baseNumPR)*random.uniform(0.7,1.4),2)) + '%',
            # '一类烟税利': corpListSummary2022[0]['前一年行业一类烟税利'],
            # '二类烟税利': corpListSummary2022[0]['前一年行业二类烟税利'],
            # '三类烟税利': corpListSummary2022[0]['前一年行业三类烟税利'],
            # '四类烟税利': corpListSummary2022[0]['前一年行业四类烟税利'],
            # '五类烟税利': corpListSummary2022[0]['前一年行业五类烟税利'],
            # '其他烟税利': corpListSummary2022[0]['前一年行业其他烟税利'],
            # '一类烟利润': corpListSummary2022[0]['前一年行业一类烟利润'],
            # '二类烟利润': corpListSummary2022[0]['前一年行业二类烟利润'],
            # '三类烟利润': corpListSummary2022[0]['前一年行业三类烟利润'],
            # '四类烟利润': corpListSummary2022[0]['前一年行业四类烟利润'],
            # '五类烟利润': corpListSummary2022[0]['前一年行业五类烟利润'],
            # '其他烟利润': corpListSummary2022[0]['前一年行业其他烟利润'],
        }
    },
    {elem['主体']:
        {
            '年度': 2022,
            # '税利':df2022["税利合计"][2],
            # '利润':df2022["营业利润"][2],
            '税利': str(RawbaseNumTP) + RawunitTP,
            '税利同比增加': baseNumTP+unitTP,
            '税利同比增长率': baseNumTPR + '%',
            '利润': RawbaseNumP + RawunitP,
            '利润同比增加': baseNumP + unitP,
            '利润同比增长率': baseNumPR + '%',
            # '一类烟税利': corpListSummary2022[0]['行业一类烟税利'],
            # '二类烟税利': corpListSummary2022[0]['行业二类烟税利'],
            # '三类烟税利': corpListSummary2022[0]['行业三类烟税利'],
            # '四类烟税利': corpListSummary2022[0]['行业四类烟税利'],
            # '五类烟税利': corpListSummary2022[0]['行业五类烟税利'],
            # '其他烟税利': corpListSummary2022[0]['行业其他烟税利'],
            # '一类烟利润': corpListSummary2022[0]['行业一类烟利润'],
            # '二类烟利润': corpListSummary2022[0]['行业二类烟利润'],
            # '三类烟利润': corpListSummary2022[0]['行业三类烟利润'],
            # '四类烟利润': corpListSummary2022[0]['行业四类烟利润'],
            # '五类烟利润': corpListSummary2022[0]['行业五类烟利润'],
            # '其他烟利润': corpListSummary2022[0]['行业其他烟利润'],
        }
    }
            ]
            )
# print(q1DataList)
# print('q1DataList')
def compairDifRatio(curTPCR, preTPCR):
    if float(curTPCR[:-1]) > (float(preTPCR[:-1])+5):
        TPcmpair = '高于去年同期增长率' + preTPCR + '，整体趋势向好。'
    elif float(curTPCR[:-1]) == (float(preTPCR[:-1])-5):
        TPcmpair = '与去年同期增长率' + preTPCR + '持平。'
    else:
        TPcmpair = '低于去年同期增长率' + preTPCR + '。'
    return TPcmpair

def compairDif(curTPC, curTPCR):
    TPCNum, TPCUnit, TPCPower = stringToNumAndUnit(curTPC)
    if float(TPCNum) > 0:
        resStr = '同比增加' + curTPC + '，增长' + curTPCR
        # todo 以下是为了prompt
        #resStr = '同比增加【' + curTPC + '】，增长【' + curTPCR + '】'
    else:
        # #todo remove abs
        # resStr = '同比减少' + curTPC[1:] + '，降低' + str(abs(float(TPCNum)*TPCPower))+TPCUnit
        # # todo 以下是为了prompt
        # resStr = '同比减少【' + curTPC[1:] + '】，降低【' + str(abs(float(TPCNum) * TPCPower)) + TPCUnit + '】'
        # todo remove abs
        resStr = '同比减少' + curTPC[1:] + '，降低' + curTPCR[1:]
        # todo 以下是为了prompt
        #resStr = '同比减少【' + curTPC[1:] + '】，降低【' + curTPCR[1:] + '】'
    return resStr

def generateQ1Summary(inputDic,corp,forPmpt = False, forq751 = False):
    # 所以，分析结论是：\n行业整体形势向好，税利整体提升26
    # .11 %；工业税利增幅低于去年同期，工业利润增幅高于去年同期。烟草行业今年实现工业税利122万元，同比增加252587元，增长26
    # .11 %，低于去年同期增长率35
    # .72 %。工业利润256889元，同比增加18214元，增长7
    # .63 %，高于去年同期增长率5
    # .88 %，整体趋势向好。
    preDic = inputDic[0][corp]
    curDic = inputDic[1][corp]
    if forq751:
        preDic = inputDic[0]
        curDic = inputDic[1]
    preTPCR = preDic['税利同比增长率']
    prePCR = preDic['利润同比增长率']

    curTP = curDic['税利']
    curTPC = curDic['税利同比增加']
    curTPCR = curDic['税利同比增长率']
    curP = curDic['利润']
    curPC = curDic['利润同比增加']
    curPCR = curDic['利润同比增长率']
    summaryList = []
    pmptSummary = ''
    if float(curTPCR[:-1]) > 5:
        startSummary = '行业整体形势向好，收入整体提升' + curTPCR
    elif float(curTPCR[:-1]) > -5:
        startSummary = '行业收入基本与去年同期持平' + curTPCR
    else:
        startSummary = '行业整体表现不佳，收入整体下降' + curTPCR
    pmptSummary = pmptSummary + '1.' + startSummary + '。\n'
    summaryList.append(str(startSummary))
    startSummary += '；'
    if float(curTPCR[:-1]) > (float(preTPCR[:-1])+5):
        strToAppend = '收入增幅高于去年同期'
    elif float(curTPCR[:-1]) > (float(preTPCR[:-1])-5):
        strToAppend = '收入基本收入与去年同期持平'
    else:
        strToAppend = '收入增幅低于去年同期'
    startSummary += str(strToAppend)
    summaryList.append(str(strToAppend))
    startSummary += '，'
    pmptSummary = pmptSummary + '2.' +  str(strToAppend) + '。\n'
    if float(curPCR[:-1]) > (float(prePCR[:-1])+5):
        strToAppend1 = '利润增幅高于去年同期'
    elif float(curPCR[:-1]) > (float(prePCR[:-1])-5):
        strToAppend1 = '利润基本与去年同期持平'
    else:
        strToAppend1 = '利润增幅低于去年同期'
    pmptSummary = pmptSummary + '3.工业' + str(strToAppend) + '。\n'
    startSummary += str(strToAppend1)
    summaryList.append(str(strToAppend1))
    startSummary += '。'
    TPcmpair = compairDif(curTPC, curTPCR)
    Pcmpair = compairDif(curPC, curPCR)
    TPcmpairR = compairDifRatio(curTPCR, preTPCR)
    PcmpairR = compairDifRatio(curPCR, prePCR)
    # endSummary = '烟草行业今年实现工业税利'+curTP+'，'+TPcmpair+'，' + TPcmpairR
    # endSummary2=       '工业利润'+curP+'，'+Pcmpair+'，' + PcmpairR
    pmptP1 = ''
    endSummary = '本行业今年实现工业税利'+curTP+'，'+TPcmpair+'，'
    endSummary2=       '工业利润'+curP+'，'+Pcmpair+'。'
    pmptP1 += '本行业今年实现工业税利【'+curTP+'】，'+TPcmpair+'。\n'
    pmptP1 += '工业利润【'+curP+'】，'+Pcmpair+'。'
    QA1Summary = startSummary + endSummary + endSummary2
    summaryList.append(str(endSummary))
    summaryList.append(str(endSummary2))
    if forPmpt:
        return pmptSummary,pmptP1
    return QA1Summary, summaryList


def buildSomeSteps(curcorp, curyear,preyear, cmpRateKey, smRateKey, smData, cmpData, oneSummary, compairOneExtra = False,
                   noReason = False, cmpRateKey2 = '0', cmpRateKey3 = '0', extraOne = False):
    cmpDStr = str(cmpData[cmpRateKey])
    smDStr = str(smData[smRateKey])
    cmpItemNum, cmpItemUnit, cmpItemPower = stringToNumAndUnit(cmpDStr)
    smItemNum, smItemUnit, smItemPower = stringToNumAndUnit(smDStr)
    if float(cmpItemNum)*cmpItemPower > float(smItemNum) * smItemPower:
        reasonStr = cmpDStr + ' > ' + smDStr
    elif float(cmpItemNum)*cmpItemPower == float(smItemNum) * smItemPower:
        reasonStr = cmpDStr + ' = ' + smDStr
    else:
        reasonStr = cmpDStr + ' < ' + smDStr

    check8percent = (float(cmpItemNum)*cmpItemPower) - (float(smItemNum)*smItemPower)
    if check8percent > 8.0:
        operatorStr = '>'
    elif check8percent == 8.0:
        operatorStr = '='
    else:
        operatorStr = '<'
    if compairOneExtra:
        return operatorStr
    if noReason:
        res =   '找到' + str(curcorp) + str(curyear) + '年的' +cmpRateKey2+str(cmpData[cmpRateKey2]) + '，'+\
                cmpRateKey3+str(cmpData[cmpRateKey3]) + '，' +\
                cmpRateKey + \
                cmpDStr +  \
                '，所以我输出：' \
                '"'+oneSummary+'"\n'
    else:
        if extraOne:
            res =   '找到' + str(curcorp) + str(curyear) + '年的' + cmpRateKey2+str(cmpData[cmpRateKey2]) + '，'+\
                    cmpRateKey + \
                    cmpDStr + '，' \
                    '相比' + str(curcorp) + str(preyear) + '年的' + cmpRateKey + \
                    smDStr + \
                    '，因为'+reasonStr+'，所以我输出: ' \
                    '"'+oneSummary+'"\n'
        else:
            res =   '找到' + str(curcorp) + str(curyear) + '年的' + cmpRateKey + \
                    cmpDStr + '，' \
                    '相比' + str(curcorp) + str(preyear) + '年的' + cmpRateKey + \
                    smDStr + \
                    '，因为'+reasonStr+'，所以我输出: ' \
                    '"'+oneSummary+'"\n'
    return res


def newGenerateQA1CoT(inputDic,corp,compairList,summaryList):
    preYear = str(inputDic[0][corp]['年度'])
    curYear = str(inputDic[1][corp]['年度'])
    fakeSmData = inputDic[0][corp]
    fakeCmpData = inputDic[1][corp]
    res =    'A：分析过程：给定数据包含'+preYear+'、'+curYear+'两个年份，默认当前年度为最近的年份，也就是'+curYear+'年。' \
                '要分析'+corp+'今年的运行情况，我需要找到'+corp+curYear+'的'+'、'.join(compairList)+'，分别与'+\
                preYear+'的'+'、'.join(compairList)+'进行比较。' \
                '我用5个步骤来分析这个问题：\n'
    for i in range(5):
        if i == 0 :
            stepConclusion = buildSomeSteps(corp, curYear,preYear, compairList[i], compairList[i], fakeSmData, fakeCmpData,
                                    summaryList[i],cmpRateKey2='税利同比增长率',extraOne=True)
        if (i==1) or (i ==2):
            stepConclusion = buildSomeSteps(corp, curYear,preYear, compairList[i], compairList[i], fakeSmData, fakeCmpData,
                                    summaryList[i])
        if i == 3:
            stepConclusion = buildSomeSteps(corp, curYear, preYear, compairList[i-2], compairList[i-2], fakeSmData,
                                            fakeCmpData,
                                            summaryList[i],noReason=True,cmpRateKey2='税利',cmpRateKey3='税利同比增加')
        if i ==4:
            stepConclusion = buildSomeSteps(corp, curYear, preYear, compairList[i-2], compairList[i-2], fakeSmData,
                                            fakeCmpData,
                                            summaryList[i],noReason=True,cmpRateKey2='利润',cmpRateKey3='利润同比增加')
        res = res + 'Step' + str(i+1) + '：' + stepConclusion
    return res

def generateQA1CoT(inputDic,corp):
    preYear = str(inputDic[0][corp]['年度'])
    curYear = str(inputDic[1][corp]['年度'])
    QA1CoT = '分析过程：给定数据包含'+preYear+'、'+curYear+'两个年份，默认当前年度为最近的年份，也就是'+curYear+'年。' \
             '需要取出行业整体在当前年度（'+curYear+'年）的税利、利润相比上一个年度（'+preYear+'年）的同比增加、同比增长率' \
             '，并给出评价。评价需要先描述今年的税利变化，接着对比今年和去年的税利变化，最后对比今年和去年的利润变化。' \
             '若今年税利大于去年税利，今年的税利变化描述为“行业整体形势向好，税利整体提升xx%”，' \
             '否则描述为“行业整体表现不佳，税利整体下降xx%”。' \
             '对比今年和去年的税利变化，若今年税利同比增长率大于去年税利同比增长率就这样描述：' \
             '"烟草行业今年实现工业税利xx万元，同比增加xx万元，增长率xx%，高于去年同期增长率yy%，整体趋势向好。"，' \
             '若今年税利同比增长率小于去年税利同比增长率就这样描述：' \
             '"草行业今年实现工业税利xx万元，同比增加xx万元，增长率xx%，低于去年同期增长率yy%。"，' \
             '当今年税利同比增长率等于去年税利同比增长率的时候这样描述：' \
             '“烟草行业今年实现工业税利xx万元，同比增加xx万元，增长率xx%，与去年同期增长率yy%持平。”。' \
             '对比今年和去年的利润变化参照对比今年和去年的税利变化的描述方式。\n'
    return QA1CoT


def generateQA1(inputDic,idx):
    splitString = '\n\n所以，分析结论是：\n'
    corp = ''
    for key in inputDic[0]:
        corp = key
    summary, summaryList = generateQ1Summary(inputDic, corp)
    compairList = ['税利', '税利同比增长率', '利润同比增长率']
    QA1CoT = newGenerateQA1CoT(inputDic,corp,compairList, summaryList)
    # QA1CoT = generateQA1CoT(inputDic, corp)
    resDic = {
        "id": idx,
        "conversations": [{
            "from": "human",
            "value": 'Q：本行业的近两年的整体数据如下：' + str(inputDic) + '\n请分析本行业今年的运行情况。' + '\nA：对以上数据的分析过程和结论是：\n'
        },
            {"from": "gpt",
             # "value": splitString + generateSummary(inputDic, corp)
            "value": QA1CoT + splitString + summary
             }]
    }
    return resDic

def qa1PmptGenerator(inputDic):
    corp = ''
    for key in inputDic[0]:
        corp = str(key)
    preYear = str(inputDic[0][corp]['年度'])
    curYear = str(inputDic[1][corp]['年度'])
    pmptData = inputDic[1]
    pmptData[corp].__setitem__('去年税利同比增长率', inputDic[0][corp]['税利同比增长率'])
    pmptData[corp].__setitem__('去年利润同比增长率', inputDic[0][corp]['利润同比增长率'])
    pmptDStr = str([pmptData])
    pmpt =    '你是一个行业报告生成器，我给你一份报告模版，和需要注入的数据，请根据以下报告模版和需要注入的数据，生成新的报告。' \
              '不要漏掉模板中的项目，并确保项目使用中文中括号强调。\n\n' \
              '"""\n' \
              'xx行业总体分析报告\n' \
              '【相关数据】\n' \
              'xxxx年\n' \
              '工业税利xxx万元（元），同比增长（或降低）xxx万元（元），同比增长（或降低）xxx个百分点。\n' \
              '工业利润xxx万元（元），同比增长（或降低）xxx万元（元），同比增长（或降低）xxx个百分点。\n' \
              'xxxx年整体' \
              '行业营收XX元，同比增加XX元，增长XX%' \
              '行业利润。。。。' \
              '【分析总结】\n' \
              '1.总结行业的税利变化，如：行业整体形势向好，收入整体提升\n' \
              '行业整体形式向好，营收和利润整体提升，且增幅高于去年同期。' \
              '2.总结行业的税利变化趋势，与去年同期相比的变化，如：利润增幅高于去年同期\n' \
              '3.总结行业的利润变化趋势，与去年同期相比的变化，如：利润增幅高于去年同期\n' \
              '"""\n' \
              '待注入数据:\n' + pmptDStr + '\n' \
              '请按照模版生成完整报告，不要漏掉模板中的项目，并确保项目使用中文中括号强调，这很重要。'
    return pmpt

def QA1promptGenerator(inputDic, idx):
    splitString = '\n\n所以，分析结论是：\n'
    corp = ''
    for key in inputDic[0]:
        corp = key
    summary,pmptP1 = generateQ1Summary(inputDic, corp, forPmpt=True)
    # compairList = ['税利', '税利同比增长率', '利润同比增长率', '税利同比增长率', '利润同比增长率']
    # QA1CoT = newGenerateQA1CoT(inputDic,corp,compairList, summaryList)
    # QA1CoT = generateQA1CoT(inputDic, corp)
    QA1Pmpt = qa1PmptGenerator(inputDic)
    pmptValue = corp + '总体分析报告\n【相关数据】\n' + pmptP1 + '\n【分析总结】\n'+ summary
    resDic = {
        "id": idx,
        "conversations": [{
            "from": "human",
            "value": QA1Pmpt
        },
            {"from": "gpt",
             # "value": splitString + generateSummary(inputDic, corp)
            "value": pmptValue
             }]
    }
    return resDic
    return {}
dataset_QA1= []
QA1PmptList = []
for idx in range(0,len(q1DataList)):
    # 在生成q1DataList的时候已经企业做了筛选
    dataset_QA1.append(generateQA1(q1DataList[idx], idx))
    QA1PmptList.append(QA1promptGenerator(q1DataList[idx],idx))

def vicunaDataToChatglm2Data(vicunaDataList):
    chatglm2DataList = []
    for elem in vicunaDataList:
        chatglm2DataList.append(
            {"instruction": elem['conversations'][0]['value'], "output": elem['conversations'][1]['value']})
    return chatglm2DataList

# with open('问题一/chatglm2_pmpt.json', 'w', encoding='utf-8') as f:
#     json.dump(QA1PmptList, f, indent=0, ensure_ascii=False)   # 格式同q1DataList

data_QA1_chatglm = vicunaDataToChatglm2Data(dataset_QA1)
with open('问题一/chatglm2_QA1.json', 'w', encoding='utf-8') as f:
    json.dump(data_QA1_chatglm, f, indent=0, ensure_ascii=False)
with open('问题一/epmVal.json', 'w', encoding='utf-8') as f:
    json.dump(data_QA1_chatglm, f, indent=0, ensure_ascii=False)

# print(dataset_QA1)








# print(q1DataList)



# QA1
# 问：帮我分析烟草行业今年的税利运行情况。
# 答：行业整体形势向好，税利整体提升（给同比）；工业税利、利润增幅高于去年同期。
# 2023年1-6月份，工业税利4080亿元,同比增加276亿元,增长8.30%。工业利润1313亿元,同比增加49亿元, 增长7.56%。

# QA2
# 问：分析一下福建中烟的行业效益情况
# 答：2023年1-6月份福建中烟税利1235亿元，同比增加26亿元，增长6.5%，低于行业8.3%的平均水平；
# 利润1067亿元，同比增加24亿元，增长5.4%，低于行业7.56%的平均水平。
# 单箱税利14,164亿元，行业均值19,642亿元，公司增幅8.85%，高于行业增幅的6.83%；
# 单箱利润1,413，行业均值3,001，公司增幅16.66%，高于行业的10.17%。


# QA3
# 问：看一下龙烟公司卷烟结构的行业对标情况
# 问：看一下龙烟公司和夏烟对标情况
# 看一下龙烟公司和夏烟对标情况
# 答：一类烟公司税利占比18%，低于行业均值32%；
# 二类烟公司税利占比32%，高于行业均值20%；
# 三类烟公司税利占比37%，低于行业均值39%；
# 四类烟公司税利占比11%，低于行业均值8%；
# 五类烟公司税利占比1%，与行业均值持平；
# 一至三类烟公司税利占比87%，低于行业均值91%。
# 我司一类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间。


# QA4
# 问：看一下公司成本情况与行业的对标情况
# 问：看一下龙烟公司成本情况与夏烟公司的对标情况
#
# 答：数据显示，福建中烟销售成本占收入比重30.48%，高于行业26.28%的平均水平，其中原料成本率、辅料成本率均高于行业均值。


# QA5
# 问：分析一下我司一类烟与其他公司竞品的对比情况
# 答：从单箱税利来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；豪情、白狼、软富健略高于行业均值；其余10个产品均低于行业同价类产品。
# 从单箱利润来看，锋芒、红狼、软混与行业同价类产品相比具有较大优势；豪情、白狼、软富健与行业均值持平；其余10个产品均低于行业同价类产品。




