# -*- coding: UTF-8 -*-
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class SendMails:
    def __init__(self):
        self.HOST = "smtp.jiagouyun.com"
        self.SUBJECT = "驻云自动化运维平台"
        self.FROM="zhuzhuhua@jiagouyun.com"
        self.SENDEREMAILPASSWORD="Zzh63124224"
        self.TO="654568508@qq.com"
        self.msg=MIMEMultipart('related')



    def addimg(self,src,cid):
        fp = open(src,'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID',cid)
        self.msg.attach(msgImage)


    def creatText(self,htmltext):
        msgtext=MIMEText(htmltext,'html','utf-8')
        self.msg.attach(msgtext)



    def creatAppendix(self,filepath,filename):
        attach=MIMEText(open(filepath,'rb').read(),'base64','utf-8')
        attach['Content-Type']='application/octet-stream'
        Content_Disposition_str = "attachment; filename=\"" + "=?utf-8?b?" + "\"" + base64.b64encode(
            filename.encode('UTF-8')) + "\"?=\""
        attach["Content-Disposition"] = Content_Disposition_str.decode("utf-8").encode("gb18030")
        self.msg.attach(attach)


    def send(self,SUBJECT="",FROM="",TO=""):
        if SUBJECT!="":
            self.SUBJECT=SUBJECT
        if FROM!="":
            self.FROM=FROM
        if TO!="":
            self.TO=TO
        self.msg['Subject']=self.SUBJECT
        self.msg['From'] = self.FROM
        self.msg['To'] = self.TO

        try:
            server = smtplib.SMTP_SSL()
            server.connect(self.HOST, "465")
            server.set_debuglevel(1)
            server.login(self.FROM, self.SENDEREMAILPASSWORD)
            server.sendmail(self.FROM, self.TO, self.msg.as_string())
            server.quit()
            print "邮件发送成功"
            return 1
        except Exception as e:
            print "邮件发送失败"
            print str(e)
            return -1