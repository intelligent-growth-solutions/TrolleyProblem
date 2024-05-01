import numpy as np
from scipy_opt_trilateration import position_from_distances

def distance_from_RSSI(rssi):
    A = -40
    n = 1.62
    exponent = (A - rssi)/(10*n)
    distance = np.power(10, exponent)
    return distance


def position_from_RSSIs(rssi_0012, rssi_0000, rssi_7512):

    d1 = distance_from_RSSI(rssi_0012)
    d2 = distance_from_RSSI(rssi_0000)
    d3 = distance_from_RSSI(rssi_7512)

    # Beacon positions:
    p1 = (0, 0)  # AP = 0012
    p2 = (12, 0)  # AP = 0000
    p3 = (0, 7.5)  # AP = 7512

    x, y = position_from_distances([d1, d2, d3],
                                   [p1, p2, p3])

    return x, y


# if __name__ == '__main__' :
#
#     # Expect this to be close to rssi_7512 = (0, 7.5)
#     estimated_posn = position_from_RSSIs(-54, -58.5, -20)
#     print(f"Should be close to [0, 7.5]: {estimated_posn = }")
#
#     estimated_posn = position_from_RSSIs(-57.5, -20, -58.5)
#     print(f"Should be close to [12, 0.0]: {estimated_posn = }")
