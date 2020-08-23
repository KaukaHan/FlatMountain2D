#! /usr/bin/python3

from Context import Context

class Service:
    def __init__(self, id, context):
        self._id = id
        self._context = context