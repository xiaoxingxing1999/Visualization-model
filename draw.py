import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']#中文设置问题
plt.rcParams['axes.unicode_minus']=False#用来正常显示负号

def drawing(list,factors):
    m = len(list)
    n = len(list[0])#2

    _x=[]
    _y=[]

    for i in range(m):
        _x.append(list[i][0])
        _y.append(list[i][1])

    plt.scatter(_x,_y,c='r')
    # 设置坐标标签
    plt.xlabel('第一主成分: '+factors[0])
    plt.ylabel('第二主成分: '+factors[1])
    # 设置标题
    plt.title("PCA Scatter Plot")
    plt.show()
