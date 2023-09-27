import paho.mqtt.client as mqtt
import time

"""
    mqtt_client = mqtt.Client("Dados dos Robos")
    mqtt_client.connect(host='localhost', port = 1883)
    mqtt_client.publish(topic="/messge", payload = "Dados do Robo")
"""

class RLCommMqttESQ:
    
    def __init__(self):
        self.__mqtt_client = None

    def start(self):
        mqttBroker = "192.168.0.101" 
        print("Start communication esp ")
        self.__mqtt_client = mqtt.Client(client_id="Dados do robot para o esp")
        self.__mqtt_client.connect(host=mqttBroker)
        print("Ok! comm esp")
    
    def send_UFBOTS(self, robot_commands = []):
        #robo_2 = robot_commands[1]
        #message = f"({robo_2['robot_id']},{abs(robo_2['wheel_left'])},{abs(robo_2['wheel_right'])})"
        #self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=message)
        message = ""
        robot_commands = sorted(robot_commands, key = lambda i: i['robot_id'])
        for rb in robot_commands:
            #message += f"({rb['robot_id']},{abs(rb['wheel_left'])},{abs(rb['wheel_right'])})"
            if (rb['robot_id']==1):
                self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=f"({rb['robot_id']},{abs(rb['wheel_left'])},{abs(rb['wheel_right'])})")
                time.sleep(5)
          
            if (rb['robot_id']==2):
                self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=f"({rb['robot_id']},{abs(rb['wheel_left'])},{abs(rb['wheel_right'])})")
                time.sleep(5)  
            if (rb['robot_id']==3):
                self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=f"({rb['robot_id']},{abs(rb['wheel_left'])},{abs(rb['wheel_right'])})")
                time.sleep(5)  

        #message = message[:-1] + ')'
        #print("Message:" + message)
        #self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=message)


    def send(self, robot_commands = []):
        message = "("
        robot_commands = sorted(robot_commands, key = lambda i: i['robot_id']) #Retorna uma lista ordenada
        for rb in robot_commands: # round arredonda um número
            #message += f"{rb['robot_id']},{round(rb['wheel_left'], 2)},{round(rb['wheel_right'], 2)},"
            
            message += f"{rb['robot_id']},{rb['wheel_left']},{rb['wheel_right']},"
            
            #mes = f"({rb['robot_id']},{rb['wheel_left']},{rb['wheel_right']})"
        message = message[:-1] + ')'
        
        #self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload=message)
        print(message)
        self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload="(2,0,0)")
        #self.__mqtt_client.publish(topic="UFRBots/transmit_robot", payload = message.encode())

