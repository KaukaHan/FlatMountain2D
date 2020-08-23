#! /usr/bin/python3

import socket
import threading
import time

class Server:
    def __init__(self):
        self._drawDataCache = []
        self._keyCache = []
        self._alive = True
        self._host = "localhost"
        self._port = 60003
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._host, self._port))
        self._socket.listen(1)
        self._client, self._clientadress = self._socket.accept()
        self._thread = threading.Thread(target=self.run)
        self._thread.start()

    def send(self, msg, delimiter=";"):
        msg = "{}{}".format(msg, delimiter).encode()
        try:
            self._client.sendall(msg)
        except BrokenPipeError:
            print("Error while sending: Connection broken")
            print("Closing Server")
            self.close()
        except ConnectionResetError:
            print("Error: connection resetted error")
            self.close()

    def recive(self) -> str:
        result = ""
        try:
            result += self._client.recv(1024).decode("UTF-8")
        except BrokenPipeError:
            print("Error while reciving: Connection broken")
            print("Closing Server")
            self.close()
        except ConnectionResetError:
            print("Error: connection resetted error")
            self.close()
        if len(result) > 0:
            result = result[:-1]            
        return result

    def draw_rectangle(self, pos, size, color):
        drawdata = ""
        for tup in (pos, size, color):
            for value in tup:
                drawdata += "{}{}".format(str(value), ",")
        drawdata = drawdata[:-1]
        self._drawDataCache.append(drawdata)

    def get_keys(self):
        keys = self._keyCache[:]
        self._keyCache = []
        return keys

    def run(self):
        while self._alive:
            if self._drawDataCache:
                self.send("draw")
                self.recive()
                self.send(self._drawDataCache.pop(0))
                self.recive()
            if not self._keyCache:
                self.send("getkeys")
                keystring = self.recive()
                keylist = keystring.split(sep=",")
                for key in keylist:
                    if key:
                        self._keyCache.append(key)
            time.sleep(0.1)

    def close(self):
        self._alive = False
        self._thread.join()
        self._socket.close()
        self._client.shutdown(0)
        self._client.close() 


if __name__ == "__main__":
    server = Server()
    server.draw_rectangle((30, 40), (200, 50), (0, 200, 20))
    while server._alive:
        print(server.get_keys())
        time.sleep(1)
    server.close()
