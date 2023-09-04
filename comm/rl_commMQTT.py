import paho.mqtt.client as mqtt

"""
    mqtt_client = mqtt.Client("Dados dos Robos")
    mqtt_client.connect(host='localhost', port = 1883)
    mqtt_client.publish(topic="/messge", payload = "Dados do Robo")
"""

class RLCommMqtt:
    
    def __init__(self):
        self.__mqtt_client = None

"""
    def start(self):
        print("Start communication")
        self.__mqtt_client = mqtt.Client(client_id="Dados dos Robot")
        self.__mqtt_client.connect(host='localhost', port = 1883)
        print("Ok! comm")

    def send(self, robot_commands = []):
        message = "<"
        robot_commands = sorted(robot_commands, key = lambda i: i['robot_id']) #Retorna uma lista ordenada
        for rb in robot_commands: # round arredonda um número
            message += f"{rb['robot_id']},{round(rb['wheel_left'], 2)},{round(rb['wheel_right'], 2)},"

        message = message[:-1] + '>'

        self.__mqtt_client.publish(topic="/messages", payload = message.encode())
"""