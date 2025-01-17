import numpy as np
import rebound
from Planet_old import Planet_old


class Planet:
    """
    represents a planet that affects other with its gravity and is affected by the gravity of others
    """
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.pos = position
        self.vel = velocity
        self.acc = np.array([0,0])

    def get_particle(self):
        return rebound.Particle(m=self.mass, x=self.pos[0], y=self.pos[1], vx=self.vel[0], vy=self.vel[1])

    def get_vector(self, type):
        match type:
            case "m_pos_vel":
                return np.concatenate([self.mass], self.pos, self.vel)
            case "m_pos_vel_acc":
                return np.concatenate([self.mass],self.pos, self.vel, self.acc)

    def __repr__(self):
        return f"|Planet with mass={self.mass}, pos={self.pos}, vel={self.vel}|"

    def __str__(self):
        return f"|Planet with mass={self.mass}, pos={self.pos}, vel={self.vel}|"

    def copy(self):
        new_planet = Planet(self.mass, self.pos.copy(), self.vel.copy())
        new_planet.acc = self.acc.copy()
        return new_planet
    
    def load_particle(particle):
        pos = np.array([particle.x, particle.y])
        vel = np.array([particle.vx, particle.vy])
        mass = particle.m
        return Planet(mass, pos, vel)
    
    def get_planet_old(self):
        return Planet_old(self.mass, self.pos.copy(), self.vel.copy())
    
    def load_planet_old(planet_old):
        return Planet(planet_old.mass, planet_old.pos.copy(), planet_old.vel.copy())
    
    def get_random():
        pos = 4 * np.random.rand(2)
        vel = 4 * np.random.rand(2)
        mass = 4 * np.random.random()
        return Planet(mass, pos, vel)

