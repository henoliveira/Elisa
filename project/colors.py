import random

ROSEWATER = (0.863, 0.541, 0.471)
FLAMINGO = (0.867, 0.471, 0.471)  #
PINK = (0.918, 0.463, 0.796)
MAUVE = (0.533, 0.224, 0.937)
RED = (0.824, 0.059, 0.224)
MAROON = (0.902, 0.271, 0.325)
PEACH = (0.996, 0.392, 0.043)
YELLOW = (0.874, 0.557, 0.114)
GREEN = (0.251, 0.627, 0.169)
TEAL = (0.090, 0.573, 0.600)  #
SKY = (0.016, 0.647, 0.898)
SAPPHIRE = (0.125, 0.624, 0.710)  #
BLUE = (0.118, 0.400, 0.961)
LAVENDER = (0.447, 0.529, 0.992)  #

TEXT = (0.298, 0.310, 0.412)
SUBTEXT1 = (0.361, 0.373, 0.467)
SUBTEXT0 = (0.424, 0.435, 0.522)
OVERLAY2 = (0.486, 0.498, 0.576)
OVERLAY1 = (0.549, 0.561, 0.631)
OVERLAY0 = (0.612, 0.627, 0.690)
SURFACE2 = (0.675, 0.690, 0.745)
SURFACE1 = (0.737, 0.753, 0.800)
SURFACE0 = (0.800, 0.816, 0.855)
BASE = (0.937, 0.945, 0.961)
MANTLE = (0.902, 0.914, 0.937)
CRUST = (0.863, 0.878, 0.910)


def randomly() -> tuple[float, float, float]:
    return random.choice(
        [
            ROSEWATER,
            FLAMINGO,
            PINK,
            MAUVE,
            RED,
            MAROON,
            PEACH,
            YELLOW,
            GREEN,
            TEAL,
            SKY,
            SAPPHIRE,
            BLUE,
            LAVENDER,
        ]
    )
