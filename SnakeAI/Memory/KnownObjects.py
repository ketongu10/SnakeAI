from SnakeAI.Objects.Object import *
from Memory import *


def init_MEM():
    MEM = Memory()
    
    """ACTIONS"""
    MEM.object_names["Remain stationary"] = 0
    MEM.object_names["Move left"] = 1
    MEM.object_names["Move right"] = 2
    
    """ITEMS"""
    MEM.object_names["Apple"] = 3
    MEM.object_names["Poisoned apple"] = 4
    
    """ITEM PROPERTIES = NOTIONS"""
    MEM.object_names["Is far away"] = 5
    MEM.object_names["Is close"] = 6
    MEM.object_names["Is lefter"] = 7
    MEM.object_names["Is righter"] = 8
    """FEELINGS"""
    MEM.object_names["Want to eat"] = 9
    MEM.object_names["Death"] = 10
    
    MEM.objects.append(ActionObject(MEM.object_names["Remain stationary"]))
    MEM.objects.append(ActionObject(MEM.object_names["Move left"]))
    MEM.objects.append(ActionObject(MEM.object_names["Move right"]))
    MEM.objects.append(NotionObject(MEM.object_names["Death"]))
    MEM.objects.append(NotionObject(MEM.object_names["Is far away"]))
    MEM.objects.append(NotionObject(MEM.object_names["Is close"]))
    MEM.objects.append(NotionObject(MEM.object_names["Is lefter"]))
    MEM.objects.append(NotionObject(MEM.object_names["Is righter"]))
    MEM.objects.append(ItemObject(MEM.object_names["Apple"])
                          .add_link("Is lefter", 0.25).add_link("Is righter", 0.25)
                          .add_link("Is far away", 0.25).add_link("Is close", 0.25))
    MEM.objects.append(ItemObject(MEM.object_names["Poisoned apple"])
                          .add_link("Is lefter", 0.25).add_link("Is righter", 0.25)
                          .add_link("Is far away", 0.25).add_link("Is close", 0.25)
                          .add_link("Death", 1))
    MEM.objects.append(NotionObject(MEM.object_names["Want to eat"])
                          .add_link("Apple", 1))
    return MEM




