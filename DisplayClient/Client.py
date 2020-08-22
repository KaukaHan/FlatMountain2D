#! /usr/bin/python3

from Display import Display

import socket

class Client:
    def __init__(self):
        self._alive = True
        self._port = 7000
        self._host = "localhost"
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._host, self._port))
        self._display = Display()

    def send(self, msg, delimiter=";"):
        msg = "{}{}".format(msg, delimiter).encode()
        try:
            self._socket.sendall(msg)
        except BrokenPipeError:
            print("Error while sending: Connection broken")
            print("Closing client")
            self.close()

    def recive(self) -> str:
        result = ""
        try:
            result += self._socket.recv(1024).decode("UTF-8")
        except BrokenPipeError:
            print("Error while reciving: Connection broken")
            print("Closing client")
            self.close()
        if len(result) > 0:
            result = result[:-1]            
        return result

    def close(self):
        self._alive = False
        self._display.close()
        self._socket.close()

    def draw_rawdata(self, srawdata:str):
        datalist = srawdata.split(sep=",")
        if len(datalist) < 7:
            print("Error while parsing drawdata: {}".format(srawdata))
            return
        pos = tuple(datalist[0:1])
        size = tuple(datalist[2:3])
        color = tuple(datalist[4:6])
        self._display.draw_rectangle(pos, size, color)

    def run_loop(self):
        while self._alive:
            command = self.recive()
            if command == "draw":
                self.send("ok")
                rawdata = self.recive()
                self.send("ok")
                self.draw_rawdata(rawdata)
            else:
                print("Unknown command from server: {}".format(command))
                self.send("err")


if __name__ == "__main__":
    client = Client()
    client.run_loop()