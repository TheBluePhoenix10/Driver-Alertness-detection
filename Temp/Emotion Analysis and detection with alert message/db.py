import sqlite3 

def search(Name="",LicenseNo="",UserID=""):
    conn=sqlite3.connect("DDetails.db")
    cur=conn.cursor()
    cur.execute("SELECT MobileNo FROM driver WHERE Name=? OR LicenseNo=? OR UserID=?", (Name,LicenseNo,UserID))
    rows=cur.fetchone()
    row=(rows[0])
    conn.close()
    return row

UserID="GoodKid"
mob=search("","",UserID)
print(mob)