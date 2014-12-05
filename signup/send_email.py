import smtplib


def send_email(reciever, ref_id):
    user = 'gjain@jiffynow.in'
    pwd = 'gauravjain'
    smtpserver = smtplib.SMTP_SSL("smtp.zoho.com",465)
    smtpserver.ehlo()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(user, pwd)
    header = 'To:' + reciever + '\n' + 'From: ' + user + '\n' + 'Subject:testing \n'
    msg = header + '\n this is test msg from Jiffy \n\n'+'http://jiffyPreLaunch.com?referral_id='+ref_id
    smtpserver.sendmail(user, reciever, msg)
    smtpserver.close()