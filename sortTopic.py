import caculator
import PCA
import PCA2


def sort(caculator):
    data=[]
    dict = {}
    group=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    propertion=[]
    for i in range(caculator.index):
        temp=[caculator.case_score[i],caculator.case_count[i],caculator.case_time[i],caculator.case_maxlen[i],caculator.case_numOflines[i]]#平均分数 平均提交次数 平均耗时 平均代码行最大长度 平均代码行数
        data.append(temp)
        difficulty=100 - caculator.case_score[i]#直接在这里就算出难度的原因：根据之前的操作已经知道只使用平均分这个维度就可以了，为降低复杂度因此直接在这里操作，就不需要在另开一个循环了
        dict[caculator.case_id[i]] =difficulty
        j=int(difficulty/5)
        if j==20:
            j=19
        group[j]=group[j]+1
    reduction_data1=PCA.pca(data)#这一个可以看出各因素的重要性排序
    reduction_data2 = PCA2.pca2(data)#这一个可以看出各因素的权重

    #从上面已经知道只使用平均分数这一特征就可以了
    #难度=100-平均分
    #case_id-难度 键值对已存在上面的字典dict里，下面对题目进行难度排序
    dictSortList = sorted(dict.items(), key=lambda x: x[1], reverse=False)
    print("题目难度排序:")
    for i in range(len(dictSortList)):
        print("题目:",dictSortList[i][0]," 难度:",dictSortList[i][1]," 排名:",caculator.index-i)


    print("题目难度分组：")
    min=0
    max=5
    for i in range(20):
        n=group[i]
        propertion.append(n/ len(dictSortList))
        if i<19:
            print("难度区间[", min, ",", max, ") 有", n, "题,占", n / len(dictSortList))
        else:
            print("难度区间[", min, ",", max, "] 有", n, "题,占", n / len(dictSortList))
        min=min+5
        max=max+5
    return dict

