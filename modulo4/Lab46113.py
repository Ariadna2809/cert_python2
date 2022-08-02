#Laboratorio 4.6.1.13 El módulo calendar
#Elaborado por: Ariadna Loredo Estrada

import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        calendar.Calendar.__init__(self)
    def count_weekday_in_year(self,year,weekday):
        __weekday_count = 0
        for month in range(1,13):
            for week in self.monthdays2calendar(year,month):
                for date in week:
                    if date[0] > 0 and date[1] == weekday:
                        __weekday_count += 1
        return __weekday_count

c = MyCalendar()
print(c.count_weekday_in_year(year=2019, weekday=0))
print(c.count_weekday_in_year(year=2000, weekday=6))