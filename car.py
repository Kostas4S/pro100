class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        
    def start(self):
        print('started')
        
    def stop(self):
        print('stopped')

    def accelerate(self):
        print('Accelerating')
        
    def change_gear(self, gear_type):
        print('Gear Changed')

toyota = Car("Highlander","Red","Toyota",120)


print(toyota.start())
print(toyota.accelerate())
    