#!/usr/bin/env python3

import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('alexcamposalexandre@gmail.com', 'kyo_kushin')
conn.sendmail('alexcamposalexandre@gmail.com', 'alex.mca@live.com', \
'Subject: So long...#2\n\nDear Glu, so long and thanks for all \
the fish, I am really grateful!\n\nFrom Alex')
conn.quit()
