from random import random as rnd
from SnakeAI.CONSTANTS import *
from SnakeAI.Objects.Object import *


class Memory:

    def __init__(self):
        self.objects = [Object]
        self.object_names = {}
        self.past = []
        self.present = []
        self.future = []
        self.past_time = {}
        self.present_time = {}
        self.future_time = {}
        self.CONSTANTS = Constants()
        self.create_links()

    def set_from_screen(self, screen):
        buf = screen.getPastObjects(self.object_names)
        if len(buf) > 0:
            for item in buf:
                if item not in self.past:
                    self.set_to_past(item)
        buf = screen.getPresentObjects(self.object_names)
        if len(buf) > 0:
            for item in buf:
                if item not in self.present:
                    self.set_to_present(item)
        buf = screen.getFutureObjects(self.object_names)
        if len(buf) > 0:
            for item in buf:
                if item not in self.future:
                    self.set_to_future(item)

    def get_dependents(self):
        """для каждого осознаваемого объекта"""
        for present_object in self.present:
            """просматриваются все образы, на которые он ссылается"""
            for link in range(self.objects[present_object].len):
                """если связь достаточно сильна"""
                if rnd() < self.objects[present_object].weights[link]:
                    """и такого объекта еще нет в текущем осознании"""
                    if self.objects[present_object].links[link] not in self.present:
                        """добавляется"""
                        self.present.append(self.objects[present_object].links[link])

    """обновляет временные расстояния события в осознании"""

    def time_shift(self):
        """удаляет слишком давние события совсем"""
        if len(self.past) > 0:
            for obj in self.past:
                if obj is not None:
                    if self.past_time[obj] > self.CONSTANTS.max_time_in_past:
                        self.remove_from_past(obj)
        """переносит длительные текущие события в случившееся прошлое"""
        if len(self.present) > 0:
            for obj in self.present:
                if self.present_time[obj] > self.CONSTANTS.max_time_in_present:
                    self.move_from_present(obj)
        """удаляет нереализованные фантазии"""
        if len(self.future) > 0:
            for obj in self.future:
                if self.future_time[obj] > self.CONSTANTS.max_time_in_future:
                    self.remove_from_future(obj)

    def get_action(self):
        return -1

    def set_to_past(self, id: int):
        self.past.append(id)
        self.past_time[id] = 0

    def set_to_present(self, id: int):
        self.present.append(id)
        self.present_time[id] = 0

    def set_to_future(self, id: int):
        self.future.append(id)
        self.future_time[id] = 0

    def remove_from_past(self, id: int):
        del self.past_time[id]
        self.past.pop(id)

    def move_from_present(self, id: int):
        del self.present_time[id]
        self.present.pop(id)
        self.set_to_present(id)

    def remove_from_future(self, id: int):
        del self.future_time[id]
        self.future.pop(id)
    
    def create_links(self):
        """ACTIONS"""
        self.object_names["Remain stationary"] = 0
        self.object_names["Move left"] = 1
        self.object_names["Move right"] = 2

        """ITEMS"""
        self.object_names["Apple"] = 3
        self.object_names["Poisoned apple"] = 4

        """ITEM PROPERTIES = NOTIONS"""
        self.object_names["Is far away"] = 5
        self.object_names["Is close"] = 6
        self.object_names["Is lefter"] = 7
        self.object_names["Is righter"] = 8
        """FEELINGS"""
        self.object_names["Want to eat"] = 9
        self.object_names["Death"] = 10

        self.objects.append(ActionObject(self.object_names, "Remain stationary"))
        self.objects.append(ActionObject(self.object_names, "Move left"))
        self.objects.append(ActionObject(self.object_names, "Move right"))
        self.objects.append(NotionObject(self.object_names, "Death"))
        self.objects.append(NotionObject(self.object_names, "Is far away"))
        self.objects.append(NotionObject(self.object_names, "Is close"))
        self.objects.append(NotionObject(self.object_names, "Is lefter"))
        self.objects.append(NotionObject(self.object_names, "Is righter"))
        self.objects.append(ItemObject(self.object_names, "Apple")
                           .add_link("Is lefter", 0.25, self.object_names).add_link("Is righter", 0.25, self.object_names)
                           .add_link("Is far away", 0.25, self.object_names).add_link("Is close", 0.25, self.object_names))
        self.objects.append(ItemObject(self.object_names, "Poisoned apple")
                           .add_link("Is lefter", 0.25, self.object_names).add_link("Is righter", 0.25, self.object_names)
                           .add_link("Is far away", 0.25, self.object_names).add_link("Is close", 0.25, self.object_names)
                           .add_link("Death", 1, self.object_names))
        self.objects.append(NotionObject(self.object_names, "Want to eat")
                           .add_link("Apple", 1, self.object_names))
