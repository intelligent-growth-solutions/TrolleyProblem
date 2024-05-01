from scipy.optimize import minimize
from scipy.spatial.distance import euclidean
import math

# Mean Square Error
# locations: [ (lat1, long1), ... ]
# distances: [ distance1, ... ]
def mse(x, locations, distances):
    mse = 0.0
    for location, distance in zip(locations, distances):
        distance_calculated = euclidean(x, location)
        mse += math.pow(distance_calculated - distance, 2.0)
    return mse / len(distances)

# initial_location: (lat, long)
# locations: [ (lat1, long1), ... ]
# distances: [ distance1,     ... ] 
def position_from_distances(distances, locations):

    initial_location = (0, 0)  # Could use last known for faster covergence

    result = minimize(
        mse,                         # The error function
        initial_location,            # The initial guess
        args=(locations, distances), # Additional parameters for mse
        method='L-BFGS-B',           # The optimisation algorithm
        options={
            'ftol':1e-5,         # Tolerance
            'maxiter': 1e+7      # Maximum iterations
        })
    
    location = result.x

    return location


if __name__ == '__main__' :

    beacon1 = (0, 0)
    beacon2 = (5, 0)
    beacon3 = (0, 5)

    # Distances when at point (5, 5)
    dist1 = math.sqrt(2)*5.0
    dist2 = 5.0
    dist3 = 5.0

    position = position_from_distances([dist1, dist2, dist3],
                                       [beacon1, beacon2, beacon3],)

    print(f"Should be close to [5.0, 5.0]: {position = }")

    # Distances when at point (2.5, 2.5)
    dist1 = math.sqrt(2)*2.5
    dist2 = math.sqrt(2)*2.5
    dist3 = math.sqrt(2)*2.5

    position = position_from_distances([dist1, dist2, dist3],
                                       [beacon1, beacon2, beacon3],)

    print(f"Should be close to [2.5, 2.5]: {position = }")
