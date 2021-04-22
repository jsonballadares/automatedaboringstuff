import smtplib

connection = smtplib.SMTP('smtp.gmail.com', 587)
print(connection.ehlo())
print(connection.starttls())
print(connection.login('jsonballadares@gmail.com', ''))
connection.sendmail('jsonballadares@gmail.com', 'jsonballadares@gmail.com',
                    'Subject: So long...\n\nDear Jason,\nSo long and thanks for all the fish.\n\n-Jason')
print(connection.quit())
