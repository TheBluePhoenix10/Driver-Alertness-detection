from twilio.rest import Client
import datetime
import sqlite3 
from datetime import timedelta
account_sid = 'AC69c19db776ae2aea52705d2f76380916'
auth_token = 'da35813d56f92be4d77844ac4cce131c'
client = Client(account_sid, auth_token)


now = datetime.date.today()

print
print ("Current date and time using str method of datetime object:")
print (now)

def search(Name="",LicenseNo="",UserID=""):
    conn=sqlite3.connect("DDetails.db")
    cur=conn.cursor()
    cur.execute("SELECT MobileNo FROM driver WHERE Name=? OR LicenseNo=? OR UserID=?", (Name,LicenseNo,UserID))
    rows=cur.fetchone()
    row=(rows[0])
    conn.close()
    return row

def search2(Name="",LicenseNo="",UserID=""):
    conn=sqlite3.connect("DDetails.db")
    cur=conn.cursor()
    cur.execute("SELECT MaintenanceDate FROM driver WHERE Name=? OR LicenseNo=? OR UserID=?", (Name,LicenseNo,UserID))
    rows=cur.fetchone()
    row=(rows[0])
    conn.close()
    return row

def update(UserID,date):
    conn=sqlite3.connect("DDetails.db")
    cur=conn.cursor()
    cur.execute("UPDATE driver SET MaintenanceDate=?   WHERE UserID=?",(date,UserID))
    conn.commit()
    conn.close()

UserID="GoodKid"
date=search2("","",UserID)

newdate=(datetime.date.today() + timedelta(days=35))

if str(date)==str(now):
	UserID="GoodKid"
	mob=search("","",UserID)

	message = client.messages.create(
	                              from_='+12033447716',
	                              body='Today is your maintenance date.',
	                              to='+91'+mob
	                          )
	update(UserID,newdate)
	print(message.sid)


