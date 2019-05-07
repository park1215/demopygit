
# import requests
#
# def testRequest():
#     print("testRequest")
#
# testRequest()

# dict = {}
# dict["one"] = 'ONE'
# dict["two"] = 'TWO'
#
# print(dict)
#
# dictkeys = dict.keys()
# print(type(dictkeys))
#
# print(dict.values())
# print(type(dict.values()))
#
# integer = int('1')
# print(integer)

# repr(x) = Converts object x to a regular expression string

# eval(str) - Evaluates a string and returns an object

# testset = {"apple", "orange", "banana"}
# print(testset)
# testset.add("grape")
# print(testset)
# testset.remove("grape")

# try:
#     testset.remove("mango")
# except:
#     print("Exception occurred")
# finally:
#     print("finally executed")
#
# tupletest = ('one', 'ONE')
# tupledict = {}
# tupledict[tupletest[0]] = tupletest[1]
# print("tupledict : \n"+str(tupledict))
#
# if "apple" not in testset:
#     print("true")
# else:
#     print("false")
#
# testset = ("apPle", "oranGe", "baNana")
#
# testsetUpper = []
#
# for i in testset:
#     # testsetUpper.append(i.upper())
#     # print(i.title())
#     print(i.swapcase())

# print(testsetUpper)

# complist1 = [1, 2, 3, 4]
# complist2 = [1, 2, 3]
#
# poppedlist = complist1.pop()
# print(complist1)
# print(poppedlist)
#
# complist1 = complist1.append('4')
#
# print("***")
# print(str(complist1))
#
#
# if True == False:
#     print("TrueFalse")
# else:
#     print("TrueFalse")

# def isAnagram(str1, str2):
#     sortedStr1 = sorted(list(str1))
#     sortedStr2 = sorted(list(str2))
#     print(sortedStr1)
#     print(sortedStr2)
#     if(len(sortedStr1) != len(sortedStr2)):
#         return False
#     else:
#         if(sortedStr1 == sortedStr2):
#             return True
#         else:
#             return False
#
# print(isAnagram("test", "esttt"))
# print(isAnagram("seanpark", "parksean"))
#
# def reverseString(str):
#     strList = list(str)
#     reversedList = []
#     index = -1
#     for i in strList:
#         if strList[index] != ' ':
#             reversedList.append(strList[index])
#         index = index -1
#     print(reversedList)
#
# reverseString("seanparkatv iasat")
#
# def test_range(num):
#     if num in range(0, 100):
#         print("%s is in range" %str(num))
#     else:
#         print("%s is not in range" %str(num))
#
# test_range(10)
#
# def lowerUpper(str):
#     initial = {"Lower_Case":0, "Upper_Case":0} # initial count of lower and upper
#     for char in str:
#         if(char.islower()):
#             initial["Lower_Case"] = initial["Lower_Case"]+1
#         elif(char.isupper()):
#             initial["Upper_Case"] = initial["Upper_Case"]+1
#         else:
#             pass
#     return initial
#
# print(lowerUpper("iamaboyyouareagirlhappyfridayHappySunda"))

# def occurrenceCheck(str):
#     initial = {} # initial count of chars
#     answer = 0
#     answerKey = None
#     for char in str:
#         if char == " ":
#             pass
#         elif( char not in initial.keys()):
#             initial[char] = 1
#         else:
#             initial[char] = initial[char]+1
#
#     for key in initial.keys():
#         if initial[key] > answer:
#             answer = initial[key]
#             answerKey = key
#     return(answerKey, answer)
#     # return(initial)
#
# print(occurrenceCheck(" ia ma b oy y o u a r e agirlhappyfridayHappySunda yn"))

# def getMaxOccuringChar(str):
#     ASCII_SIZE = 256
#     count = [0] * ASCII_SIZE
#
#     max = -1
#     c = ""
#
#     for i in str:
#         count[ord(i)]+=1
#
#     print(count[ord(i)])
#
#     for i in str:
#         if max < count[ord(i)]:
#             max = count[ord(i)]
#             c = i
#     print(c)
#
# getMaxOccuringChar("testasdfdasfsdfwelqrupczsjfadsjfss")
#
# print(ord('i'))
#

# import math
# print(math.factorial(23))

# def factorial(number):
#     answer = 1
#     if number == 1:
#         return 1
#     else:
#         for i in range(1, number+1):
#             answer = answer*i
#
#     return answer
#
# print(factorial(5))

# def factorial_recur(number):
#     if(number ==1):
#         return 1
#     else:
#         return number*factorial_recur(number-1)
#
# print(factorial_recur(5))

# print('a'.isalpha())
# print('1'.isalpha())
# print('1'.isalphanu)
#
# myList = [1, 2, 3, 4, 5]
# print(myList.append(6))
#
# print(myList)
#
# print(myList.pop())
#
# for _ in range(len(myList)):
#     print(myList.pop())

# word = input("Input a world : ")
# word_list = list(word)
# reversed = []
# for _ in range(len(word_list)):
#     reversed.append(word_list.pop())
#
# print("".join(reversed))
# print(word_list[::-1])

# myList = [1, 2, 3, 4, 5]
# myList.append(60)
# myList.append(70)
# print(myList.pop(0))
# print(myList.pop(0))
# print(myList.pop(0))

# tuple_ex = (1,2,3)
# print(type(tuple_ex))
# t = (1,)
# print(type(t))

# set_ex = [1,2,3,4,4,4,2,5]
# print(set_ex)
# set_ex = set(set_ex)
# print(set_ex)
#
# set_ex1 = {1,2,3,4,4,4,4,5,5,1,2,7,8,0}
# set_ex1.add(9)
# set_ex1.remove(9)
# set_ex1.update([1,2,3,4,4,4,4,5,5,1,2,7,8,10,11])
# print(set_ex1)
# # set_ex1.clear()
#
# set_ex2 = {1,2,3,4,4,4,4,5,5,1,2,7,8}
#
# print(set_ex1.union(set_ex2))
# print(set_ex1 | set_ex2)
#
# print(set_ex1.intersection(set_ex2))
# print(set_ex1 & set_ex2)
#
# print(set_ex1.difference(set_ex2))
# print(set_ex1 - set_ex2)

# student_info = {1 : "Bob", 2:"John", 3:"Tyler", 4:"Ryan"}
# print(type(student_info))
# student_info[5] = "Jon"
# print(student_info)
#
# print(student_info[3])
# print(student_info.keys())
# print(student_info.values())

# print(1 in student_info)
# print("Bob" in student_info)
# print("Bob" in student_info.values())

import csv

def getKey(item): #정렬을 위한 함수
    return item[1] #신경쓸 필요 없음

command_data = [] # 파일 읽기

with open(".\\resource\\command_data.csv", "r", encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)

# print(command_data[:5])
# command_counter={} # dict 생성, 아이디를 key값, 입력줄수를 value 값
#
# for data in command_data: #리스트 데이터를 딕트로 변경
#     if data[1] in command_counter.keys(): #아이디가 이미 키값으로 변경되었을때
#         command_counter[data[1]] += 1 # 기존 출현한 아이디
#     else:
#         command_counter[data[1]] = 1 # 처음 나온 아이디
#
# dictlist = [] # 딕트를 리스트로 변경
# for key, value in command_counter.items():
#     temp = [key, value]
#     dictlist.append(temp)
#
# sorted_dict = sorted(dictlist, key=getKey, reverse=True) # 리스트를 입력 줄 수로 정렬
# print(sorted_dict[:100]) # 리스트의 상위 10 개 값만 출력
#
# testList = [1, 2, 4, 5, 6,3,4,5,6]
# print(sum(testList))

def counter(filename):
    f = open("./resource/"+filename, 'r', encoding="utf-8")
    yesterday_lyric = ""
    while 1:
        line = f.readline()
        if not line:
            break
        yesterday_lyric = yesterday_lyric + line.strip() + "\n"
    f.close()

    n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
    print("Number of a Word 'Yesterday'" , n_of_yesterday)

if __name__ == "__main__":
    filename = "yesterday.txt"
    counter(filename)