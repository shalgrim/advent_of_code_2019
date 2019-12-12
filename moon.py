class Moon(object):
    def __init__(self, x, y, z, start_velocity=None):
        self.position = [x, y, z]
        self.velocity = start_velocity if start_velocity else [0, 0, 0]

    def apply_gravity(self, other):
        for i in range(3):
            self._apply_gravity_position(other, i)

    def _apply_gravity_position(self, other, i):
        if self.position[i] < other.position[i]:
            self.velocity[i] += 1
        elif self.position[i] > other.position[i]:
            self.velocity[i] -= 1

    def apply_velocity(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    @property
    def potential_energy(self):
        return sum([abs(p) for p in self.position])

    @property
    def kinetic_energy(self):
        return sum([abs(v) for v in self.velocity])

    @property
    def energy(self):
        return self.potential_energy * self.kinetic_energy

    def __eq__(self, other):
        return self.velocity == other.velocity and self.position == other.position
        # return self.velocity == other.velocity  # and self.position == other.position

    def __repr__(self):
        return (
            f'pos=<x={self.position[0]}, y={self.position[1]}, z={self.position[2]}>, '
            f'vel=<x={self.velocity[0]}, y={self.velocity[1]}, z={self.velocity[2]}>'
        )
