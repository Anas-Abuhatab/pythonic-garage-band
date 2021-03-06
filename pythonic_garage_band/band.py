

class Band :

    instances = []
    
    def __init__(self,name,members=None):
        self.name =name
        self.members = members
        Band.instances.append(self)

    def __str__(self) :
        return f"The band {self.name}"
    
    def __repr__(self):
        print(self.name)
        return f'{self.name}'

    def play_solos(self):
        return list(map(lambda member : member.play_solo(),self.members))
    
    @classmethod
    def to_list(cls):
        return cls.instances


class Musician:
    def __init__(self, name):
        self.name =name


class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"

