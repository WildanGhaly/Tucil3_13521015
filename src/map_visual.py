# file: map_visual.py

import folium
import graph as g

def color(name, solution):
    # kalau starting point
    if name == solution[0][0]:
        color = 'green'
    else:
        # kalau di path
        if name in solution[0]:
            color = 'red'
        else:
            color = 'blue'
    return color

def visual_map(list_path, path_solution, isUCS):

    map = folium.Map(location=[g.avg_lat(g.list_lat),g.avg_lon(g.list_lon)],zoom_start=15)

    # make markers
    for point in range(0, len(g.list_of_coordinates)):
        folium.Marker(g.list_of_coordinates[point], popup=g.list_of_names[point], icon=folium.Icon(color=color(g.list_of_names[point], path_solution))).add_to(map)

    # make path
    fg = folium.FeatureGroup("Path")
    line = folium.vector_layers.PolyLine(list_path, color='red', weight=10).add_to(fg)
    fg.add_to(map)

    # add lintasan terpendek
    solution = g.string_route(path_solution)
    solution_html = '''
                <h3 align="center" style="font-size:20px"><b>{}</b>
                </h3>
                '''.format(solution)
    map.get_root().html.add_child(folium.Element(solution_html))

    if isUCS:
        panjang_lintasan = "Panjang lintasan UCS : "    
    else:
        panjang_lintasan = "Panjang lintasan A* : "
    panjang_lintasan += str(path_solution[1]) + " meter."

    panjang_lintasan_html = '''
                    <h3 align="center" style="font-size:20px"><b>{}</b>
                    </h3>
                    '''.format(panjang_lintasan)
    map.get_root().html.add_child(folium.Element(panjang_lintasan_html))
                
    map.add_child(folium.LayerControl())
    map.save(outfile='map.html')