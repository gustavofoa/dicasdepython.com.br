from datetime import datetime

str_date = '11/07/2018'

date = datetime.strptime(str_date, '%d/%m/%Y').date()

print(date, type(date))

str_date = '2018-07-11'

date = datetime.strptime(str_date, '%Y-%m-%d').date()

print(date, type(date))