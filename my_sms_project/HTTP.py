from typing import Self
#Создаём класс представляющий HTTP-запрос
class HTTPRequest:
    def __init__(self, method, url, headers: dict, body):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def to_bytes(self) -> bytes:
        headers = "\r\n".join(f"{k}: {v}" for k, v in self.headers.items())
        return f"{self.method} {self.url} HTTP/1.1\r\n{headers}\r\n\r\n{self.body}".encode()

#Создаём класс представляющий HTTP-ответ  
class HTTPResponse:
    def __init__(self, status_code, headers, body):
        self.status_code = status_code
        self.headers = headers
        self.body = body

    @classmethod
    def from_bytes(cls,binary_data: bytes) -> Self:
        # Реализация преобразования байт в объект HTTPResponse
        headers_part, body = binary_data.split(b"\r\n\r\n", 1)
        
        headers = headers_part.decode().split("\r\n")
        status_line = headers[0]
        status_code = status_line.split(" ", 2)
        
        header_dict = {}
        for line in headers[1:]:
            if line:
                key, value = line.split(": ", 1)
                header_dict[key] = value
        body=body.decode()
        return cls(status_code,header_dict,body)
