class person:
    name='shahin'
    def __init__(self,name,family,age):
        self.name=name
        self.family=family
        self.age=age
    def showeinfo(self):
        return f'{self.name}-{self.family}-{self.age}--{person.name}'
p1=person('ali','ahmadi',19)