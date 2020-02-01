import os
from slackclient import SlackClient

# CPS-847-Bot Slack
SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN')

# Hardcoded SLACK_API_TOKEN
client = SlackClient(SLACK_API_TOKEN)

def echo(data):
    # echo text
    client.api_call('chat.postMessage',
        channel=data['channel'],
        text= data.get('text'),
        thread_ts=data['ts']
    )

if __name__ == "__main__":
    if client.rtm_connect():
        print("Bot connected and running!")
        # clientMessageID is used to filter out old messages
        clientMessageID = []

        while client.server.connected is True:
            for data in client.rtm_read():
                if "type" in data and data["type"] == "message" and data.get('client_msg_id') not in clientMessageID:
                    echo(data)
                    clientMessageID.append(data.get('client_msg_id'))
                    
    else:
        print("Connection Failed")