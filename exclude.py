import student
import difflib

#该函数负责删除不正常的数据
def get_real_students(students):
    real_students=[]
    i=0
    students_num=len(students)
    print("开始剔除异常数据——————————————————————————————————————")
    while i<students_num:
        j=0
        while j<students[i].index:
            #如果一题使用if、else、elif次数超过20，则判断面向用例
            if students[i].numOfif[j]>20:
                print("学生%s的第%s题可能面向用例，该题被剔除！"%(students[i].id,students[i].case_id[j]))
                del students[i].case_id[j]
                del students[i].case_type[j]
                del students[i].final_score[j]
                del students[i].max_len[j]
                del students[i].numOflines[j]
                del students[i].numOfif[j]
                del students[i].code[j]
                del students[i].time[j]
                del students[i].count[j]
                students[i].index -= 1
                j-=1
            j+=1
        #如果学生做题数目少于15题，则不考虑该人
        if students[i].index<15:
            print("学生%s做的正常题目数目过少，该学生被剔除！"%(students[i].id))
            del students[i]
            i-=1
            students_num-=1
        i+=1
    print("结束剔除异常数据——————————————————————————————————————")
    return students

#检测代码抄袭
def detectCheat(students):
    print("开始检测代码抄袭——————————————————————————————————————")
    case_id=[]
    student_num=len(students)
    #提取所有题目id
    for i in range(0, student_num):
        student = students[i]
        for j in range(0, student.index):
            if not student.case_id[j] in case_id:
                case_id.append(student.case_id[j])
    #根据题目id将代码比较
    #student_param:记录学生的索引
    #isCheat:记录是否抄袭
    for i in range(0,len(case_id)):
        student_param=[]
        code=[]
        isCheat=[]
        for j in range(0,student_num):
            student=students[j]
            for k in range(0,student.index):
                if case_id[i]==student.case_id[k]:
                    student_param.append(j)
                    code.append(student.code[k])


        # 判断是否抄袭
        title_num=len(student_param)
        for j in range(0,title_num):
            isCheat.append(False)
        for j in range(0,title_num):
            for k in range(0,title_num):
                if j!=k and difflib.SequenceMatcher(None,code[j],code[k]).quick_ratio()>0.8:
                    isCheat[j]=True
                    isCheat[k]=True


        #将抄袭的题目删除
        for j in range(0,len(isCheat)):
            if isCheat[j]:
                student_index=student_param[j]
                title_index = students[student_param[j]].case_id.index(case_id[i])
                print("学生%s的第%s题可能抄袭，该题被剔除！"%(students[student_index].id,case_id[i]))
                del students[student_index].case_id[title_index]
                del students[student_index].case_type[title_index]
                del students[student_index].final_score[title_index]
                del students[student_index].max_len[title_index]
                del students[student_index].numOflines[title_index]
                del students[student_index].numOfif[title_index]
                del students[student_index].code[title_index]
                del students[student_index].time[title_index]
                del students[student_index].count[title_index]
                students[student_index].index -= 1

    print("结束检测代码抄袭——————————————————————————————————————")



