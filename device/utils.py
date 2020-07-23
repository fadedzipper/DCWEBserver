# 计算AQI 一小时
AQI_LIST = {
    "IAQI" :[0,50,100,150,200,300,400,500],
    "PM25" :[0,35,75,115,150,250,350,500],
    "SO2"  : [0,150,500,650,800],
    "NO2" : [0,100,200,700,1200,2340,3090,3840],
    "PM10" : [0,50,150,250,350,420,500,600],
    "CO" : [0,5,10,35,60,90,120,150],
    "O3" : [0,160,200,300,400,800,1000,1200]
}


def getIndex(value,query_type):

    query_list = AQI_LIST[query_type]

    for i in  range(1,len(query_list)):
        if value  < query_list[i]:
            return i
    return i

def getAQI(value,query_type):

    query_list =  AQI_LIST[query_type]
    iaqi_list = AQI_LIST["IAQI"]

    i = getIndex(value, query_type)

    return ((iaqi_list[i] - iaqi_list[i-1])/(query_list[i]-query_list[i-1])) \
    * (value - query_list[i-1]) +iaqi_list[i-1]


