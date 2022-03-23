from slack_sdk import WebClient
from datetime import datetime

class SlackAlert:
    def __init__(self, channel, token):
        self.channel = channel
        self.client = WebClient(token=token)

    def success_msg(self, msg):
        text = f"""
            date : {datetime.today().strftime('%Y-%m-%d')}
            alert : 
                Success! 
                    task id : {msg.get('task_instance').task_id}, 
                    dag id : {msg.get('task_instance').dag_id}, 
                    log url : {msg.get('task_instance').log_url}
            """
        self.client.chat_postMessage(channel=self.channel, text=text)

    def fail_msg(self, msg):
        text = f"""
            date : {datetime.today().strftime('%Y-%m-%d')}  
            alert : 
                Fail! 
                    task id : {msg.get('task_instance').task_id}, 
                    dag id : {msg.get('task_instance').dag_id}, 
                    log url : {msg.get('task_instance').log_url}
        """
        self.client.chat_postMessage(channel=self.channel, text=text)
