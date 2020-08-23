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

    def get_entitys(self, filterproperty):
        result = []
        for entity in self._entitys:
            if isinstance(filterproperty, Component):
                if self.get_component(entity.get_id(), filterproperty) != None:
                    result.append(entity.get_id())
            elif isinstance(filterproperty, str):
                if entity.has(filterproperty):
                    result.append(entity.get_id())
        return result

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
    
    def add_to_entity(self, entityid, parameter):
        """
        parameter has to be a newly created Componentobject or a Stringobject
        """
        # add Componentobject to the context
        if isinstance(parameter, Component):
            self._components.append(parameter.set_id(len(self._components)))
            parameter = parameter.get_id()
        # parameter is now the id of the above added componentobject OR a stringobject
        self._entitys[entityid].add(parameter)

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
    context = Context()
    eid = context.new_entity()
    context.add()