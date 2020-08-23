#! /usr/bin/python3

class Component:
    def __init__(self):
        self._id = None

    def get_id(self) -> int:
        return self._id

    def set_id(self, newid):
        self._id = newid