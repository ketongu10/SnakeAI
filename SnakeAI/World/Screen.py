


class Screen:
    
    def __init__(self):
        self.apple_pos = -1
        self.poisoned_apple_pos = -1
        self.snake_pos = 0
        
    def getPastObjects(self, memory):
        return []
    
    def getPresentObjects(self, Dict):
        buf = []
        if self.apple_pos != -1:
            buf.append(Dict["Apple"])
            if self.apple_pos < self.snake_pos:
                buf.append(Dict["Is lefter"])
            else:
                buf.append(Dict["Is righter"])
                
        if self.poisoned_apple_pos != -1:
            buf.append(Dict["Poisoned apple"])
            if self.apple_pos < self.snake_pos:
                buf.append(Dict["Is lefter"])
            else:
                buf.append(Dict["Is righter"])
        return buf
    
    def getFutureObjects(self, Dict):
        buf = []
        if self.poisoned_apple_pos != -1:
            buf.append(Dict["Death"])
            return buf
        return buf

    def setScreeenFromWorld(self, world):
        self.apple_pos = world.apple_pos
        self.poisoned_apple_pos = world.poisoned_apple_pos
        self.snake_pos = world.snake_pos


