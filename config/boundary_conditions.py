"""
This is dictionary  containing information about boundary
conditions in the case solved. For further readings involving
proper setup refer to the README.md file. Number of entries to
the BC file should be equal to the number of boundary zones.
"""
BC = {
    "top": {"type": 'moving_wall', "velocity": [2, 0]},  # list [u, v]
    "bottom": {"type": 'stationary_wall'},
    "left": {"type": 'stationary_wall'},
    "right": {"type": 'stationary_wall'},
}