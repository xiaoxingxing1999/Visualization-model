class student:
    # id:学生的id
    # case_id:题目编号
    # case_type:题目类型
    # final_score:题目最终得分
    # max_len:题目代码行的最大长度
    # numOflines:题目代码的行数
    # numOfif:题目使用if、elif、else的次数
    # time:做题时长
    # count:提交次数
    # index:做题数目
    def __init__(self,id):
        self.id=id
        self.case_id=[]
        self.case_type=[]
        self.final_score=[]
        self.max_len=[]
        self.numOflines=[]
        self.numOfif=[]
        self.code=[]
        self.time=[]
        self.count=[]
        self.index=0

    def add_case(self,case_id,case_type,final_score,time,count,max_len,numOflines,numOfif,code):
        self.case_id.append(case_id)
        self.case_type.append(case_type)
        self.final_score.append(final_score)
        self.time.append(time)
        self.count.append(count)
        self.max_len.append(max_len)
        self.numOflines.append(numOflines)
        self.numOfif.append(numOfif)
        self.code.append(code)
        self.index+=1