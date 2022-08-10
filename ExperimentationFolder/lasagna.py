"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
layers = int(input("Total layers?"))
minutes_per_layer = 2
baking_time = int(input("Enter the time in minutes baking: "))


def bake_time_remaining(EXPECTED_BAKE_TIME, baking_time):
    return EXPECTED_BAKE_TIME - baking_time
    
print("Remaining Time: ", bake_time_remaining(EXPECTED_BAKE_TIME, baking_time))

def preparation_time_in_minutes(layers, minutes_per_layer):
    return layers * minutes_per_layer

print("Total Prep time: ", preparation_time_in_minutes(layers, minutes_per_layer))


def elapsed_bake_time(baking_time, bake_time_remaining):
    return  bake_time_remaining - baking_time

print("Total Elapsed Baking Time: ", elapsed_bake_time(baking_time,  bake_time_remaining(EXPECTED_BAKE_TIME, baking_time)))
#pass


def elapsed_time_in_minutes(baking_time, preparation_time_in_minutes):
    return baking_time + preparation_time_in_minutes

print("Total Elapsed Time", elapsed_time_in_minutes(baking_time, preparation_time_in_minutes(layers, minutes_per_layer)))