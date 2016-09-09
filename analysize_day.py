#coding=utf8
import csv
import time
import Apriori
import Imp_Apriori

time_start=time.time()

calcu_list = []
sum_list = []

start_date = '20160801'
end_time = '20160831'
stocks = ['600366', '600651', '600848', '601222', '601567', '603100']
#print stocks[0]


#stock = 'E:\python-works\BKLD_API\myTry\Data\sz.txt'
#stock_list = [line.split() for line in open(stock).readlines()]
#print stock_list
#print stock_list[0][0]
#size = len(stock_list)
#print size


stock_detail = 'D:/Program Files/python project/python-works-Heather/BKLD_API/MyTry/PC/Data/8_day/'

def dataset(number):
    with open(stock_detail + stocks[number] + '.SH.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row



for i in range(len(stocks)):    #size
    code = [row["chCode"] for row in dataset(i)]
    date = [row["nDate"] for row in dataset(i)]
    bigRise = [row["nTrend"] for row in dataset(i)]
    #print code
    #print date
    #print bigRise

    #print len(code)
    #print len(date)
    #print len(bigRise)

    #print date[0]
    #print start_date

    for n in range(len(date)):
        if date[n] == start_date:
            flag1 = n

        if date[n] == end_time:
            flag2 = n




for day in range(flag1, flag2 + 1):

    calcu_list = []

    for i in range(len(stocks)):  # size
        code = [row["chCode"] for row in dataset(i)]
        date = [row["nDate"] for row in dataset(i)]
        bigRise = [row["nTrend"] for row in dataset(i)]
        # print code
        # print date
        # print bigRise

        # print len(code)
        # print len(date)
        # print len(bigRise)

        # print date[0]
        # print start_date

        #print bigRise[i]



        if len(bigRise) == 23:
            if bigRise[day] == '1':
                calcu_list.append(code[day])
        #else:
        #    print code[0] + ' does not have enough days'
        #print calcu_list

    sum_list.append(calcu_list)
    #print sum_list


print sum_list
print len(sum_list)

minSupport = 0.1
minConf = 0.1

L,SupportData = Apriori.apriori(sum_list,minSupport)
rules = Apriori.generateRules(L,SupportData,minConf)
print rules

time_end=time.time()
print u"总运行时间为："
print time_end-time_start