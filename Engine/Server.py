#! /usr/bin/python3

import socket
import threading

class Server:
    def __init__(self):
        self._alive = True
        self._host = "localhost"
        self._port = "70000"
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._host, self._port))
        self._socket.listen(1)
        self._client, self._clientadress = self._socket.accept()
        self._thread = threading.Thread(self.run)
        self._thread.start()

    def send(self, msg, delimiter=";"):
        msg = "{}{}".format(msg, delimiter).encode()
        try:
            self._client.sendall(msg)
        except BrokenPipeError:
            print("Error while sending: Connection broken")
            print("Closing Server")
            self.close()

    def recive(self) -> str:
        result = ""
        try:
            result += self._client.recv(1024).decode("UTF-8")
        except BrokenPipeError:
            print("Error while reciving: Connection broken")
            print("Closing Server")
            self.close()
        if len(result) > 0:
            result = result[:-1]            
        return result

    def run(self):
        while self._alive:
            self.send("draw")
            self.recive()
            self.send("10,10,50,100,75,0,200")
            self.recive()

    def close(self):
        self._alive = False
        self._thread.join()
        self._socket.close()
        self._client.close()


if __name__ == "__main__":
    import time
    server = Server()
    time.sleep(5)
    server.close()
