# Student: Valentina Hernandez Vera
# EXCEEDING REQUIREMENTS: Added another user defined function, called kpa_to_psi, to convert the pressure in KPA to PSI and display it. There is also test_kpa_to_psi which can be found in test_water_flow.py.
import pytest
p = 998.2  # density of water in kg/m3
mu = 0.0010016

def pressure_loss_from_fittings (fluid_velocity, quantity_fittings):
    lost_pres_kilopascals = (-0.04 * p * (fluid_velocity ** 2) * quantity_fittings) / 2000
    if lost_pres_kilopascals == 0:
        lost_pres_kilopascals = 0.0
    return round(lost_pres_kilopascals, 3)

def reynolds_number(hydraulic_diameter, fluid_velocity):
    r_n = (p * hydraulic_diameter  * fluid_velocity)/mu
    return round(r_n)

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = (0.1 + (50/reynolds_number))*((larger_diameter/smaller_diameter)**4 - 1)
    P = (-k * p * fluid_velocity**2)/2000
    return round(P, 3)

def water_column_height(tower_height, tank_height):
    tower_height = tower_height + 0.5 * tank_height
    return tower_height

def pressure_gain_from_water_height(water_height):
    g = 9.81 # acceleration due to gravity in m/s2
    convert_to_kilopascals = (p * g * water_height) / 1000
    return round(convert_to_kilopascals, 2)

def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    pressure_loss = -friction_factor * (length / diameter) * (p * velocity ** 2) / (2 * diameter * 1000)
    return round(pressure_loss, 2)

def kpa_to_psi(pressure):
    psi = pressure / 6.89476
    return psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY

    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY

    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    new_pressure = kpa_to_psi(pressure)
    print(f"The pressure, converted to per square inch, is the following: {new_pressure:.2f}.")
if __name__ == "__main__":
    main()