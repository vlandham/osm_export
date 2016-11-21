
import os
import osmnx as ox
ox.config(log_console=True, use_cache=True)

places = [
    {'name': "seattle", 'loc': "Seattle, Washington, USA"},
    {'name': "modena", 'loc': "Modena, Italy"}
]

for place in places:
    place_path = os.path.join(os.path.dirname(__file__), 'images', place['name'] + '.svg' )
    print(place_path)
    if not os.path.exists(place_path):
        G = ox.graph_from_place(place['loc'], network_type='drive', simplify=True)
        G_projected = ox.project_graph(G)
        ox.plot_graph(G_projected, fig_height=20, node_size=0, edge_linewidth=0.5, show=False, save=True, filename=place['name'], file_format='svg')
    else:
        print('skipping ' + place['name'])
