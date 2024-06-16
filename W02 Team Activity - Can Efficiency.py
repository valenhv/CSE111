# Student: Valentina Hernandez Vera
# Work in progress

import math

def compute_volume(radius, height):
    volume = round(math.pi * radius ** 2 * height, 2)
    print(volume)
    return volume

def compute_surface_area(radius, height):
    surface_area = round(2 * math.pi * radius * (radius + height), 2)
    print(surface_area)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = round(volume / surface_area, 2)
    print(storage_efficiency)
    return storage_efficiency

result_vol = compute_volume(6.83, 10.16)
result_sur = compute_surface_area(6.83, 10.16)
result_sto = compute_storage_efficiency(result_vol, result_sur)