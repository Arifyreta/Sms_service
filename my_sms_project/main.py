from config import load_config
from http_client import send_request
from HTTP import HTTPRequest
import json
import base64
import logging
#Логирование в файл
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def main():
    print("Enter the sender of the recipient and the message\r\n")
    data=input()
    try:
        data_split=data.split(' ',2)
        if len(data_split) != 3:
            raise ValueError("Invalid input format. Expected: sender recipient message")
        sender, recipient, message = data_split
        if not sender or not recipient or not message:
            logging.error("One of the fields is empty")
        else:
            logging.info(f"Sender: {sender}, Recipient: {recipient}, Message: {message}")
    except ValueError:
        logging.error("An empty line has been entered")
    
    
    config = load_config()
    sms_service = config["SMS_SERVICE"]

    request = HTTPRequest(
        method="POST",
        url="/send_sms",
        headers={
            "Host": "localhost:4010","Authorization": f"Basic {base64.b64encode(f'{sms_service['username']}:{sms_service['password']}'.encode()).decode()}","Content-Type": "application/json"
        },
        body=json.dumps({
            "sender": data_split[0],
            "recipient": data_split[1],
            "message": data_split[2]
        })
        
    )

    response = send_request(request)
    headers= "\r\n".join(f"{k}: {v}" for k, v in request.headers.items())
    logging.info(f"HTTP-Request:\r\n{request.method} {request.url} HTTP/1.1\r\n{headers}\r\n\r\n{request.body}")
    logging.info(f"HTTP-Response:\r\n{response.status_code}\r\n{response.body}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.body}")
main()