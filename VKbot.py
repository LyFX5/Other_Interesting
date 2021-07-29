import serial
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

SERIAL_PORT = 'COM3'
SERIAL_SPEED = 9600
ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)

def write_msg(user_id,message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})

token = "15d1eadf043fd65b39d13e544c42b7681bbae03e2ec2db195fac83b94e9fec383a98a8eeee855576487b4"

xozain = 504125725

vk = vk_api.VkApi(token = token)

longpoll = VkLongPoll(vk)

#write_msg(564443201,"привет")

def build_str(a,f,L):
    st = ""
    for i in range(f,L+1):
        st = st + str(a[i]) + " "
    return st

for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            someone = event.user_id
            request = event.text
            
            if someone == xozain: #хозяин
                command = request.split(" ")
                if len(command) > 2 and command[0] == "отправь":
                    i = 0
                    
                    try:
                        i = int(command[1])
                    except ValueError:
                        #Handle the exception
                        write_msg(xozain,"введите id")
                        
                    write_msg(i,build_str(command,2,(len(command)-1)))
                else:
                    if request == "on":
                        ser.write("N".encode('utf-8'))
                    elif request == "off":
                        ser.write("F".encode('utf-8'))
                    else:
                        write_msg(xozain,"не понял вашей команды")
            else:
                write_msg(xozain,(str(someone) + " " + request))











                
