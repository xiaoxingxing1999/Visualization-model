class caculator:
    #以题目为索引的计算结果
    #case_id：题目编号
    #case_type:题目类型
    #case_average_score:题目分数平均数
    #case_count:题目平均提交次数
    #case_time:题目平均花费时间
    #case_maxlen:题目平均代码行最大长度
    #case_numOflines:题目平均代码行数

    def __init__(self,students):
        self.index=0
        self.case_id=[]
        self.case_type=[]
        self.case_score=[]
        #self.case_variance=[]
        self.case_count=[]
        self.case_time=[]
        self.case_maxlen=[]
        self.case_numOflines=[]
        students_num=len(students)

        #初始化
        for i in range(0,students_num):
            student=students[i]
            for j in range(0,student.index):
                if not student.case_id[j] in self.case_id:
                    self.index+=1
                    self.case_id.append(student.case_id[j])
                    self.case_type.append(student.case_type[j])

        #计算均值
        for i in range(0, self.index):
            all_score=0
            all_count = 0
            all_time = 0
            all_len = 0
            all_lines = 0
            for j in range(0,students_num):
                student=students[j]
                if self.case_id[i] in student.case_id:
                    index=student.case_id.index(self.case_id[i])
                    all_score+=student.final_score[index]
                    all_count += student.count[index]
                    all_time += student.time[index]
                    all_len += student.max_len[index]
                    all_lines += student.numOflines[index]
            self.case_score.append(all_score / students_num)
            self.case_count.append(all_count / students_num)
            self.case_time.append(all_time / students_num)
            self.case_maxlen.append(all_len / students_num)
            self.case_numOflines.append(all_lines / students_num)
        '''
        #计算方差
        for i in range(0, self.index):
            all_score=0
            for j in range(0,students_num):
                student=students[j]
                if self.case_id[i] in student.case_id:
                    index=student.case_id.index(self.case_id[i])
                    all_score=all_score+(student.final_score[index]-self.case_average_score[i])*(student.final_score[index]-self.case_average_score[i])
                else:
                    all_score=all_score+self.case_average_score[i]*self.case_average_score[i]
            self.case_variance.append(all_score/students_num)
        '''