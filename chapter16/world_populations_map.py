import json
from country_codes import get_country_code
import pygal_maps_world.maps

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

wm = pygal_maps_world.maps.World()
wm.title = 'Populations of World in 2010, by Country'
wm.add('World 2010', cc_population)

wm.render_to_file('world_populations.svg')
