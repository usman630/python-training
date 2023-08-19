import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.utils import make_msgid
from email.mime.application import MIMEApplication




email_from_addr = "pinjariusman600@gmail.com"
email_to_addr = "usmanbashap@pathbreakertech.com"
email_smtp_server = "smtp.gmail.com"
email_smtp_port = "587"
email_user = "pinjariusman600@gmail.com"
email_password = "ctbibyimapooealh"
# email_subject = "NERS"

email_subject = "NERS"

email_body = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            margin: 50px;
        }
        a{
            text-decoration: none;
          }
        .img{
            height: 120px;
            width: 150px;
        }
        .container {
            display: flex;
        }
        .ceo_div{
            margin-left: 30px;
            font-size: 15px;
        }
        .content_div{
            width: 70vw;
        }
        .text_color{
            color: #7a216d;
        }
    </style>
</head>
<body>
    <h4>Hi--</h4>
    <h5>National employee regulatory system</h5>
    <div>
        <div>
            <div>
                <div class="container">
                    <div class="">
                        <img class="img" src="https://nersorg.in/wp-content/uploads/2023/03/ners-logo.png" alt="">
                    </div>
                    <div class="ceo_div">
                        <h5> NERS Team <br> Mobile: +91 8501926527 <br> Website: <a href="https://nersorg.in/">nersorg.in</a></h5>
                    </div>
                </div>
                <div class="content_div text_color">
                    <p><b>Disclaimer:</b> The information contained in this email (including any attachments) is privileged and confidential. If you have received it by mistake, please notify the sender by return e-mail and permanently delete this e-mail and any attachments from your system. Any dissemination, use, review, distribution, printing or copying of this message in whole or in part is strictly prohibited. Please note that emails are susceptible to change. NERS(including its group companies) shall not be liable for the improper or incomplete transmission of the information contained in this communication nor for any delay in its receipt or damage to your system. NERS (or its group companies) does not guarantee that the integrity of this communication has been maintained or that this communication is free of Viruses, interceptions or interference.</p>
                    <p><b>Notice:</b> The information contained in this email, message and/or attachments to it may contain confidential or privileged information. If you are not the intended recipient, any dissemination, use, review, distribution, printing or copying of the information contained in this e-mail message and/or attachments to it are strictly prohibited. If you have received this communication in error, please notify us by reply e-mail or telephone and immediately and permanently delete the message and any attachments. <br> This email is intended for all HR users, in case you are not a correct recipient, please send an email to <a href="#">info@nerss.org.in</a> to remove your ID from the mailing group</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

message = MIMEMultipart('alternative')
message['From'] = email_from_addr
message['To'] = email_to_addr
# message['Subject'] = email_subject
body = email_body
message.attach(MIMEText(body, 'html'))


pdf_filename = r'C:\Users\PATH-04\Downloads\usman_payslip.pdf'
with open(pdf_filename, 'rb') as pdf_file:
    pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
    pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_filename}')
    message.attach(pdf_attachment)


server = smtplib.SMTP(email_smtp_server,int(email_smtp_port))
text = message.as_string()
server.starttls()
server.login(email_user, email_password)
server.sendmail(email_from_addr,email_to_addr,message.as_string())
server.quit()






































# pdfname = 'usman_payslip.pdf'
# binary_pdf = open(pdfname, 'rb')
# payload = MIMEBase('application', 'octate-stream', Name=pdfname)
# payload.set_payload((binary_pdf).read())
# encoders.encode_base64(payload)
# payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
# message.attach(payload)


# pdfname = 'usman_payslip.pdf'
# with open(pdfname, 'rb') as pdf_file:
#     pdf_attachment = MIMEApplication(pdf_file.read(), Name=pdfname)

# pdf_attachment['Content-Disposition'] = f'attachment; filename={pdfname}'
# message.attach(pdf_attachment)






# import smtplib
# import getpass
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# host = "smtp.gmail.com"
# # "smpt-mail.outlook.com"
# # "smtp.gmail.com"
# email_smtp_port = "587"



# email_from_addr = "usmanbashap@pathbreakertech.com"

# email_to_addr = "usmanjawan33@gmail.com"

# # email_smtp_server = "smtp.gmail.com"
# # email_user = "myfromemail"

# email_password = "nbnybqaozqlmxvck"

# msg = MIMEMultipart("alternative")

# msg['subject'] = "Mail sent using python"
# msg["From"] = email_from_addr
# msg["To"] = email_to_addr
# msg["cc"] = email_from_addr
# msg["Bcc"] = email_from_addr

# html = ""
# with open("email.html","r") as file:
#     html = file.read()

# html_part = MIMEText(html,'html')
# msg.attach(html_part)

# smtp = smtplib.SMTP(host,email_smtp_port) 

# status_code, response = smtp.ehlo()
# print(f"[*] Echoing the server: {status_code} {response}")

# status_code, response = smtp.starttls()
# print(f"[*] starting TLS connection: {status_code} {response}")

# status_code, response = smtp.login(email_from_addr,email_password)
# print(f"[*] Logging in: {status_code} {response}")

# smtp.sendmail(email_from_addr,email_to_addr, msg,msg.as_string())
# smtp.quit()









# import smtplib
# import getpass

# email_from_addr = "pinjariusman600@gmail.com"
# email_to_addr = "usmanjawan33@gmail.com"
# email_password = input(str("Enter password: "))
# msg = "Hey, This is usman"

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(email_from_addr,email_password)
# print("Login success")
# server.sendmail(email_from_addr,email_to_addr,msg)
# print("Email sent")













# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


# email_from_addr = "usmanbashap@pathbreakertech.com"
# email_to_addr = "pinjariusman600@gamil.com"
# email_smtp_server = "smtp.gmail.com"
# email_smtp_port = "587"
# email_user = "usman"
# email_password = "nbnybqaozqlmxvck"


# #Email Subject
# email_subject = "Welcome to Python Email Test"
# email_body = None
# email_body_header = ' '
# email_body_header = email_body_header + '<html><head></head><body>'
# email_body_header = email_body_header + '<style type="text/css"></style>'
# email_body_header = email_body_header + '<br><p>Hello Team,<br><br>This is a test email.<br>'

# email_body_content = ' '
# email_body_content = email_body_content + '<H1>This is main content area</h1>'

# email_body_footer = ' '
# email_body_footer = email_body_footer + '<br>Thank you'
# email_body_footer = email_body_footer + '<br>Support Team<br>'

# email_body = str(email_body_header) + str(email_body_content) + str(email_body_footer)

# message = MIMEMultipart('alternative')
# message['From'] = email_from_addr
# message['To'] = email_to_addr
# message['Subject'] = email_subject
# body = email_body
# message.attach(MIMEText(body, 'html'))

# # print (email_body)


# server = smtplib.SMTP(email_smtp_server,int(email_smtp_port))
# text = message.as_string()
# server.starttls()
# server.login(email_user, email_password)
# server.sendmail(email_from_addr,email_to_addr,message.as_string())
# server.quit()











