# coding=<encoding name> ： # coding=utf-8
#!/usr/bin/python
import requests
import json
import smtplib
import os
from email.mime.text import MIMEText

base_url = 'https://leetcode-cn.com'
# 获取今日每日一题的题名(英文)
response = requests.post(base_url + "/graphql", json={
    "operationName": "questionOfToday",
    "variables": {},
    "query": "query questionOfToday { todayRecord {   question {     questionFrontendId     questionTitleSlug     __typename   }   lastSubmission {     id     __typename   }   date   userStatus   __typename }}"
})
leetcodeTitle = json.loads(response.text).get('data').get('todayRecord')[0].get("question").get('questionTitleSlug')

# 获取今日每日一题的所有信息
url = base_url + "/problems/" + leetcodeTitle
response = requests.post(base_url + "/graphql", json={
    "operationName": "questionData", 
    "variables": {"titleSlug": leetcodeTitle},
    "query": "query questionData($titleSlug: String!) {  question(titleSlug: $titleSlug) {    questionId    questionFrontendId    boundTopicId    title    titleSlug    content    translatedTitle    translatedContent    isPaidOnly    difficulty    likes    dislikes    isLiked    similarQuestions    contributors {      username      profileUrl      avatarUrl      __typename    }    langToValidPlayground    topicTags {      name      slug      translatedName      __typename    }    companyTagStats    codeSnippets {      lang      langSlug      code      __typename    }    stats    hints    solution {      id      canSeeDetail      __typename    }    status    sampleTestCase    metaData    judgerAvailable    judgeType    mysqlSchemas    enableRunCode    envInfo    book {      id      bookName      pressName      source      shortDescription      fullDescription      bookImgUrl      pressImgUrl      productUrl      __typename    }    isSubscribed    isDailyQuestion    dailyRecordStatus    editorType    ugcQuestionId    style    __typename  }}"})
# 转化成json格式
jsonText = json.loads(response.text).get('data').get("question")
# 题目题号
no = jsonText.get('questionFrontendId')
# 题名（中文）
leetcodeTitle = jsonText.get('translatedTitle')
# 题目难度级别
level = jsonText.get('difficulty')
# 题目内容
context = jsonText.get('translatedContent')
uname = os.environ["username"]
pwd = os.environ["pwd"]

# print(leetcodeTitle)
# print(context)
# print(level)
# print(no)

# 数据全部HTML化
htmlText = """ <head>
        <meta charset=UTF-8>
        <link rel="stylesheet">
        <style>
            code {
                color: blue;
                font-size: larger;
            }
        </style>
        </link>
    </head>
    <body>
<div>
    <h3>Leetcode-每日一题</h3>
    <h4>""" + no + '.' + leetcodeTitle + '.' + level + """</h4>""" + context + '本题连接：<a href=' + url + ">" + url + "</a></div>"


# 邮箱类
class SendEmail:
    def __init__(self, show_name, send_user, email_host, email_port, password, user_list, title, message):
        self.show_name = show_name
        self.send_user = send_user
        self.email_host = email_host
        self.email_port = email_port
        self.password = password
        self.user_list = user_list
        self.message = message
        self.title = title

        
    def send_email(self):
        try:
            user = self.show_name + "<" + self.send_user + ">"
            message = MIMEText(self.message, _subtype='html', _charset='utf-8')
            message['Subject'] = self.title
            message['From'] = user
            message['To'] = ";".join(self.user_list)
            server = smtplib.SMTP_SSL(self.email_host)
            server.connect(self.email_host, self.email_port)
            server.login(self.send_user, self.password)
            server.sendmail(user, self.user_list, message.as_string())
            server.close()
            print("success!!!")
        except Exception as e:
            print("error:", e)


if __name__ == '__main__':
    # 发件人邮箱
    send_user = uname
    # 邮箱对应的host
    email_host = "smtp.163.com"
    email_port = 465
    # 开启SMTP时的密码
    password = pwd
    # 邮件上显示的昵称
    show_name = "QSX1C"
    # 收件人邮箱账户（可多人）
    user_list = ["809549807@qq.com"]
    # 邮件标题
    title = no
    message = htmlText
    send = SendEmail(show_name, send_user, email_host, email_port, password, user_list, title, message)
    send.send_email()
