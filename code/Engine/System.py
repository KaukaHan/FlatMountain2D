#! /usr/bin/python3

from Context import Context
from Service import Service

class System:
    def __init__(self, newid, context, filterproperty):
        self._id = newid
        self._context = context
        self._filterproperty = filterproperty

    def process(self, entityid):
        raise NotImplementedError

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def update(self):
        for entityid in self._context.get_entitys(self._filterproperty):
            self.process(entityid)

if __name__ == "__main__":
    pass