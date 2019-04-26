import requests
from bs4 import BeautifulSoup

class Conversation:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return "question: " + self.question + "\nanswer: " + self.answer


def get_subjects():
    subjects = []

    response = requests.get("https://basicenglishspeaking.com/daily-english-conversation-topics/")

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.findAll('div', {"class": "su-column-inner su-clearfix"})

    for div in divs:
        links = div.findAll('a')

        for link in links:
            subject = link.text
            subjects.append(subject)

    return subjects

subjects = get_subjects()

print("Total number of subjects : " + str(len(subjects)))

print(subjects)

conversations = []
i = 1

for sub in subjects:
    print('(', i, '/', len(subjects), ')', sub)

    response = requests.get("https://basicenglishspeaking.com/" + sub)

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    qnas = soup.findAll('div', {"class": "sc_player_container1"})

    if i == 3:
        break

    for qna in qnas:
        if qnas.index(qna) % 2 ==0:
            q = qna.next_sibling
        else:
            a=qna.next_sibling
            c=Conversation(q, a)
            conversations.append(c)
    i = i+ 1

print("Total conversations : ", len(conversations))

for c in conversations:
    print(str(c))


# # response = requests.get("http://www.dowellcomputer.com/main.jsp")
#
# response = requests.get("https://www.viasat.com")
#
# html = response.text  # type of html is '<class 'str'>
# print(response.status_code)
# print(html)
#
# # Converting HTML source code to Python object
# soup = BeautifulSoup(html, "html.parser")
# # find an a tag in a td tags
# links = soup.select('td > a')
#
# print(len(links))
#
# for link in links:
#     if link.has_attri('href'):
#         if link.get('href').find('notice') !=-1:
#             print(link.text)
#         else:
#             print("None found")

# JUP-001 branch test"


