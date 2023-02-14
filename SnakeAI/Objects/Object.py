


class Object:
    def __init__(self, ob_id: int):
        self.links = [int]
        self.weights = [float]
        self.len = 0
        self.id = ob_id

    def __init__(self, ob_id: int, name: str):
        self.links = [int]
        self.weights = [float]
        self.len = 0
        self.id = ob_id
        self.name = name

    def __init__(self, Dict, name: str):
        self.links = [int]
        self.weights = [float]
        self.len = 0
        self.id = Dict[name]
        self.name = name

    def add_link(self, new_id: int, weight: float):
        self.links.append(new_id)
        self.weights.append(weight)
        self.len += 1

    def add_link(self, obj_name: str, weight: float, Dict):
        self.links.append(Dict[obj_name])
        self.weights.append(weight)
        self.len += 1
        return self

    def is_action(self):
        return False

    def is_item(self):
        return False

    def is_notion(self):
        return False

    def has_name(self):
        return self.name is not None


class ActionObject(Object):
    def is_action(self):
        return True


class ItemObject(Object):
    def is_item(self):
        return True


class NotionObject(Object):
    def is_notion(self):
        return True


