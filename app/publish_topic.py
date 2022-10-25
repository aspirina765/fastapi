from azure.servicebus import ServiceBusClient, ServiceBusMessage

import os


class publish_topic():
    connstr = os.environ['SERVICE_BUS_CONNECTION_STR']
    topic_name = os.environ['SERVICE_BUS_TOPIC_NAME']
    subscription_name = os.environ['SERVICE_BUS_SUBSCRIPTION_NAME']

    with ServiceBusClient.from_connection_string(connstr) as client:
        with client.get_topic_sender(topic_name) as sender:
            with open("data.json", "r") as f: 
                    data_tmp = f.read()
                    data = json.loads(data_tmp)
                    
            sender.send_messages(ServiceBusMessage(data))

        # If session_id is null here, will receive from the first available session.
        # with client.get_subscription_receiver(topic_name, subscription_name) as receiver:
        #     for msg in receiver:
        #         print(str(msg))