import datetime


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

DATE_FORMAT = "%Y-%m-%d"
def is_valid_date(cls,str_date):