import json

import pandas as pd
import random
from cigarQuestionGenerator_q1_q5 import corpList2021, corpList2022, corpListSummary2022,optionalCorpList,\
    stdOplCorpList, checkOplExists, stringToNumAndUnit



def checkOplExists (optionalCorpList, curcorp):
    for oplC in optionalCorpList:
        if not str(curcorp).find(oplC) == -1:
            return True
    return False

def vicunaDataToChatglm2Data(vicunaDataList):
    chatglm2DataList = []
    for elem in vicunaDataList:
        chatglm2DataList.append(
            {"instruction": elem['conversations'][0]['value'], "output": elem['conversations'][1]['value']})
    return chatglm2DataList

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



def get_q2DataList(cmp):
    q2DataList = []
    for elem in corpListSummary2022:
        if elem['主体'] == cmp:
            q2DataList.append(
                {elem['主体']: {
                    # '主体': elem['主体'],
                    '年度': elem['前一年度'],
                    '税利': elem['前一年税利'],
                    '利润': elem['前一年利润'],
                    '单箱税利': elem['前一年单箱税利'],
                    '单箱利润': elem['前一年单箱利润'],

                    '税利同比增加': elem['前一年税利同比增加'],
                    '税利同比增长率': elem['前一年税利同比增长率'],
                    '利润同比增加': elem['前一年利润同比增加'],
                    '利润同比增长率': elem['前一年利润同比增长率'],

                    '单箱税利同比增加': elem['前一年单箱税利同比增加'],
                    '单箱税利同比增长率': elem['前一年单箱税利同比增长率'],
                    '单箱利润同比增加': elem['前一年单箱利润同比增加'],
                    '单箱利润同比增长率': elem['前一年单箱利润同比增长率'],
                    # '评价': "暂定行业整体形势向好，税利、卷烟结构整体提升；工业税利、利润增幅高于去年同期。2023年1-6月份，工业税利4080亿元,同比增加276亿元,增长8.30%。工业利润1313亿元,同比增加49亿元, 增长7.56%"
                }})
            q2DataList.append(
                {elem['主体']: {
                    # '主体': elem['主体'],
                    '年度': elem['年度'],
                    '税利': elem['税利'],
                    '利润': elem['利润'],
                    '单箱税利': elem['单箱税利'],
                    '单箱利润': elem['单箱利润'],

                    '税利同比增加': elem['税利同比增加'],
                    '税利同比增长率': elem['税利同比增长率'],
                    '利润同比增加': elem['利润同比增加'],
                    '利润同比增长率': elem['利润同比增长率'],

                    '单箱税利同比增加': elem['单箱税利同比增加'],
                    '单箱税利同比增长率': elem['单箱税利同比增长率'],
                    '单箱利润同比增加': elem['单箱利润同比增加'],
                    '单箱利润同比增长率': elem['单箱利润同比增长率'],
                    # '评价': "暂定行业整体形势向好，税利、卷烟结构整体提升；工业税利、利润增幅高于去年同期。2023年1-6月份，工业税利4080亿元,同比增加276亿元,增长8.30%。工业利润1313亿元,同比增加49亿元, 增长7.56%"
                }})
            q2DataList.append({"行业整体": {
                '年度': elem["前一年度"],
                '税利': elem['前一年行业整体税利'],
                '利润': elem['前一年行业整体利润'],
                '单箱税利': elem['前一年行业单箱税利'],
                '单箱利润': elem['前一年行业单箱利润'],

                '税利同比增加': elem['前一年行业税利同比增加'],
                '税利同比增长率': elem['前一年行业税利同比增长率'],
                '利润同比增加': elem['前一年行业利润同比增加'],
                '利润同比增长率': elem['前一年行业利润同比增长率'],

                '单箱税利同比增加': elem['前一年行业单箱税利同比增加'],
                '单箱税利同比增长率': elem['前一年行业单箱税利同比增长率'],
                '单箱利润同比增加': elem['前一年行业单箱利润同比增加'],
                '单箱利润同比增长率': elem['前一年行业单箱利润同比增长率'],

            }})
            q2DataList.append({"行业整体": {
                '年度': elem["年度"],
                '税利': elem['行业整体税利'],
                '利润': elem['行业整体利润'],
                '单箱税利': elem['行业单箱税利'],
                '单箱利润': elem['行业单箱利润'],

                '税利同比增加': elem['行业税利同比增加'],
                '税利同比增长率': elem['行业税利同比增长率'],
                '利润同比增加': elem['行业利润同比增加'],
                '利润同比增长率': elem['行业利润同比增长率'],

                '单箱税利同比增加': elem['行业单箱税利同比增加'],
                '单箱税利同比增长率': elem['行业单箱税利同比增长率'],
                '单箱利润同比增加': elem['行业单箱利润同比增加'],
                '单箱利润同比增长率': elem['行业单箱利润同比增长率'],
            }})
    return q2DataList

def generate_dict_from_year(DataList):
    new_dict = {}
    for data in DataList:
        for cmp in data.keys():
            inf = data[cmp]
            time = inf['年度']
            new_dict[f'{cmp}_{time}'] = inf
    return new_dict


# 公司 和 行业整体 对比
def cmp_sm_compare_rate(cmp_rate, sm_rate):
    if sm_rate > 0:
        sm_part = f'增长{sm_rate}'
    else:
        # todo pmpt由下降改为降低
        sm_part = f'下降{abs(sm_rate)}'
        sm_part = f'降低{abs(sm_rate)}'
    if cmp_rate > sm_rate:
        return f'高于行业{sm_part}%的平均水平'
    elif cmp_rate < sm_rate:
        return f'低于行业{sm_part}%的平均水平'
    else:
        return f'等于行业{sm_part}%的平均水平'

# 获取行业整体数据
def get_data_sm(data_dict, sm, type_list, unit_list, pre_time, cur_time):
    sm_inf_pre = data_dict[f'{sm}_{pre_time}']
    sm_inf_cur = data_dict[f'{sm}_{cur_time}']
    sm_rate_dict = {}
    sm_pre_dict = {}
    sm_cur_dict = {}
    for type, unit in zip(type_list, unit_list):
        # print(sm_inf_pre[type])
        # print(sm_inf_cur[type])
        pre_numstr, preunit, prepower = stringToNumAndUnit(sm_inf_pre[type])
        cur_numstr, curunit, curpower = stringToNumAndUnit(sm_inf_cur[type])
        pre_inf = float(pre_numstr)*prepower
        cur_inf = float(cur_numstr)*curpower
        if pre_inf>0:
            sm_rate_dict[type] = round(((cur_inf - pre_inf) / pre_inf) * (10 ** 2), 2)
        elif pre_inf<0:
            sm_rate_dict[type] = round(((cur_inf - pre_inf) / abs(pre_inf)) * (10 ** 2), 2)
        else:
            sm_rate_dict[type] = 999999999999.99
        if prepower < curpower:
            sm_pre_dict[type] = {'baseNumber': int(pre_inf*prepower/curpower), 'unit': curunit}
            sm_cur_dict[type] = {'baseNumber': int(cur_inf*prepower/curpower), 'unit': curunit}
        else:
            sm_pre_dict[type] = {'baseNumber': int(pre_inf * curpower / prepower), 'unit': preunit}
            sm_cur_dict[type] = {'baseNumber': int(cur_inf * curpower / prepower), 'unit': preunit}
    return sm_rate_dict, sm_pre_dict, sm_cur_dict


# 生成句式
def generate_sent_compare_year(pre_data_str, cur_data_str, sm_rate, sm_pre, sm_cur, type):
    # todo 这里有问题，减幅的情况下还可以高于行业均值
    pre_numstr, preunit, prepower = stringToNumAndUnit(pre_data_str)
    cur_numstr, curunit, curpower = stringToNumAndUnit(cur_data_str)
    pre_data = int(pre_numstr)
    cur_data = int(cur_numstr)
    pre_raw_data = pre_data * prepower
    cur_raw_data = cur_data * curpower
    if prepower > curpower:
        difpower = prepower
        dif_unit = preunit
    else:
        difpower = curpower
        dif_unit = curunit
    dif_data = int(round((cur_raw_data - pre_raw_data)/difpower,2))     #round(dif_rate * (10 ** 2), 2)
    if not int(pre_raw_data) == 0:
        dif_rate = round(((cur_raw_data - pre_raw_data) / abs(pre_raw_data)) * (10 ** 2), 2)
    if type == '单箱税利' or type == '单箱利润':  # 需要特定生成的句式(如果有新句式，加if情况扩展)
        if dif_data > 0:
            if int(pre_data) == 0:
                sent_part = f'{type}{cur_data}{curunit}，行业均值{sm_cur["baseNumber"]}{sm_cur["unit"]}。'
            else:
                sent_part = f'{type}{cur_data}{curunit}，行业均值{sm_cur["baseNumber"]}{sm_cur["unit"]}，公司{type}增长{abs(dif_rate)}%，' \
                            f'{cmp_sm_compare_rate(dif_rate, sm_rate)}。'
        else:
            if pre_data == 0:
                sent_part = f'{type}{cur_data}{curunit}，行业均值{sm_cur["baseNumber"]}{sm_cur["unit"]}。'
            else:
                # todo remove abs
                sent_part = f'{type}{cur_data}{curunit}，行业均值{sm_cur["baseNumber"]}{sm_cur["unit"]}，公司{type}降低{abs(dif_rate)}%，' \
                            f'{cmp_sm_compare_rate((dif_data / pre_data), sm_rate)}。'
                # sent_part = f'{type}{cur_data}{curunit}，行业均值{sm_cur["baseNumber"]}{sm_cur["unit"]}，公司{type}增长{(dif_rate)}%，' \
                #             f'{cmp_sm_compare_rate((dif_data / pre_data), sm_rate)}。'
    else:  # 通用情况句式
        if dif_data > 0:
            if int(pre_data) == 0:
                sent_part = f'{type}{cur_data}{curunit}，同比增加{dif_data}{dif_unit}。'
            else:
                sent_part = f'{type}{cur_data}{curunit}，同比增加{dif_data}{dif_unit}，增长{dif_rate}%，' \
                            f'{cmp_sm_compare_rate(dif_rate, sm_rate)}。'
        else:
            if pre_data == 0:
                # todo remove abs
                sent_part = f'{type}{cur_data}{curunit}，同比减少{abs(dif_data)}{dif_unit}。'
                # sent_part = f'{type}{cur_data}{curunit}，同比增加{(dif_data)}{dif_unit}。'
            else:
                # todo remove abs
                sent_part = f'{type}{cur_data}{curunit}，同比增加{(dif_data)}{dif_unit}，降低{abs(dif_rate)}%，' \
                            f'{cmp_sm_compare_rate(dif_rate, sm_rate)}。'
                # sent_part = f'{type}{cur_data}{curunit}，同比增加{(dif_data)}{dif_unit}，增长{(dif_rate)}%，' \
                #             f'{cmp_sm_compare_rate(dif_rate, sm_rate)}。'
    return sent_part



def new_q2_generate_sent_compare_year(fourPos, type,preNotZero=True):
    # todo 这里有问题，减幅的情况下还可以高于行业均值
    floatFourpos = []
    fourposUnit = []
    for elem in fourPos:
        pos1_numstr, pos1unit, pos1power = stringToNumAndUnit(elem)
        floatFourpos.append(float(pos1_numstr) * pos1power)
        fourposUnit.append(pos1unit)
    if not preNotZero:
        return '无法计算'
        # dif_rate = round(((cur_raw_data - pre_raw_data) / abs(pre_raw_data)) * (10 ** 2), 2)
    # if type == '单箱税利' or type == '单箱利润':  # 需要特定生成的句式(如果有新句式，加if情况扩展)
    res = ''
    if type == '收入' or type == '利润':
        if floatFourpos[1] > 0:
            res = res + type + fourPos[0] + '，同比增加' + fourPos[1] + '，增长' + fourPos[2]
        else:
            res = res + type + fourPos[0] + '，同比增加' + fourPos[1] + '，增长' + fourPos[2]
            # res = res + type + fourPos[0] + '，同比减少' + str(int(abs(floatFourpos[1]))) + fourposUnit[1] + '。' \
            #         '减少' + str(abs(floatFourpos[2])) + fourposUnit[2]
        if floatFourpos[2] > floatFourpos[3]:
            res = res + '，高于行业' + fourPos[3] + '的平均水平。'
        elif floatFourpos[2] == floatFourpos[3]:
            res = res + '，与行业持平。'
        else:
            res = res + '，低于行业' + fourPos[3] + '的平均水平。'
    else:
        if floatFourpos[0] > floatFourpos[1]:
            res = res + type + fourPos[0] + '，高于行业均值' + fourPos[1]
        else:
            res = res + type + fourPos[0] + '，低于行业均值' + fourPos[1]
        if floatFourpos[2] > 0:
            res = res + '，增加' + fourPos[2]
        else:
            res = res + '，增加' + fourPos[2]
            # res = res + '。减少' + str(int(abs(floatFourpos[2]))) + fourposUnit[2]
        if floatFourpos[2] > floatFourpos[3]:
            res = res + '，高于行业' + fourPos[3] + '的平均水平。'
        elif floatFourpos[2] == floatFourpos[3]:
            res = res + '，与行业持平。'
        else:
            res = res + '，低于行业' + fourPos[3] + '的平均水平。'
    # else:  # 通用情况句式
    #     if dif_data > 0:
    #         sent_part = f'{type}{cur_data_str}，同比增加{dif_data}，增长{dif_rate}%，' \
    #                     f'{cmp_sm_compare_rate(dif_rate, sm_rate)}。'
    #     else:
    #         # todo remove abs
    #         sent_part = f'{type}{cur_data_str}，同比增加{(dif_data)}，降低{abs(dif_rate)}%，' \
    #                     f'{cmp_sm_compare_rate(dif_rate, sm_rate)}。'
    #         # sent_part = f'{type}{cur_data}{curunit}，同比增加{(dif_data)}{dif_unit}，增长{(dif_rate)}%，' \
    #         #             f'{cmp_sm_compare_rate(dif_rate, sm_rate)}。'
    return res

def build4Steps(cmp,cur_time,pre_time,item, smq2data, cmpq2data,oneSummary):
    changeValue = item + '同比增加'
    compairItem = item + '同比增长率'
    cmpItemNum, cmpItemUnit, cmpItemPower = stringToNumAndUnit(cmpq2data[compairItem])
    smItemNum, smItemUnit, smItemPower = stringToNumAndUnit(smq2data[compairItem])
    if float(cmpItemNum)*cmpItemPower > float(smItemNum) * smItemPower:
        reasonStr = cmpq2data[compairItem] + ' > ' + smq2data[compairItem]
    elif float(cmpItemNum)*cmpItemPower == float(smItemNum) * smItemPower:
        reasonStr = cmpq2data[compairItem] + ' = ' + smq2data[compairItem]
    else:
        reasonStr = cmpq2data[compairItem] + ' < ' + smq2data[compairItem]
    res =   '找到' + str(cmp) + cur_time + '年的' + item + \
            '为' + str(cmpq2data[item]) + '，' \
            +item+'同比增长量为' + str(cmpq2data[changeValue]) + '，' \
            +item+'同比增长率为' + str(cmpq2data[compairItem]) + '，' \
            '行业整体'+cur_time+'年的'+item+'同比增长率为' + str(smq2data[compairItem]) + \
            '，因为'+reasonStr+'，所以我输出: ' \
            '"'+oneSummary+'"\n'
    return res

def buildCot(pre_time, cur_time, type_list, cmp, sm, q2data_list, summaryListforCot):
    cur_t_brac = '（' + str(cur_time) + '年）'
    pre_t_brac = '（' + str(pre_time) + '年）'
    cmp_brac = '（' + str(cmp) + '）'
    resStr = '分析过程：\n'
    keyListStr = '、'.join(type_list)
    cmpAndSmTermStr = str(cmp) + '和' + str(sm) +'的' + keyListStr
    preCurYearStr = str(cur_time) + '、' + str(pre_time) + '年'
    few_shot = '给定数据包含' + preCurYearStr + '两个年份，默认分析最近的年份，也就是' + cur_time + '年。对当前公司' + cmp_brac
    few_shotEG = '当前年度'+cur_t_brac+'的税利同比增长率，与同一年度行业整体的税利同比增长率进行比较，' \
                    '若公司的税利同比增长率高于行业整体的税利同比增长率的时候，' \
                    '输出："' + str(cur_time)+'年'+str(cmp)+'税利' \
                    'xx万元，同比增加xx万元，增加xx%，高于行业增长yy%的平均水平。"，' \
                    '否则输出："'+str(cur_time)+'年'+str(cmp)+'税利' \
                    'xx万元，同比减少xx万元，减小xx%，低于行业增长yy%的平均水平。"，' \
                    '按照以上的输出逻辑，对利润同比增长率、单箱税利同比增长率、单箱利润同比增长率进行比较和输出。' \
                    # '对当前公司'+cmp_brac+'的单箱税利，找出当前年度'+ cur_t_brac + '的单箱税利同比增长率，' \
                    # '与同一年度行业整体的单箱同比增长率税利，当前年度的单箱税利同比增长率进行比较，' \
                    # '若公司的单箱税利同比增长率高于行业整体的单箱税利同比增长率，输出：' \
                    # '"单箱税利xx元，行业均值yy元，公司增幅xx%，高于行业增长yy%的平均水平。"，' \
                    # '否则输出：' \
                    # '"单箱税利xx元，行业均值yy元，公司减幅xx%，低于行业增长yy%的平均水平。"，' \
                    # '按照和单箱税利同样的方式，对单箱利润进行比较和输出。' \
    # '方法是分别分析这些条目的同比增长、同比增长率，并与行业的同名条目做对比。'
    resStr = resStr + few_shot + few_shotEG
    stepOne = build4Steps(cmp,cur_time,pre_time,'税利', q2data_list[3][sm], q2data_list[1][cmp], summaryListforCot[0])
    stepTwo = build4Steps(cmp, cur_time, pre_time, '利润', q2data_list[3][sm], q2data_list[1][cmp],
                          summaryListforCot[1])
    stepThree = build4Steps(cmp, cur_time, pre_time, '单箱税利', q2data_list[3][sm], q2data_list[1][cmp],
                          summaryListforCot[2])
    stepFour = build4Steps(cmp, cur_time, pre_time, '单箱利润', q2data_list[3][sm], q2data_list[1][cmp],
                          summaryListforCot[3])

    res720_2 =  'A: "分析过程：\n' \
                '给定的数据包含'+preCurYearStr+'两个年份，默认当前年度为最近年份，也就是'+cur_time+'年。' \
                '要分析'+str(cmp)+'的行业效益情况，我需要找到'+str(cmp)+'的税利、利润、单箱税利、单箱利润相关信息，将'+str(cmp) + \
                '的'+cur_time+'年的' \
                '税利同比增长率、利润同比增长率、单箱税利同比增长率、单箱利润同比增长率，' \
                '分别与行业整体的'+cur_time+'年的' \
                '税利同比增长率、利润同比增长率、单箱税利同比增长率、单箱利润同比增长率进行比较。' \
                '我用4个步骤来分析这个问题：\n' \
                'Step1: ' + stepOne +\
                'Step2: ' + stepTwo + \
                'Step3: ' + stepThree + \
                'Step4: ' + stepFour
                # 'A: "分析过程：\n' \
                # '给定的表包含' + preCurYearStr + '两个年份，我默认' + cur_time + '年为最近年份。' \
                # '要分析' + str(cmp) + '的行业效益情况，我需要将' + str(cmp) + '的' + cur_time + '年相比' + pre_time + '年的' \
                # '税利同比增长率、利润同比增长率、单箱税利同比增长率、单箱利润同比增长率，' \
                # '分别与行业整体的' + cur_time + '年相比' + pre_time + '年的' \
                # '税利同比增长率、利润同比增长率、单箱税利同比增长率、单箱利润同比增长率进行比较。' \
                # '我用4个步骤来分析这个问题：\n' \
                # 'Step1: ' + stepOne + \
                # 'Step2: ' + stepTwo + \
                # 'Step3: ' + stepThree + \
                # 'Step4: ' + stepFour
    return res720_2

# 总体数据生成
def generate_Q2(q2_datalist, cmp, sm, prompt, type_list, unit_list, pre_time, cur_time, id):
    global maxLen
    data_dict = generate_dict_from_year(q2_datalist)
    sm_rate_dict, sm_pre_dict, sm_cur_dict = get_data_sm(data_dict, sm, type_list, unit_list, pre_time, cur_time)
    cmp_inf_pre = data_dict[f'{cmp}_{pre_time}']
    cmp_inf_cur = data_dict[f'{cmp}_{cur_time}']
    summary = f'{cmp}'
    summaryListforCot = []
    for type, unit in zip(type_list, unit_list):
        # pre_inf = int(cmp_inf_pre[type].strip(unit))
        # cur_inf = int(cmp_inf_cur[type].strip(unit))
        pre_infStr, preunit, prepower = stringToNumAndUnit(cmp_inf_pre[type])
        cur_infStr, curunit, curpower = stringToNumAndUnit(cmp_inf_cur[type])
        pre_inf = int(pre_infStr)*prepower
        cur_inf = int(cur_infStr)*curpower
        sent_part = generate_sent_compare_year(cmp_inf_pre[type], cmp_inf_cur[type], sm_rate_dict[type], sm_pre_dict[type],
                                               sm_cur_dict[type], type)
        summary += sent_part
        # if len(summaryListforCot) == 0:
        summaryListforCot.append(sent_part)
        if curpower > prepower:
            dif_data = (cur_inf - pre_inf) / curpower
            dif_unit = curunit
        else:
            dif_data = (cur_inf - pre_inf) / prepower
            dif_unit = preunit
        if pre_inf == 0:
            dif_rate = '数值错误'
        else:
            dif_rate = dif_data / pre_inf
            dif_rate = round(dif_rate * (10 ** 2), 2)
            dif_rate = str(dif_rate)
        # for q2dic in q2_datalist:
        #     for key in q2dic:
        #         if q2dic[key]['年度'] == cur_time:
        #             if key == cmp:
        #                 q2dic[key].__setitem__(type + '同比增加',str(dif_data) + dif_unit)
        #                 q2dic[key].__setitem__(type + '同比增长率', str(dif_rate)+'%')
        #             if key == sm:
        #                 for smrkey in sm_cur_dict:
        #                     q2dic[key].__setitem__('行业' + smrkey + '同比增加', str(sm_cur_dict[smrkey]['number']-sm_pre_dict[smrkey]['number']) + sm_pre_dict[smrkey]['unit'])
        #                 for smrkey in sm_rate_dict:
        #                     q2dic[key].__setitem__('行业' + smrkey + '同比增长率', str(sm_rate_dict[smrkey])+'%')
        #         elif q2dic[key]['年度'] == pre_time:
        #             if key == cmp:
        #                 q2dic[key].__setitem__(type + '同比增加', '暂无数据')
        #                 q2dic[key].__setitem__(type + '同比增长率', '暂无数据')
        #             if key == sm:
        #                 for smrkey in sm_cur_dict:
        #                     q2dic[key].__setitem__('行业' + smrkey + '同比增加',
        #                                            '暂无数据')
        #                 for smrkey in sm_rate_dict:
        #                     q2dic[key].__setitem__('行业' + smrkey + '同比增长率', '暂无数据')


    splitString = '\n\n所以，分析结论是：\n'
    cot = buildCot(pre_time, cur_time,type_list, cmp, sm, q2_datalist,summaryListforCot)
    # if not cmp.find('北京') == -1:
    answer = {
        "id": id,
        "conversations": [{
            "from": "human",
            "value": 'Q：烟草行业的部分数据如下：' + str(q2_datalist) + '\n请分析' + prompt + '\nA：对以上数据的分析过程和结论是：\n'
        },
            {"from": "gpt",
             # "value": splitString + summary
             "value": cot + splitString + summary
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
def getMultipleData(inputList, totalNum = 50):
    if totalNum > len(inputList):
        for idx in range(0,totalNum):
            inputList.append(inputList[idx%len(inputList)])
    else:
        inputList = random.sample(inputList, k=totalNum)
    return inputList
def pmptGenerator(q2_datalist, cmp, sm, prompt, type_list, unit_list, pre_time, cur_time, id):
    global maxLen
    data_dict = generate_dict_from_year(q2_datalist)
    sm_rate_dict, sm_pre_dict, sm_cur_dict = get_data_sm(data_dict, sm, type_list, unit_list, pre_time, cur_time)
    cmp_inf_pre = data_dict[f'{cmp}_{pre_time}']
    cmp_inf_cur = data_dict[f'{cmp}_{cur_time}']
    summary = str(cmp) + '行业效益报告\n【相关数据】\n'
    summaryListforCot = []
    pmptidx = 1
    for type, unit in zip(type_list, unit_list):
        # pre_inf = int(cmp_inf_pre[type].strip(unit))
        # cur_inf = int(cmp_inf_cur[type].strip(unit))
        pre_infStr, preunit, prepower = stringToNumAndUnit(cmp_inf_pre[type])
        cur_infStr, curunit, curpower = stringToNumAndUnit(cmp_inf_cur[type])
        pre_inf = int(pre_infStr) * prepower
        cur_inf = int(cur_infStr) * curpower
        sent_part = generate_sent_compare_year(cmp_inf_pre[type], cmp_inf_cur[type], sm_rate_dict[type],
                                               sm_pre_dict[type],
                                               sm_cur_dict[type], type)
        summary = summary + str(pmptidx) + '.' + sent_part + '\n'
        pmptidx += 1
        # if len(summaryListforCot) == 0:
        summaryListforCot.append(sent_part)
        if curpower > prepower:
            dif_data = (cur_inf - pre_inf) / curpower
            dif_unit = curunit
        else:
            dif_data = (cur_inf - pre_inf) / prepower
            dif_unit = preunit
        if pre_inf == 0:
            dif_rate = '数值错误'
        else:
            dif_rate = dif_data / pre_inf
            dif_rate = round(dif_rate * (10 ** 2), 2)
            dif_rate = str(dif_rate)
    cmpTarDic = q2_datalist[1]
    smTarDic = q2_datalist[3]
    cmpTarDic[cmp].__setitem__('行业税利同比增长率', smTarDic['行业整体']['税利同比增长率'])
    cmpTarDic[cmp].__setitem__('行业利润同比增长率', smTarDic['行业整体']['利润同比增长率'])
    cmpTarDic[cmp].__setitem__('行业单箱税利同比增长率', smTarDic['行业整体']['单箱税利同比增长率'])
    cmpTarDic[cmp].__setitem__('行业单箱利润同比增长率', smTarDic['行业整体']['单箱利润同比增长率'])
    pmptDataSet = [q2_datalist[1],q2_datalist[3]]
    pmptres = '你是一个行业报告生成器，我给你一份报告模版，和需要注入的数据，请根据以下报告模版和需要注入的数据，生成新的报告。' \
          '不要漏掉模板中的项目，并确保项目使用中文中括号强调。\n\n' \
          '"""\n' \
          'xx行业效益报告\n' \
          '【相关数据】\n' \
          'xxxx年\n' \
          'xxx公司的税利xxx元,同比增加（或减少）xxx元, 同比增长（或降低）xxx%, 高于（或低于）行业增长xxx的平均水平；\n' \
          '利润xxx元,同比增长（或减少）xxx元, 同比增长（或降低）xxx%, 高于（或低于）行业增长xxx的平均水平；\n' \
          '单箱税利xxx元, 行业均值xxx元, 公司单箱税利同比增长（或降低）xxx%, 高于（或低于）行业xxx%的平均水平；\n' \
          '单箱利润xxx元, 行业均值xxx元, 公司单箱利润同比增长（或降低）xxx%, 高于（或低于）行业xxx%的平均水平\n' \
          '"""\n' \
          '待注入数据:\n' + str(q2_datalist) + '\n' \
          '请按照模版生成完整报告，不要漏掉模板中的项目，并确保项目使用中文中括号强调，这很重要。'
    splitString = '\n\n所以，分析结论是：\n'
    cot = buildCot(pre_time, cur_time, type_list, cmp, sm, q2_datalist, summaryListforCot)
    # if not cmp.find('北京') == -1:
    answer = {
        "id": id,
        "conversations": [{
            "from": "human",
            "value": pmptres
        },
            {"from": "gpt",
             "value": summary
             }]
    }
    totalLen = (len(answer['conversations'][0]['value']) + len(answer['conversations'][1]['value']))
    if totalLen > maxLen:
        maxLen = totalLen
    return answer



corpList_2021_2022 = list(set(corpList2021) & set(corpList2022))
# print(corpList_2021_2022)
corpList_2021_2022 = list(filter(lambda x: not pd.isnull(x), corpList_2021_2022))

sm = '行业整体'
type_list = ['税利', '利润', '单箱税利', '单箱利润']
unit_list = ['万元', '万元', '元', '元']
pre_time = '2021'
cur_time = '2022'
l = []
QA2PmptList = []
global maxLen
maxLen = 0
for idx, cmp in enumerate(corpList_2021_2022):
    if not checkOplExists(optionalCorpList,cmp):
        if checkOplExists(stdOplCorpList,cmp):
            continue
    prompt = f'{cmp}的行业效益情况'
    q2_datalist = get_q2DataList(cmp)
    # print('看看q2datalist')
    # print(q2_datalist)
    l.append(generate_Q2(q2_datalist, cmp, sm, prompt, type_list, unit_list, pre_time, cur_time, idx))
    QA2PmptList.append(pmptGenerator(q2_datalist, cmp, sm, prompt, type_list, unit_list, pre_time, cur_time, idx))


# with open('问题二/chatglm2_pmpt.json', 'w', encoding='utf-8') as f:
#     json.dump(QA2PmptList, f, indent=0, ensure_ascii=False)   # 格式同q1DataList

data_QA2_chatglm = vicunaDataToChatglm2Data(l)
with open('问题二/chatglm2_QA2.json', 'w', encoding='utf-8') as f:
    json.dump(data_QA2_chatglm, f, indent=0, ensure_ascii=False)
data_QA2_chatglm = getMultipleData(data_QA2_chatglm,90)
idxList = list(range(0, len(data_QA2_chatglm)))
trainIdxList = random.sample(idxList, k=int(len(data_QA2_chatglm)*0.85))
tcount = 0
vcount = 0
trainList = []
valList = []
for i in range(0, len(data_QA2_chatglm)):
    try:
        trainIdxList.index(i)
        trainList.append(data_QA2_chatglm[i])
        tcount = tcount + 1
    except:
        vcount = vcount + 1
        valList.append(data_QA2_chatglm[i])
with open('问题二/epmVal.json', 'w', encoding='utf-8') as f:
    json.dump(valList, f, indent=0, ensure_ascii=False)
# print(maxLen)
#
# idxList = list(range(0, len(l)))
# trainIdxList = random.sample(idxList, k=int(len(l)*0.85))
# tcount = 0
# vcount = 0
# trainList = []
# valList = []
# for i in range(0, len(l)):
#     try:
#         trainIdxList.index(i)
#         trainList.append(l[i])
#         tcount = tcount + 1
#     except:
#         vcount = vcount + 1
#         valList.append(l[i])
# print('train:')
# print(tcount)
# print('val:')
# print(vcount)
# with open('问题二/dataset_QA2_Train.json', 'w', encoding='utf-8') as f:
#     json.dump(trainList, f, indent=0, ensure_ascii=False)   # 格式同q1DataList
# with open('问题二/dataset_QA2_Validation.json', 'w', encoding='utf-8') as f:
#     json.dump(valList, f, indent=0, ensure_ascii=False)   # 格式同q1DataList
# with open('问题二/dataset_QA2.json', 'w', encoding='utf-8') as f:
#     json.dump(l, f, indent=0, ensure_ascii=False)   # 格式同q1DataList
# json.dump(l, open('问题二/dataset_QA2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


# chatglm2train = vicunaDataToChatglm2Data(trainList)
# chatglm2Val = vicunaDataToChatglm2Data(valList)
# chatglm2Full = vicunaDataToChatglm2Data(l)
# with open('问题二/chatglm2_dataset_QA2_Train.json', 'w', encoding='utf-8') as f:
#     json.dump(chatglm2train, f, indent=0, ensure_ascii=False)   # 格式同q1DataList
# with open('问题二/chatglm2_dataset_QA2_Validation.json', 'w', encoding='utf-8') as f:
#     json.dump(chatglm2Val, f, indent=0, ensure_ascii=False)   # 格式同q1DataList
# with open('问题二/chatglm2_dataset_QA2.json', 'w', encoding='utf-8') as f:
#     json.dump(chatglm2Full, f, indent=0, ensure_ascii=False)   # 格式同q1DataList