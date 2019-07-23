import smtplib
def smtp(name,link,otp,email):
    msg = "--*--*---------veriifcation mail----------*--*--\n\n\n" \
          "dont  ,%s \n\n" \
          "share this otp with the third person.\n\n" \
          "    this is for security reasons\n\n" \
          "  link             : %s \n\n" \
          "otpgentime      : %s \n\n" % (name, link, str(otp))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('pranitverma43@gmail.com', 'pv9418893098PV')
    server.sendmail('pranitverma43@gmail.com', email, msg)
    server.quit()