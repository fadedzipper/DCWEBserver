from django.conf import settings
import  json
import  socket
import  datetime


HOST =  settings.HOST
PORT = settings.PORT

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    mysocket.connect((HOST,PORT))
except Exception as err:
    print(err,"采集服务器连接失败！")


def sendcmd(data):

    try:
        mysocket.send(data.encode())
    except Exception as err:
        print(err)
        mysocket.close()
        return 1

    return 0


def updateConfigCmd(serialnum,key):

    data = {
        'type':"download",
        "option": "updateconf",
        "serialnum": serialnum,
        "key": key
    }

    data=json.dumps(data) +'\r\n\r\n'
    return sendcmd(data)


def activeCmd(serialnum,key):



    data = {
        'type':"download",
        "option": "active",
        "serialnum": serialnum,
        "key": key,
        'status': 1
    }

    data=json.dumps(data) +'\r\n\r\n'

    return sendcmd(data)





