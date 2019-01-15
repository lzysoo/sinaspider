import datetime
import time

#class Date:
#获取两个日期间的所有日期
def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list
print(getEveryDay('2016-01-01','2017-05-11'))


#比较大小
strftime = datetime.datetime.strptime("2017-11-02", "%Y-%m-%d")
strftime2 = datetime.datetime.strptime("2017-01-04", "%Y-%m-%d")
print("2017-11-02大于2017-01-04：",strftime>strftime2)

#判断日期是否符合格式
def is_valid_date(str_date):
    try:
       time.strptime(str_date,"%Y-%m-%d")
       return True
    except:
       return False

print(is_valid_date('12-8'))

def add_year_date(str_date):
    if(is_valid_date(str_date)):
        str_date = str_date
    else:
        str_date = '2019-'+str_date
    return str_date

print(add_year_date('01-01'))