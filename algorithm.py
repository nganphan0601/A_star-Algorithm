import heapq
import requests

# API key
API_KEY = open('API_key.txt').read()

# Function to get the distance between two cities using Google Maps API
def get_distance(source, dest, API_KEY):
    # Ensure the base URL ends without a question mark, as we're adding parameters manually
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

    # Format the request URL with proper URL encoding of parameters
    params = {
        'origins': source,
        'destinations': dest,
        'key': API_KEY
    }

    # Send the request
    r = requests.get(url, params=params)
    distance = float(r.json()['rows'][0]['elements'][0]['distance']['text'].split()[0])
    return  distance 


# Coordinates of cities
coordinates = {
    'Vancouver' : '49.260857852878296, -123.11404086052406',
    'North Vancouver': '49.320833134904376, -123.07413300583751',
    'West Vancouver': '49.33110455291839, -123.15986561170857',
    'Burnaby': '49.24341327397481, -122.97309706390146',
    'Richmond': '49.16331422744502, -123.13784669379238',
    'Surrey': '49.1913171427961, -122.84938514981447',
    'New Westminster': '49.206899511976424, -122.91105825518349',
    'Delta': '49.0845855257811, -123.05798913161706',
    'Langley': '49.103881764690456, -122.65699985105141',
    'Abbotsford': '49.052039946415775, -122.32944845763357',
    'Chilliwack': '49.15784616439666, -121.951190407741',
    'Hope': '49.38905677493949, -121.43918948626084',
    'Mission': '49.158920287643106, -122.28362373230219',
}


def heuristics(city1, city2):
    h = get_distance(coordinates[city1], coordinates[city2], API_KEY) - 10
    return h 

def a_star(G, start, goal):
    # frontier is a priority queue stores the nodes to be explored in the 
    #form of a tuple (f, node) with f is the cost of the path from the start to the node + the heuristic value of the node
    frontier = []
    # Initialize the frontier with the start node
    heapq.heappush(frontier, (0 + heuristics(start, goal), start))
    # came_from is a dictionary that stores the parent of each node
    came_from = {}
    # cost_so_far is a dictionary that stores the cost of the path from the start to each node
    cost_so_far = {}
    # Initialize the parent of the start node to None
    came_from[start] = None
    # Initialize the cost of the start node to 0
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]
        if current == goal:
            break

        for n in G.neighbors(current):
            new_cost = cost_so_far[current] + G[current][n]['weight']
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                f = new_cost + heuristics(n, goal)
                heapq.heappush(frontier, (f, n))
                came_from[n] = current

    # Reconstruct the path from the start to the goal
    path = []
    total_cost = 0
    current = goal
    while current != start:
        path.append(current)
        total_cost += G[came_from[current]][current]['weight']
        current = came_from[current]
    path.append(start)
    path.reverse()

    # Return the path and the cost of the path

    return path, total_cost



