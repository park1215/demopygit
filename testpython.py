
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