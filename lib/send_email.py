import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

class Email:

    @classmethod
    def send_email(cls):
        # 邮件信息配置. 授权码 xdclass123
        sender = '498431861@qq.com'
        receiver = 'fhqqtd305@gmail.com'
        auth_code = 'dqljqxjwveqobihe'  # 设置客户端授权码，不是密码

        smtp_server = 'smtp.qq.com'
        smtp_port = 587
        subject = '自动化测试报告'

        # 定义发送内容
        msg = MIMEText("hello", _subtype="plan", _charset="utf-8")
        msg["Subject"] = subject  # 主题
        msg["From"] = sender  # 发件人
        msg["To"] = receiver  # 收件人

        # 拿到对象
        smtp = smtplib.SMTP()
        # 连接smtp服务器
        smtp.connect(smtp_server, smtp_port)
        # 登录服务器,发件人和授权码
        smtp.login(sender, auth_code)
        # 发送邮件，传入发送/接收者，消息内容
        smtp.sendmail(sender, receiver, msg.as_string())
        # 退出
        smtp.quit()

    # @classmethod
    # def send_test_report(cls):
    #     # 邮件信息配置. 授权码 xdclass123
    #     sender = '498431861@qq.com'
    #     receiver = 'fhqqtd305@gmail.com'
    #     auth_code = 'dqljqxjwveqobihe'  # 设置客户端授权码，不是密码
    #
    #     smtpserver = 'smtp.qq.com'
    #     subject = '自动化测试报告'
    #
    #     # 读取文件内容
    #     f = open("./result.html", 'rb')
    #     mail_body = f.read()
    #     f.close()
    #
    #     # HTML 形式的文件内容
    #     html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    #     html['Subject'] = subject
    #     html['from'] = sender
    #     html['to'] = receiver
    #
    #     # html附件 将测试报告放在附件中发送
    #     att1 = MIMEText(mail_body, 'base64', 'gb2312')
    #     att1["Content-Type"] = 'application/octet-stream'
    #     att1["Content-Disposition"] = 'attachment; filename="XdclassTestReport.html"'  # 这里的filename可以任意写
    #
    #     msg = MIMEMultipart()
    #     msg['Subject'] = subject  # 邮件的标题
    #     msg.attach(html)  # 将html附加在msg里
    #     msg.attach(att1)  # 新增一个附件
    #
    #
    #     # 连接 登录 上smtp服务器
    #     smtp = smtplib.SMTP()
    #     smtp.connect('smtp.qq.com')
    #     smtp.login(sender, auth_code)
    #
    #     # 发送邮件
    #     smtp.sendmail(sender, receiver, msg.as_string())
    #     smtp.quit()

if __name__ == '__main__':
    Email.send_email()