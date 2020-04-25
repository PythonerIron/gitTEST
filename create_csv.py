import csv
import random


csvFile=open("/Users/suntie/DEV/pycharm_projects/pycharm_project/new_anapro/wuqi.csv",'w',newline='')

try:
    writer=csv.writer(csvFile)
    get_the_customer_name = list()
    for i in range(1,101):
        get_the_customer_name.append('客户编号'+str(i))
    get_the_customer_name = tuple(get_the_customer_name)
    # print('get_the_customer_name',get_the_customer_name)
    # writer.writerow(('number','number plus 2','number times 2'))
    writer.writerow(get_the_customer_name)
    update_data = list()
    for i in range(100):
        for j in range(100):
            update_data.append(random.randint(0,1))
        writer.writerow(tuple(update_data))
        update_data.clear()
        # writer.writerow((random.random(),random.random(),random.random()))
finally:
    csvFile.close()
# try:
#     with open('/Users/suntie/DEV/Jupyter_note/wuqi.csv','r') as f:
#         reader = csv.reader(f)

'''
trouble



'''
#         # print(type(reader)
#         # result = list(reader)
#         # print(result)
#         for row in reader:
#             print('+++',type(row),row)
# finally:
#     print('------------------')
