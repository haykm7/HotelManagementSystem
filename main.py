import sqlite3
from datetime import datetime, date

con = sqlite3.connect('test.db')
cur = con.cursor()
table_number = 1

def reserve_room(room_num,str_day,end_day,name,surname,phonenumber,address):
    reserved = False
    for reserved_data in cur.execute("SELECT * FROM room"+f"{room_num}"):
        if datetime.strptime(reserved_data[0], '%d-%m-%Y') < datetime.strptime(str_day, '%d-%m-%Y') and datetime.strptime(reserved_data[1], '%d-%m-%Y') > datetime.strptime(end_day, '%d-%m-%Y'):
            reserved = True
            break
    if reserved == True:
        print("Sorry the room is reserved during that period")
    else:
        price = 100*(datetime.strptime(end_day, '%d-%m-%Y')-datetime.strptime(str_day, '%d-%m-%Y')).days
        cur.execute(f"INSERT INTO room1 VALUES ('{str_day}','{end_day}','{name}','{surname}',{phonenumber},{price},'{address}')")


def amend_rec(room_num,old_phonenumber,str_day,end_day,name,surname,phonenumber,address):
    new_price = 100 * (datetime.strptime(end_day, '%d-%m-%Y') - datetime.strptime(str_day, '%d-%m-%Y')).days
    cur.execute("UPDATE room"+f"{room_num} SET (Start,End,Name,Surname,Phonenumber,Price,Address)  = ('{str_day}','{end_day}','{name}','{surname}',{phonenumber},{new_price},'{address}') WHERE Phonenumber = {old_phonenumber}")

def get_info(room_num,name,phonenumber):
    for i in cur.execute("SELECT * FROM room"+f"{room_num}"+" " + f"WHERE Name = '{name}' AND Phonenumber = {phonenumber}"):
        print(i)

def get_alloted(str_day,end_day,room = 'All'):
    if room == 'All':
        for i in range(1,table_number+1):
            for j in cur.execute("SELECT * from room" + f"{i}"):
                if datetime.strptime(str_day, '%d-%m-%Y') < datetime.strptime(j[0], '%d-%m-%Y') and datetime.strptime(end_day, '%d-%m-%Y') > datetime.strptime(j[1], '%d-%m-%Y'):
                    print(j)
    if room != 'All':
        for j in cur.execute("SELECT * from room" + f"{room}"):
            if datetime.strptime(str_day, '%d-%m-%Y') < datetime.strptime(j[0], '%d-%m-%Y') and datetime.strptime(
                    end_day, '%d-%m-%Y') > datetime.strptime(j[1], '%d-%m-%Y'):
                print(j)

def get_bill(room_num, name, surname):
    for i in cur.execute("SELECT Price from room"+f"{room_num}" + " "+ f"WHERE Name = '{name}' AND Surname = '{surname}'"):
        print(i)

def delete_record(room_num, name, surname):
    cur.execute("DELETE FROM room"+f"{room_num}" + " "+f"WHERE Name = '{name}' AND Surname = '{surname}'")


reserve_room(1,'15-09-2014','10-10-2014','na','n',53258)
amend_rec(1,56928646,'12-09-2016', '20-10-2016', 'Jorge', 'Keyne', 735262258)
get_info(1,'Bob',4726953258)
get_alloted('02-08-2016','07-11-2016')
get_bill(1,'Bob','Waltz')
delete_record(1,'Anna','Margaryan')



con.commit()
con.close()


