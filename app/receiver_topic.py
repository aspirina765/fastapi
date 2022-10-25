from azure.servicebus import ServiceBusClient, ServiceBusMessage

import os


class receive_topic():
    connstr = os.environ['SERVICE_BUS_CONNECTION_STR']
    topic_name = os.environ['SERVICE_BUS_TOPIC_NAME']
    subscription_name = os.environ['SERVICE_BUS_SUBSCRIPTION_NAME']

    with ServiceBusClient.from_connection_string(connstr) as client:
        # with client.get_topic_sender(topic_name) as sender:
        #     sender.send_messages(ServiceBusMessage("Data"))

        # If session_id is null here, will receive from the first available session.
        with client.get_subscription_receiver(topic_name, subscription_name) as receiver:
            for msg in receiver:
                print(str(msg))
                with open("data.json", "w") as f: 
                    f.write(json.dumps(msg))