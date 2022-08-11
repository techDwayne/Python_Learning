EXPECTED_BAKE_TIME=40
PREPARATION_TIME=5
TIME_PER_LAYER=2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(layer):
    """Calculate the total preparation time.
 
    :param layer: int number of layers.
    :return: int total time of preparation for all layers.
 
    Function that takes a number of lasagna layers, and returns how many minutes
    it needs to be prepared, based on the `TIME_PER_LAYER`.
    """
    return layer * TIME_PER_LAYER
def elapsed_time_in_minutes(layer, baking_time):
    """Calculate the full time needed (preparation + baking) in minutes.
 
    :param layer: int number of layers.
    :param baking_time: total baking time needed in minutes.
    :return: int total time in minutes to prepare and bake the marvellous lasagna.
 
    Function that takes the preparation and baking times, and return the total in
    minutes.
    """
    preparation_time = preparation_time_in_minutes(layer)
    return preparation_time + baking_time