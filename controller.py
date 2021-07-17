import read
import caculator
import exclude
import sortStudents
import sortTopic

#该函数是控制台，主要负责测试
sample='data/sample.json'
test_data='data/test_data.json'
my_test='data/my_test.json'

target=my_test


students=read.read(target)

#题目难度排序
data=caculator.caculator(students)
dict=sortTopic.sort(data)


#学生编程能力排序
sortStudents.sort(students,dict)


