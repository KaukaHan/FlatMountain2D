#! /usr/bin/python3

from Entity import Entity
from Component import Component

class Context:
    def __init__(self):
        self._entitys = []
        self._components = []
        self._data = {}

    def new_entity(self) -> int:
        newid = len(self._entitys)
        newentity = Entity(newid)
        return newid

    def get_entity(self, searchproperty) -> int:
        if isinstance(searchproperty, str) or isinstance(searchproperty, int):
            for entity in self._entitys:
                if entity.has(searchproperty):
                    return entity.get_id()
        elif isinstance(searchproperty, Component):
            for component in self._components:
                if isinstance(component, searchproperty):
                    entityid = self.get_entity(component.get_id())
                    if entityid != None:
                        return entityid
        return None
    
    def get_component(self, entityid, componenttype):
        for component in self._components:
            if isinstance(component, componenttype) and self._entitys[entityid].has(component.get_id()):
                return component
        return None

    def set_data(self, key, value):
        self._data["key"] = value

    def get_data(self, key):
        return self._data.get(key)


if __name__ == "__main__":
    pass