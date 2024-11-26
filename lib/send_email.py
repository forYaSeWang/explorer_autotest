import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮件信息配置
sender = '498431861@qq.com'
# 设置客户端授权码，不是密码
auth_code = 'dqljqxjwveqobihe'
# smtp服务器配置
smtp_server = 'smtp.qq.com'
smtp_port = 587

# 接收者邮箱 - 必须指定为字符串形式
receiver_email = 'fhqqtd305@gmail.com,chenhan921226@gmail.com'


class Email:

    def send_email(self, body):
        """
        - 发送邮件
        :param body: 普通字符串内容
        :return: None
        """
        subject = '自动化测试报告'

        # 定义发送内容
        msg = MIMEMultipart()
        msg["Subject"] = subject  # 主题
        msg["From"] = sender  # 发件人
        msg.attach(MIMEText(body, 'plain'))

        # 拿到对象
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        # 启动加密连接，连接smtp服务器
        smtp.starttls()
        # 登录服务器,发件人和授权码
        smtp.login(sender, auth_code)

        # 循环发送邮件，传入发送/接收者，消息内容
        smtp.sendmail(sender, receiver_email.split(','), msg.as_string())
        # 退出
        smtp.quit()
        print("All emails sent successfully.")

    def send_test_report(self, body, zip_file):
        """
        - 发送邮件 文本内容及附件
        :param report_path: html文件路径
        :return: None
        """
        subject = '自动化测试报告'

        msg = MIMEMultipart()
        msg['Subject'] = subject  # 邮件的标题
        msg["From"] = sender  # 发件人
        msg.attach(MIMEText(body, 'plain'))

        # 读取文件内容
        attachment = open(zip_file, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename= {zip_file}")
        # 新增一个附件
        msg.attach(p)

        # 拿到对象
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        # 启动加密连接，连接smtp服务器
        smtp.starttls()
        # 登录服务器,发件人和授权码
        smtp.login(sender, auth_code)

        # 发送邮件
        smtp.sendmail(sender, receiver_email.split(","), msg.as_string())
        smtp.quit()
        print("All emails sent successfully.")

    def send_test_html_report(self, report_path):
        """
        - 发送邮件 html报告及附件
        :param report_path: html文件路径
        :return: None
        """
        subject = '自动化测试报告'

        # 读取文件内容
        f = open(report_path, 'rb')
        mail_body = f.read()
        f.close()

        # HTML 形式的文件内容
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        html['Subject'] = subject
        html['From'] = sender
        html["To"] = receiver_email

        # html附件 将测试报告放在附件中发送
        att1 = MIMEText(mail_body, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写

        msg = MIMEMultipart()
        msg['Subject'] = subject  # 邮件的标题
        msg["From"] = sender  # 发件人
        msg.attach(html)  # 将html附加在msg里
        msg.attach(att1)  # 新增一个附件

        # 拿到对象
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        # 启动加密连接，连接smtp服务器
        smtp.starttls()
        # 登录服务器,发件人和授权码
        smtp.login(sender, auth_code)

        # 发送邮件
        smtp.sendmail(sender, receiver_email.split(","), msg.as_string())
        smtp.quit()
        print("All emails sent successfully.")


if __name__ == '__main__':
    # body = "test send email"
    # Email().send_email(body)

    # report_path = "/Users/zhaofeng/Documents/workers/xingcuang/explorer_autotest/result.html"
    # Email().send_test_html_report(report_path)

    Email().send_test_report("body", "/Users/zhaofeng/Documents/workers/xingcuang/explorer_autotest/result/test.zip")
