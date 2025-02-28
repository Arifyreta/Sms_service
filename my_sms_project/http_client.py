import socket
from HTTP import HTTPRequest, HTTPResponse
#Реализация передачи HTTP-запроса и получения HTTP-ответа
def send_request(request: HTTPRequest) -> HTTPResponse:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 4010))
        s.sendall(request.to_bytes())
        data = s.recv(4096)
        return HTTPResponse.from_bytes(data)

