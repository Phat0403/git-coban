import os

import pandas as pd
import yagmail as yg
import pandas

user=os.getenv('USER')
password=os.getenv('PASSWORD')
subject="""
This is the subject!
"""
yag=yg.SMTP(user=user,password=password)
df=pd.read_csv('contacts.csv')
for index,row in df.iterrows():
    contents=[f"""Hey, Ardit you have to pay {row['amount']} Bill is attached!""",row['filepath']]
    yag.send(to=row['email'],subject=subject,contents=contents)
    print("Gui email thanh cong")