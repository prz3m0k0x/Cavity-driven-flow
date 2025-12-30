"""
This is dictionary  containing information about boundary
conditions in the case solved. For further readings involving
proper setup refer to the README.md file. Number of entries to
the BC file should be equal to the number of boundary zones.
"""
BC = {
    "top" : {
        'type' : 'moving wall',
        'velocity' : (1, 0)
    },

    'left' : {
        'type' : 'stationary wall'
    },

    'right' : {
        'type' : 'stationary wall'
    },

    'bottom' : {
        'type' : 'stationary wall'
    },
}