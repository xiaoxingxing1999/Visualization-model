import student
import math

def sort(students,dict):
    print("学生编程能力排序:")
    index=[]
    stu_dict={}
    for i in range(len(students)):
        student=students[i]
        #该成绩计算公式可以根据实际情况修改
        #index.append((sum(student.final_score)*sum(student.numOflines)*pow(10,9)/(sum(student.time)*max(student.max_len))))
        score=0
        for j in range(len(student.case_id)):
            score=score+student.final_score[j]*dict[student.case_id[j]]/100#根据每道题的难度重新算出这个学生每道题的分数
        index.append(score)
        stu_dict[student.id]=score
    new_index=index[:]
    new_index.sort(reverse=True)
    dict={j:i+1 for i,j in enumerate(new_index)}
    dictSortStu_List = sorted(stu_dict.items(), key=lambda x: x[1], reverse=False)
    '''
    for i in range(len(students)):
        print("学生:%s 成绩:%f 排名:%d"%(students[i].id,index[i],dict[index[i]]))
    '''
    for i in range(len(dictSortStu_List)):
        print("学生:",dictSortStu_List[i][0]," 能力:",dictSortStu_List[i][1]," 排名:",len(students)-i)
