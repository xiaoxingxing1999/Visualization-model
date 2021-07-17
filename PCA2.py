import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def pca2(list):

    #使用库里的pca，用计算投影特征方差贡献率的方式算出每个特征所占权重

    x=np.array(list)
    p=PCA(n_components=5)#设置权重和阈值——这里设置为5的原因是要它打出5个成分各自的权重
    p.fit(x)
    print('各因素所占权重为',p.explained_variance_ratio_)#各成分的权重

    #print(p.explained_variance_)#各成分投影后的特征维度的方差
    #print(p.n_components_)#最后有意义的成分个数——如果前面设置n_components=0.9的话这里将打出1，因为平均分一项就占了差不多100%了



