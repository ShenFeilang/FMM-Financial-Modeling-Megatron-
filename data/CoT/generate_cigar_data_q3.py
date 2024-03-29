import copy
import json
import pandas as pd
from cigarQuestionGenerator_q1_q5 import corpList2021, corpList2022, corpListSummary2022,optionalCorpList,stringToNumAndUnit


def checkOplExists (optionalCorpList, curcorp):
    for oplC in optionalCorpList:
        if not str(curcorp).find(oplC) == -1:
            return True
    return False

# def stringToNumAndUnit(numString,unitPowerCandidateList=[['亿元',100000000],['万元',10000],['元',1]]):
#     rawNumStr = '999999999.99'
#     unit = '暂无单位'
#     power = 1
#     for tempUnit in unitPowerCandidateList:
#         if not numString.find(tempUnit[0]) == -1:
#             unit = tempUnit[0]
#             rawNumStr = numString[:-len(unit)]
#             power = tempUnit[1]
#             break
#     return rawNumStr, unit, power


def get_q3DataList(cmp):
    q3DataList = []
    for elem in corpListSummary2022:
        # description = ''
        # if float(elem['公司一类烟税利占比'][:len(elem['公司一类烟税利占比'])-1]) > float(elem['行业一类烟税利占比均值'][:len(elem['行业一类烟税利占比均值'])-1]):
        #     description = '公司一类烟税利占比高于行业均值'
        # else:
        #     description = '公司一类烟税利占比低于行业均值'
        if elem['主体'] == cmp:
            q3DataList.append(
                {'行业整体': {
                    "年度": elem['前一年度'],
                    '税利': elem['前一年行业整体税利'],
                    '一类烟税利': elem['前一年行业一类烟税利'],
                    '二类烟税利': elem['前一年行业二类烟税利'],
                    '三类烟税利': elem['前一年行业三类烟税利'],
                    '四类烟税利': elem['前一年行业四类烟税利'],
                    '五类烟税利': elem['前一年行业五类烟税利'],
                    '其他烟税利': elem['前一年行业其他烟税利'],
                    '一类烟利润': elem['前一年行业一类烟利润'],
                    '二类烟利润': elem['前一年行业二类烟利润'],
                    '三类烟利润': elem['前一年行业三类烟利润'],
                    '四类烟利润': elem['前一年行业四类烟利润'],
                    '五类烟利润': elem['前一年行业五类烟利润'],
                    '其他烟利润': elem['前一年行业其他烟税利'],
                }}
            )
            q3DataList.append(
                {'行业整体': {
                    "年度": elem['年度'],
                    '税利': elem['行业整体税利'],
                    '一类烟税利': elem['行业一类烟税利'],
                    '二类烟税利': elem['行业二类烟税利'],
                    '三类烟税利': elem['行业三类烟税利'],
                    '四类烟税利': elem['行业四类烟税利'],
                    '五类烟税利': elem['行业五类烟税利'],
                    '其他烟税利': elem['行业其他烟税利'],
                    '一类烟利润': elem['行业一类烟利润'],
                    '二类烟利润': elem['行业二类烟利润'],
                    '三类烟利润': elem['行业三类烟利润'],
                    '四类烟利润': elem['行业四类烟利润'],
                    '五类烟利润': elem['行业五类烟利润'],
                    '其他烟利润': elem['行业其他烟税利'],
                }}
            )
            q3DataList.append({elem['主体']
            : {
                    # '主体': elem['主体'],、
                    '年度': elem['前一年度'],
                    '税利': elem['前一年税利'],
                    '公司一类烟税利': elem['前一年公司一类烟税利'],
                    '公司二类烟税利': elem['前一年公司二类烟税利'],
                    '公司三类烟税利': elem['前一年公司三类烟税利'],
                    '公司四类烟税利': elem['前一年公司四类烟税利'],
                    '公司五类烟税利': elem['前一年公司五类烟税利'],
                    '公司其他烟税利': elem['前一年公司其他烟税利'],
                    '公司一类烟利润': elem['前一年公司一类烟利润'],
                    '公司二类烟利润': elem['前一年公司二类烟利润'],
                    '公司三类烟利润': elem['前一年公司三类烟利润'],
                    '公司四类烟利润': elem['前一年公司四类烟利润'],
                    '公司五类烟利润': elem['前一年公司五类烟利润'],
                    '公司其他烟利润': elem['前一年公司其他烟利润'],

                    # '同比增加': elem['同比增加'],
                    # '同比增长率': elem['同比增长率'],
                    # '评价': "暂定行业整体形势向好，税利、卷烟结构整体提升；工业税利、利润增幅高于去年同期。2023年1-6月份，工业税利4080亿元,同比增加276亿元,增长8.30%。工业利润1313亿元,同比增加49亿元, 增长7.56%"
                }})
            q3DataList.append({elem['主体']
            : {
                    # '主体': elem['主体'],
                    '年度': elem['年度'],
                    '税利': elem['税利'],
                    '公司一类烟税利': elem['公司一类烟税利'],
                    '公司二类烟税利': elem['公司二类烟税利'],
                    '公司三类烟税利': elem['公司三类烟税利'],
                    '公司四类烟税利': elem['公司四类烟税利'],
                    '公司五类烟税利': elem['公司五类烟税利'],
                    '公司其他烟税利': elem['公司其他烟税利'],
                    '公司一类烟利润': elem['公司一类烟利润'],
                    '公司二类烟利润': elem['公司二类烟利润'],
                    '公司三类烟利润': elem['公司三类烟利润'],
                    '公司四类烟利润': elem['公司四类烟利润'],
                    '公司五类烟利润': elem['公司五类烟利润'],
                    '公司其他烟利润': elem['公司其他烟利润'],

                    # '同比增加': elem['同比增加'],
                    # '同比增长率': elem['同比增长率'],
                    # '评价': "暂定行业整体形势向好，税利、卷烟结构整体提升；工业税利、利润增幅高于去年同期。2023年1-6月份，工业税利4080亿元,同比增加276亿元,增长8.30%。工业利润1313亿元,同比增加49亿元, 增长7.56%"
                }})
    return q3DataList


def generate_dict_from_year(DataList):
    new_dict = {}
    for data in DataList:
        for cmp in data.keys():
            inf = data[cmp]
            for key in inf.keys():
                amount = str(inf[key])
                if '元' in amount:
                    if '万元' in amount:
                        continue
                    elif '万元' not in amount:
                        temp = int(amount.strip('元')) / (10 ** 4)
                        inf[key] = str(temp) + '万元'
            time = inf['年度']
            new_dict[f'{cmp}_{time}'] = inf
    return new_dict


# 公司 和 行业整体 对比
def cmp_sm_compare_rate(cmp_rate, sm_rate, type):
    if type[:2] =='公司':
        typeForSent = type[2:]
    else:
        typeForSent = str(type)
    if cmp_rate > sm_rate:
        part1 = f'高于行业均值{sm_rate}%。'
        if cmp_rate - sm_rate >= 8 and type == '公司一类烟税利':
            part2 = f'我司{typeForSent}远高于行业平均水平，说明我司卷烟结构相对已经比较优化。'
        else:
            part2 = ''
    elif cmp_rate < sm_rate:
        part1 = f'低于行业均值{sm_rate}%。'
        if sm_rate - cmp_rate >= 8 and type == '公司一类烟税利':
            part2 = f'我司{typeForSent}远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间。'
        else:
            part2 = ''
    else:
        part1 = f'与行业均值持平。'
        part2 = ''

    return part1, part2


# 获取行业整体数据
def get_data_sm(data_dict, sm, type_list, unit_list, pre_time, cur_time):
    resDic = {}
    for curOrPre in [pre_time, cur_time]:
        sm_inf_cur = data_dict[f'{sm}_{curOrPre}']
        cmp_sum_cur_BaseNum, cmpCurUnit, cmpCurPower = stringToNumAndUnit(sm_inf_cur['税利'])
        sm_sum_cur = float(cmp_sum_cur_BaseNum) * cmpCurPower
        sm_rate_dict = {}
        for type in type_list:
            if type == '一至三类烟税利':
                continue
            curBasenum, curunit, curpower = stringToNumAndUnit(sm_inf_cur[type])
            cur_inf = float(curBasenum) * curpower
            sm_rate_dict[type] = round((cur_inf/ abs(sm_sum_cur)) * (10 ** 2), 2)
        sm_rate_dict['一至三类烟税利'] = round(sm_rate_dict['一类烟税利'] + sm_rate_dict['二类烟税利'] + sm_rate_dict['三类烟税利'], 2)
        resDic.__setitem__(str(curOrPre),sm_rate_dict)
    return resDic


# 获取公司数据
def get_data_cmp(data_dict, cmp, type_list, unit_list, pre_time, cur_time):
    resDic = {}
    for curOrPre in [pre_time,cur_time]:
        cmp_inf_cur = data_dict[f'{cmp}_{curOrPre}']
        cmp_sum_cur_BaseNum, cmpCurUnit, cmpCurPower = stringToNumAndUnit(cmp_inf_cur['税利'])
        cmp_sum_cur = float(cmp_sum_cur_BaseNum) * cmpCurPower
        cmp_rate_dict = {}
        for type in type_list:
            if type == '一至三类烟公司税利占比':
                continue
            # cur_inf = float(cmp_inf_cur[type].strip(unit))
            curBasenum, curunit, curpower = stringToNumAndUnit(cmp_inf_cur[type])
            cur_inf = float(curBasenum) * curpower
            cmp_rate_dict[type] = round((cur_inf / abs(cmp_sum_cur)) * (10 ** 2), 2)
        cmp_rate_dict['一至三类烟公司税利占比'] = round(cmp_rate_dict['公司一类烟税利'] + cmp_rate_dict['公司二类烟税利'] + cmp_rate_dict[
            '公司三类烟税利'], 2)
        resDic.__setitem__(str(curOrPre),cmp_rate_dict)
    return resDic


# 生成句式
# 例句
# XXX占比XX%，低于/高于行业均值XX%。XXX烟税利占比XX%，低于/高于行业均值XX%。...
# 我司XXX远低于/远高于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间/说明我司卷烟结构相对已经比较优化。
def generate_sent_compare_year(cmp_rate, sm_rate, type):

    compare_part1, compare_part2 = cmp_sm_compare_rate(cmp_rate, sm_rate, type)
    if type[:2] == '公司':
        typeStr = type[2:-2] + '公司税利占比'
    else:
        typeStr = type
    if type[:3] == '一至三':
        typeStr = type + '之和为'
    sent_part1 = f'{typeStr}{cmp_rate}%，{compare_part1}'
    sent_part2 = compare_part2

    return sent_part1, sent_part2

def buildSomeSteps(curcorp, curyear, cmpRateKey, smRateKey, smData, cmpData, oneSummary, compairOneExtra = False):
    cmpDStr = str(cmpData[cmpRateKey])+'%'
    smDStr = str(smData[smRateKey])+'%'
    cmpItemNum, cmpItemUnit, cmpItemPower = stringToNumAndUnit(cmpDStr)
    smItemNum, smItemUnit, smItemPower = stringToNumAndUnit(smDStr)
    if (float(cmpItemNum)*cmpItemPower) > (float(smItemNum) * smItemPower):
        reasonStr = cmpDStr + ' > ' + smDStr
    elif (float(cmpItemNum)*cmpItemPower) == (float(smItemNum) * smItemPower):
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
    res =   '找到' + str(curcorp) + str(curyear) + '年的' + cmpRateKey + \
            cmpDStr + '，' \
            '相比行业整体' + str(curyear) + '年的' + cmpRateKey + \
            smDStr +  \
            '，因为'+reasonStr+'，所以我输出: ' \
            '"'+oneSummary+'"\n'
    return res

def buildNewCoTWithSteps(cmp, cur_time, pre_time, sm_rate_dict, cmp_rate_dict,summaryList):
    # f'{cmp}{cur_time}卷烟结构的行业对标情况。{blank}'
    res = ''
    cmpRateKeyList = []
    smRateKeyList = []
    for key in sm_rate_dict[cur_time]:
        smRateKeyList.append(key)
    for key in cmp_rate_dict[cur_time]:
        cmpRateKeyList.append(key)
    res =   'A：分析过程：\n' + '给定数据包含' + str(pre_time) + '、' + str(
        cur_time) + '两个年份，问题中提到了具体的年份' + str(cur_time) + '。' \
            '要分析' + str(cmp) + str(cur_time) + '卷烟结构的行业对标情况，我需要将'+ str(cmp)+ str(cur_time) + '的' +\
            '、'.join(cmpRateKeyList) + '，分别与行业整体的' + '、'.join(smRateKeyList) + '进行比较，' \
            '最后对一类烟税利进行单独评价。' \
            '我用7个步骤来分析这个问题：\n'
    for i in range(0,len(cmpRateKeyList)):
        curStep = buildSomeSteps(str(cmp), str(cur_time), cmpRateKeyList[i], smRateKeyList[i],sm_rate_dict[cur_time],
                                 cmp_rate_dict[cur_time],
                          summaryList[i])
        res = res + 'Step' + str(i+1)+'：' + curStep
    compairOperator = buildSomeSteps(str(cmp), str(cur_time), cmpRateKeyList[0], smRateKeyList[0],sm_rate_dict[cur_time],
                                     cmp_rate_dict[cur_time], summaryList[0], compairOneExtra=True)
    reasonOneExtra = 'Step'+str(len(cmpRateKeyList)+1)+'：因为(一类烟公司税利占比-行业一类烟税利占比)' + compairOperator + '8%，所以我输出：'
    reasonOneExtra += summaryList[len(summaryList)-1] + '\n'
    res += reasonOneExtra
    return res

def buildCcmpParaGraphot(pre_time, cur_time, cmp, q3_datalist, type_list_sm, type_list_cmp,sm_rate_dict,cmp_rate_dict):
    # resStr = '\n\nCoT:默认年份是最新年份。问题中包含具体年份'+cur_time+'，因此回答该问题需要分别找出' + cur_time + cmp + '所有价类的烟的税利占比和'+cur_time+'行业所有价类的烟的税利占比，再将这两个税利占比进行比较。'
    # few_shot = '比较的规则是：一类烟烟税利占比>行业一类烟税利占比均值，则描述为高于行业均值，否则描述为低于行业均值。\n' \
    #            '二、三、四、五类的逻辑与一类烟一致。\n' \
    #            '将公司一、二、三类烟税利占比的和，与行业一、二、三类烟税利占比均值对比，描述逻辑和一类烟一致。\n' \
    #            '最后，如果公司一类烟税利占比-行业一类烟占比均值 >8%,则描述为“我司一类烟税利远高于行业平均水平，说明我司卷烟结构相对已经比较优化”；' \
    #            '如果公司一类烟税利占比-行业一类烟占比均值<-8%,则描述为“我司一类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间，' \
    #            '否则与行业水平相当。'
    # resStr = resStr + few_shot
    count = 1
    # for dic in q3_datalist: # dic = {行业: {}}
    #     for key in dic: # key = 行业
    #         curStr = '第' + str(count) + '条数据是关于' + str(dic[key]['年度']) + str(key)+ '的，'
    #         if str(dic[key]['年度']) == str(cur_time):    # 对上了同一年
    #             if key == '行业整体':
    #                 curStr = curStr + '是问题相关的数据，根据该数据可以得出：'
    #                 for typekey in type_list_sm:
    #                     curStr = curStr + '行业' + str(typekey) + '占比' + str(sm_rate_dict[typekey]) + '%；'
    #                 curStr = curStr[:-1] + '。'
    #             elif key == cmp:
    #                 curStr = curStr + '是问题相关的数据，根据该数据可以得出：'
    #                 for typekey in type_list_cmp:
    #                     curStr = curStr + str(cmp) + str(typekey) + '占比' + str(cmp_rate_dict[typekey]) + '%；'
    #                 curStr = curStr[:-1] + '。'
    #             else:
    #                 curStr = curStr + '不是问题问的公司或行业，忽略。'
    #         else:
    #             curStr = curStr + '不是问题问的年度，忽略。'
    #         resStr = resStr + str(curStr)
    #     count = count + 1
    LBresStr = '分析过程：\n' + '给定数据包含' + str(pre_time) + '、' + str(cur_time) + '两个年份，问题中提到了具体的年份'+ str(cur_time) + '。'
    LBresStr = LBresStr +'卷烟结构的比较规则是：\n当前公司的x类烟公司税利占比xx%与行业的x类烟税利占比yy%比较，若公司的税利占比大于行业的税利占比，' \
                         '输出：' \
                          '"我司的x类烟公司税利占比xx%，高于行业均值yy%"，' \
                         '否则输出："我司的x类烟公司税利占比xx%，低于行业均值yy%"；'
    LBresStr = LBresStr + '对一类烟、二类烟、三类烟的税率占比求和，进行单独比较，若公司的一至三类烟占比之和大于行业一至三类烟占比之和，输出：' \
                          '"我司的一至三类烟公司税利占比之和为xx%，高于行业均值yy%"，' \
                          '否则输出："我司的一至三类烟公司税利占比之和为xx%，低于行业均值yy%"。\n'
    LBresStr = LBresStr + '对一类烟税利进行单独比较，如果(当前公司的一类公司烟税利占比-行业的一类烟税利占比)>8%，' \
                          '则输出"我司一类烟公司税利占比远高于行业平均水平，说明我司卷烟结构相对已经比较优化"，' \
                          '(当前公司的一类烟公司税利占比 - 行业一类烟的税利占比)< -8%，则输出："我司一类烟公司税利占比远低于行业平均水平，' \
                          '说明我司卷烟结构提升方面仍有较大提升空间"，其它情况，则输出"我司一类烟公司税利与行业水平相当"。\n'
    indusParaGraph =  str(cur_time) + '年行业整体的数据是，'
    for elem in sm_rate_dict:
        indusParaGraph = indusParaGraph + '行业' + elem + str(sm_rate_dict[elem]) + '%；'
    indusParaGraph = indusParaGraph[:-1] + '\n'
    cmpParaGraph = str(cur_time) + '年当前公司（' + str(cmp) + '）的数据是'
    for elem in cmp_rate_dict:
        cmpParaGraph = cmpParaGraph + '行业' + elem + str(cmp_rate_dict[elem]) + '%；'
    cmpParaGraph = cmpParaGraph[:-1] + '。'
    LBresStr= LBresStr + indusParaGraph + cmpParaGraph

    return LBresStr+'\n'
# 总体数据生成
def generate_Q3(q3_datalist, cmp, sm, prompt, type_list_sm, type_list_cmp, unit_list, pre_time, cur_time, id):
    global maxLen
    # print(q3_datalist)
    q3_datalist_copy = copy.deepcopy(q3_datalist)
    data_dict = generate_dict_from_year(q3_datalist_copy)
    sm_rate_dict = get_data_sm(data_dict, sm, type_list_sm, unit_list, pre_time, cur_time)
    # 行业占比
    # sm_rate_dict:
    # {'一类烟税利': 87.49, '二类烟税利': 29.15, '三类烟税利': 23.81, '四类烟税利': 0.74, '五类烟税利': 0.05,
    #  '其他烟税利': 0.29}
    cmp_rate_dict = get_data_cmp(data_dict, cmp, type_list_cmp, unit_list, pre_time, cur_time)
    # 公司各类占比
    # cmp_rate_dict:
    # {'公司一类烟税利': 57.3, '公司二类烟税利': 11.93, '公司三类烟税利': 30.64, '公司四类烟税利': 0.14,
    #  '公司五类烟税利': 0.0, '公司其他烟税利': 0.0}
    # 把cmp_rate_dict加入到q3_datalist里面
    for q3_data in q3_datalist:
        for q3key in q3_data:   # q3key是行业整体或者公司名称
            if q3key == cmp:
                for key in cmp_rate_dict[str(q3_data[q3key]['年度'])]:
                    if key[:2] == '公司':
                        keyStr = key[2:-2] + '公司税利占比'
                    else:
                        keyStr = key
                    q3_data[q3key].__setitem__(keyStr, str(cmp_rate_dict[str(q3_data[q3key]['年度'])][key])+'%')
                # break
            if q3key == sm:
                for key in sm_rate_dict[str(q3_data[q3key]['年度'])]:
                    q3_data[q3key].__setitem__(key+'占比', str(sm_rate_dict[str(q3_data[q3key]['年度'])][key])+'%')
                # break
    summary_part1 = '我司（'+ str(cmp)+'）的'
    summary_part2 = ''
    summaryList = []
    for type_sm, type_cmp, unit in zip(type_list_sm, type_list_cmp, unit_list):
        sent_part1, sent_part2 = generate_sent_compare_year(cmp_rate_dict[str(cur_time)][type_cmp], sm_rate_dict[str(cur_time)][type_sm], type_cmp)
        summaryList.append(str(sent_part1))
        summary_part1 += sent_part1
        summary_part2 += sent_part2
        # 这部分不用改，这是最后的结论 我司公司一类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间。我司公司二类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间。
    summaryList.append(summary_part2)
    cot = buildNewCoTWithSteps(cmp, cur_time, pre_time, sm_rate_dict, cmp_rate_dict,summaryList)
    # cot = buildCcmpParaGraphot(pre_time, cur_time,cmp,q3_datalist,type_list_sm,type_list_cmp,sm_rate_dict[str(cur_time)],cmp_rate_dict[str(cur_time)])
    q3_data_dic = {}    # 预期是{行业： [{行业:{}},{行业:{}}], 公司： [{公司:{}},{公司:{}}]}
    for q3dic in q3_datalist:
        for key in q3dic:
            if q3_data_dic.__contains__(key):
                q3_data_dic[key].append(q3dic)
            else:
                q3_data_dic.__setitem__(key, [q3dic])
    list_of_sublist_q3_datalist = [] # 预期是 [ [{行业:{}},{行业:{}}]， [{公司:{}},{公司:{}}] ]
    for q3_data_dic_key in q3_data_dic:
        list_of_sublist_q3_datalist.append(q3_data_dic[q3_data_dic_key])
    dataStr = ''

    for sub_q3_data_list in list_of_sublist_q3_datalist:   # ls 是一个 list of dict
        dataStr = dataStr + str(sub_q3_data_list) + '\n'

    splitString = '\n\n所以，分析结论是：\n'
    # if not cmp.find('天津') == -1:
    if True:
        # new
        answer = {
            "id": id,
            "conversations": [{
                "from": "human",
                "value": 'Q：烟草行业的部分数据如下：\n' + dataStr + '\n请分析' + prompt + 'A：对以上数据的分析过程和结论是：\n'
            },
                {"from": "gpt",
                 # "value": splitString + summary_part1 + summary_part2
                 "value": cot + splitString + summary_part1 + summary_part2
                 }]
        }
        totalLen = (len(answer['conversations'][0]['value']) + len(answer['conversations'][1]['value']))
        if totalLen > maxLen:
            maxLen = totalLen
        return answer
    # else:
    #     return {
    #         "id": id,
    #         "conversations": [{
    #             "from": "human",
    #             "value": ''
    #         },
    #             {"from": "gpt",
    #              "value": ''
    #              # "value": cot + splitString + summary
    #              }]
    #     }


corpList_2021_2022 = list(set(corpList2021) & set(corpList2022))
corpList_2021_2022 = list(filter(lambda x: not pd.isnull(x), corpList_2021_2022))

sm = '行业整体'
type_list_sm = ['一类烟税利', '二类烟税利', '三类烟税利', '四类烟税利', '五类烟税利', '一至三类烟税利']
type_list_cmp = ['公司一类烟税利', '公司二类烟税利', '公司三类烟税利', '公司四类烟税利', '公司五类烟税利', '一至三类烟公司税利占比']
unit_list = ['万元', '万元', '万元', '万元', '万元', '万元']
pre_time = '2021'
cur_time = '2022'
l = []
few_shot = '公司一类烟税利占比>行业一类烟占比均值:则按照高于行业均值来表述；' \
           '否则按照低于行业均值来表述。其他二类、三类、四类、五类烟的逻辑和一类一致。' \
           '如果（公司一类烟税利占比-行业一类烟占比均值）>8%,则描述为“我司一类烟税利远高于行业平均水平，说明我司卷烟结构相对已经比较优化”；' \
           '如果（公司一类烟税利占比-行业一类烟占比均值）<-8%,则描述为“我司一类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间，' \
           '否则与行业水平相当。'




lsyfewshot = '''
'''
blank = ''
global maxLen
maxLen = 0


def QA3pmptGenerator(q3_datalist, cmp, sm, prompt, type_list_sm, type_list_cmp, unit_list, pre_time, cur_time, id):
    global maxLen
    # print(q3_datalist)
    q3_datalist_copy = copy.deepcopy(q3_datalist)
    data_dict = generate_dict_from_year(q3_datalist_copy)
    sm_rate_dict = get_data_sm(data_dict, sm, type_list_sm, unit_list, pre_time, cur_time)
    # 行业占比
    # sm_rate_dict:
    # {'一类烟税利': 87.49, '二类烟税利': 29.15, '三类烟税利': 23.81, '四类烟税利': 0.74, '五类烟税利': 0.05,
    #  '其他烟税利': 0.29}
    cmp_rate_dict = get_data_cmp(data_dict, cmp, type_list_cmp, unit_list, pre_time, cur_time)
    # 公司各类占比
    # cmp_rate_dict:
    # {'公司一类烟税利': 57.3, '公司二类烟税利': 11.93, '公司三类烟税利': 30.64, '公司四类烟税利': 0.14,
    #  '公司五类烟税利': 0.0, '公司其他烟税利': 0.0}
    # 把cmp_rate_dict加入到q3_datalist里面
    for q3_data in q3_datalist:
        for q3key in q3_data:   # q3key是行业整体或者公司名称
            if q3key == cmp:
                for key in cmp_rate_dict[str(q3_data[q3key]['年度'])]:
                    if key[:2] == '公司':
                        keyStr = key[2:-2] + '公司税利占比'
                    else:
                        keyStr = key
                    q3_data[q3key].__setitem__(keyStr, str(cmp_rate_dict[str(q3_data[q3key]['年度'])][key])+'%')
                # break
            if q3key == sm:
                for key in sm_rate_dict[str(q3_data[q3key]['年度'])]:
                    q3_data[q3key].__setitem__(key+'占比', str(sm_rate_dict[str(q3_data[q3key]['年度'])][key])+'%')
                # break
    summary_part1 = '我司（'+ str(cmp)+'）的'
    summary_part2 = ''
    summaryList = []
    pmptsummary = ''
    pmptidx = 1
    for type_sm, type_cmp, unit in zip(type_list_sm, type_list_cmp, unit_list):
        sent_part1, sent_part2 = generate_sent_compare_year(cmp_rate_dict[str(cur_time)][type_cmp], sm_rate_dict[str(cur_time)][type_sm], type_cmp)
        summaryList.append(str(sent_part1))
        summary_part1 += sent_part1
        summary_part2 += sent_part2
        pmptsummary = pmptsummary + summary_part1 + '\n'
        # 这部分不用改，这是最后的结论 我司公司一类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间。我司公司二类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间。
    summaryList.append(summary_part2)
    cot = buildNewCoTWithSteps(cmp, cur_time, pre_time, sm_rate_dict, cmp_rate_dict,summaryList)
    # cot = buildCcmpParaGraphot(pre_time, cur_time,cmp,q3_datalist,type_list_sm,type_list_cmp,sm_rate_dict[str(cur_time)],cmp_rate_dict[str(cur_time)])
    q3_data_dic = {}    # 预期是{行业： [{行业:{}},{行业:{}}], 公司： [{公司:{}},{公司:{}}]}
    for q3dic in q3_datalist:
        for key in q3dic:
            if q3_data_dic.__contains__(key):
                q3_data_dic[key].append(q3dic)
            else:
                q3_data_dic.__setitem__(key, [q3dic])
    list_of_sublist_q3_datalist = [] # 预期是 [ [{行业:{}},{行业:{}}]， [{公司:{}},{公司:{}}] ]
    for q3_data_dic_key in q3_data_dic:
        list_of_sublist_q3_datalist.append(q3_data_dic[q3_data_dic_key])
    dataStr = ''

    for sub_q3_data_list in list_of_sublist_q3_datalist:   # ls 是一个 list of dict
        dataStr = dataStr + str(sub_q3_data_list) + '\n'

    pmpt =    '你是一个行业报告生成器，我给你一份报告模版，和需要注入的数据，请根据以下报告模版和需要注入的数据，生成新的报告。' \
              '不要漏掉模板中的项目，并确保项目使用中文中括号强调。\n\n' \
              '"""\n' \
              'xx行业对标分析报告\n' \
              '【相关数据】\n' \
              'xxxx年\n' \
              'xx公司一类烟公司税利占比xx%，高于（或低于）行业均值xx%。\n' \
              'xx公司二类烟公司税利占比xx%，高于（或低于）行业均值xx%。\n' \
              'xx公司三类烟公司税利占比xx%，高于（或低于）行业均值xx%。\n' \
              'xx公司四类烟公司税利占比xx%，高于（或低于）行业均值xx%。\n' \
              'xx公司五类烟公司税利占比xx%，高于（或低于）行业均值xx%。\n' \
              'xx公司其他烟公司税利占比xx%，高于（或低于）行业均值xx%。\n' \
              'xx公司一直三类烟公司税利占比xx%，高于（或低于）行业均值xx%。\n' \
              '【分析总结】\n' \
              '1.评价公司一类烟税利占比，如：我司一类烟税利远低于行业平均水平，说明我司卷烟结构提升方面仍有较大提升空间。\n' \
              '"""\n' \
              '待注入数据:\n' + dataStr + '\n' \
              '请按照模版生成完整报告，不要漏掉模板中的项目，并确保项目使用中文中括号强调，这很重要。'
    answer = {
        "id": id,
        "conversations": [{
            "from": "human",
            "value": pmpt
        },
            {"from": "gpt",
             # "value": splitString + summary_part1 + summary_part2
             "value": summary_part1 + summary_part2
             }]
    }
    totalLen = (len(answer['conversations'][0]['value']) + len(answer['conversations'][1]['value']))
    if totalLen > maxLen:
        maxLen = totalLen
        return answer


vicunaQA3dataList = []
QA3PmptList = []
# prompt = '''问：分析以下问题，在问题后给出的数据中先做出筛选，再回答问题。看一下2020年某公司一类烟税利占比的行业对标情况。'''
for idx, cmp in enumerate(corpList_2021_2022):
    if not (checkOplExists(optionalCorpList, cmp)):
        continue
    prompt = f'{cmp}{cur_time}卷烟结构的行业对标情况。{blank}'
    q3_datalist = get_q3DataList(cmp)
    l.append(generate_Q3(q3_datalist, cmp, sm, prompt, type_list_sm, type_list_cmp, unit_list, pre_time, cur_time, idx))
    QA3PmptList.append(QA3pmptGenerator(q3_datalist, cmp, sm, prompt, type_list_sm, type_list_cmp, unit_list, pre_time, cur_time, idx))




# print(l)
# json.dump(l, open('dataset_Q3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
# sss




