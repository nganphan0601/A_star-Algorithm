
from graph import create_graph, draw_graph
from algorithm import heuristics, a_star


# graph
Lower_Mainland = create_graph()

# take user input
start = str(input('Enter the start city: '))
goal = str(input('Enter the goal city: '))

print(a_star(Lower_Mainland, start, goal))
draw_graph(Lower_Mainland)