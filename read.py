import json
import student
from urllib.request import urlopen
from io import BytesIO
import zipfile

#根据URL地址读取zip文件，返回所需要的值
#result为返回值
def readbyURL(url):
    try:
        result=[]
        max_len=0
        numOflines=0
        numOfif=0
        remotezip=urlopen(url)
        zipMemory=BytesIO(remotezip.read())
        zip=zipfile.ZipFile(zipMemory)
        code=""
        for fn in zip.namelist():
            if fn.endswith(".zip"):
                new_Memory=BytesIO(zip.read(fn))
                next_zip=zipfile.ZipFile(new_Memory)
                #next_zip是zip文件里面的zip文件
                for fnn in next_zip.namelist():
                    if fnn.endswith(".py"):
                        data=next_zip.read(fnn).decode()
                        for line in data.split('\n'):
                            code+=line
                            numOflines+=1
                            numOfif=numOfif+line.count('if')+line.count('elif')+line.count('else')
                            if len(line)>max_len:
                                max_len=len(line)

        result.append(max_len)
        result.append(numOflines)
        result.append(numOfif)
        result.append(code)
        return result
    except zipfile.BadZipFile:
        return False

#根据文件地址读取文件
def read(filename):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
    students=[]
    students_num=0
    for user_id in data:
        students_num+=1
        dict = data[user_id]
        #cases:每个人的各题成绩
        cases = dict['cases']
        stu = student.student(user_id)
        for case in cases:
            # case_id:题目编号
            # case_type:题目类型
            # final_score:题目最终得分
            # time:做题时长
            # count:提交次数
            case_id=case['case_id']
            case_type=case['case_type']
            final_score=case['final_score']
            start_time=0
            has_start=False
            end_time=0
            code_url=""
            count=0
            for record in case['upload_records']:
                count+=1
                code_url = record['code_url']
                if not has_start:
                    has_start=True
                    start_time=record['upload_time']
                if record['score']>=final_score:
                    end_time=record['upload_time']
            #满分但无记录的情况抛弃，读取的zip文件有问题也抛弃
            if code_url!="":
                time=end_time-start_time
                if time==0:
                    time=1
                list=readbyURL(code_url)
                if list:
                    stu.add_case(case_id,case_type,final_score,time,count,list[0],list[1],list[2],list[3])
        students.append(stu)
    return students