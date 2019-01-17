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

#将不符合规格的日期加上2019
def add_year_date(str_date):
    if(is_valid_date(str_date)):
        str_date = str_date
    else:
        str_date = '2019-'+str_date
    return str_date

print(add_year_date('01-01'))

#判断日期是否在指定时间范围内
def is_target_date(str_date,start_date):
    cur_array = time.strptime(str_date,"%Y-%m-%d")
    cur_stamp = time.mktime(cur_array)
    start_array = time.strptime(start_date,"%Y-%m-%d")
    start_stamp = time.mktime(start_array)
    return cur_stamp >= start_stamp

print(is_target_date('2017-01-01','2018-01-01'))  # False
print(is_target_date('2019-01-01','2018-01-01'))  # True
print(is_target_date('2018-01-01','2018-01-01'))  # True