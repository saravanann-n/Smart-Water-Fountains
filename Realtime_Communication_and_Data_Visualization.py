#Real-time Communication: 
#Code to establish a communication link between the Raspberry Pi and the mobile app, enabling real-time updates and notifications.
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt

# MQTT broker settings
broker_address = "mqtt.example.com"
broker_port = 1883
client_id = "raspberry_pi"
 
# Callback function for when the connection is established
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    # Subscribe to topics
    client.subscribe("fountain/status")
    client.subscribe("fountain/readings")
 
# Callback function for when a message is received
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " " + str(msg.payload.decode()))
 
# Create MQTT client instance
client = mqtt.Client(client_id)
 
# Set callback functions
client.on_connect = on_connect
client.on_message = on_message
 
# Connect to MQTT broker
client.connect(broker_address, broker_port, 60)
 
# Start MQTT loop
client.loop_start()
#To publish messages from the Raspberry Pi to the mobile app use the client.publish() method

#Data Visualization: 
#Code to present the analyzed data in a visually appealing manner within the mobile app, allowing users to easily understand the water fountain's status.

# Sample data for water level and temperature
water_level = [10, 15, 20, 25, 30]
temperature = [25, 23, 22, 21, 20]
 
# Create a line chart
plt.plot(water_level, temperature)
 
# Add labels and titles
plt.xlabel('Water Level')
plt.ylabel('Temperature')
plt.title('Water Fountain Status')
 
# Display the chart
plt.show()
