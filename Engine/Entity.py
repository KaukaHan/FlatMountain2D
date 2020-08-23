#! /usr/bin/python3

class Entity:
    def __init__(self, id):
        self._id = id
        self._tags = []
        self._componentids =[]

    def add(self, parameter):
        if isinstance(parameter, str):
            self._tags.append(parameter)
        elif isinstance(parameter, int):
            self._componentids.append(parameter)
        else:
            print("Warning: parametertype not supported '{}'".format(type(parameter)))
    
    def has(self, parameter):
        if isinstance(parameter, str):
            for tag in self._tags:
                if tag == parameter:
                    return True

        elif isinstance(parameter, int):
            for componentid in self._componentids:
                if componentid == parameter:
                    return True
        else:
            print("Warning: parametertype not supported '{}'".format(type(parameter)))
        return False

    def remove(self, parameter):
        if isinstance(parameter, str):
            if self.has(parameter):
                self._tags.remove(parameter)
        elif isinstance(parameter, int):
            if self.has(parameter):
                self._componentids.remove(parameter)
        else:
            print("Warning: parametertype not supported '{}'".format(type(parameter)))