
def calculate_speed(distance, time):
    return distance / time


def calculate_force(mass, acceleration):
    return mass * acceleration



def calculate_weight(mass, gravity=9.8):
    return mass * gravity



def calculate_density(mass, volume):
    return mass / volume


def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


print("PHYSICS FORMULAS")

print("Speed:", calculate_speed(100, 20), "m/s")
print("Force:", calculate_force(10, 5), "N")
print("Weight:", calculate_weight(20), "N")
print("Density:", calculate_density(50, 10), "kg/m³")
print("Kinetic Energy:", calculate_kinetic_energy(10, 4), "J")
