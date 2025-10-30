import math
class Planet:
    def __init___(self, _name, _radius, _mass, _distance):
        self.name = _name
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance

    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_distance(self):
        return self.distance
    def get_density(self):
        return self.distance
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume
    def get_density(self):
        density = self.mass / self.get_volume()
        return density
    
    def set_name(self, new_name):
        name = new_name

class Star:
    def __init__(self, _name):
        self.name = _name
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def __str__(self):
        msg = ''
        msg += f'I am {self.name}, King of your planetary system!'

class PlanetarySystem:
    def __init__(self, _star):
        self.star = +_star
        self.planets = []

    def add_planet(self, _planet):
        self.planets.append(_planet)

    def show_planets(self):
        '''iterate throufh each planet and print the name'''
        for planet in self.planets:
            print(planet.get_name())