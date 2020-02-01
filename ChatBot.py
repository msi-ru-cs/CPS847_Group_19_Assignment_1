import os
from slackclient import SlackClient

SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN')
client = SlackClient(SLACK_API_TOKEN)

def echo(data):
    # echo text
    if ('text' in data):
        if (data['text'][-1] == "?"):
            client.api_call('chat.postMessage',
                channel=data['channel'],
                text= data.get('text')[13:],
                thread_ts=data['ts']
            )

if __name__ == "__main__":
    if client.rtm_connect():
        print("Bot connected and running!")

        while client.server.connected is True:
            for data in client.rtm_read():
                if "type" in data and data["type"] == "message": 
                    echo(data)

                    
    else:
        print("Connection Failed")