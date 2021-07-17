import numpy as np
import draw

#该函数负责将数据降维
def pca(list):
    #list为m行n列矩阵,p为所要降到的维度
    #average:均值
    #cov:协方差矩阵
    #value:特征值
    #vector:特征向量
    #projection:投影矩阵
    m=len(list)
    n=len(list[0])
    print('原数据',list)
    p=2
    average=[]
    for i in range(n):
        score=0
        for j in range(m):
            score+=list[j][i]
        average.append(round(score/m,2))
    for i in range(m):
        for j in range(n):
            list[i][j]-=average[j]
    cov=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                cov[i][j]+=(list[k][i]*list[k][j])
            cov[i][j]=round(cov[i][j],2)
    cov = np.array(cov)
    #这边特征值没有问题，特征向量有问题，那位大佬帮忙看看呀
    value,vector=np.linalg.eig(cov)
    value=np.around(value,2)
    vector=np.around(vector,9)
    vectorlist=vector.tolist()

    print('打印协方差矩阵cov:\n{}'.format(cov))
    print('打印特征值a：\n{}'.format(value))
    print('打印特征向量b：\n{}'.format(vector))

    #从大到小排序特征值极其相对应的特征向量，找出影响最大的p个因素
    factors = ['平均分数', '平均提交次数', '平均耗时', '平均代码行最大长度', '平均代码行数']
    for i in range(value.size):
        j=0
        while j<value.size-i-1:
            if value[j]<value[j+1]:
                vectorlist[j],vectorlist[j+1]=vectorlist[j+1],vectorlist[j]
                factors[j],factors[j+1]=factors[j+1],factors[j]
            j=j+1

    #利用投影矩阵将数据降到p维
    projection=[]
    for i in range(p):
        projection.append(vectorlist[i])
    #projection=[[-0.83271,-0.20746,-0.3461481,0.029,0.05,0.372],[0.03,0.749,0.13,0.0965,0.327755,0.55]]
    print('各因素的重要性排序为：',factors)
    print('影响最大的',p,'个因素是 ',factors[0:p])
    result=[[0]*p for i in range(m)]
    for i in range(p):
        for j in range(m):
            for k in range(n):
                result[j][i]+=(list[j][k]*projection[i][k])

    draw.drawing(result,factors[0:p])#象征性画个降到2维的图

    return result



