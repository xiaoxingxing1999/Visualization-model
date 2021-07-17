import read
import caculator
import exclude
import sortStudents
import sortTopic
import os

#该函数负责处理命令

sample='data/sample.json'
test_data='data/test_data.json'
my_test='data/my_test.json'

target=""
file_name=input("请输入需要处理的文件(1:sample/2:test_data/3:my_test)：")
if file_name=="1":
    target=sample
elif file_name=="2":
    target=test_data
elif file_name=="3":
    target=my_test
else:
    print("没有该文件")

if target!="":
    print("请等待数据读取…………")
    students = read.read(target)
    print("数据读取完毕！")

    index = input("是否检测代码抄袭(1:是/0:否):")
    if index == "1":
        exclude.detectCheat(students)
    index = input("是否剔除异常数据(1:是/0:否):")
    if index=="1":
        exclude.get_real_students(students)

    service = input("请输入你需要的服务(1:学生编程能力排行/2:题目难度排行:")
    while service!="":
        if service=="1":
            sortStudents.sort(students)
        elif service=="2":
            sortTopic.sort(caculator.caculator(students))
        else:
            print("没有该服务！")
        service = input("请输入你需要的服务(1:学生编程能力排行/2:题目难度排行:")


os.system("pause")