with open('input.txt') as file:
  data = file.read().strip()

def parse_seeds(data):
  seeds = []
  for line in data.split("\n"):
    if line.startswith("seeds:"):
        seeds += list(map(int, line.split()[1:]))  # Skip "seeds:" and convert the rest to integers
    elif seeds and not line.strip():  # Check if we've reached the end of the "seeds:" section
        continue
  return seeds

def parse_maps(data):
  maps = {}
  current_map = None

  for line in data.split("\n"):
    if line.startswith("seeds:"):
      continue
    elif line.startswith("seed-to-soil map:"):
        current_map = "seed_to_soil"
    elif line.startswith("soil-to-fertilizer map:"):
        current_map = "soil_to_fertilizer"
    elif line.startswith("fertilizer-to-water map:"):
        current_map = "fertilizer_to_water"
    elif line.startswith("water-to-light map:"):
        current_map = "water_to_light"
    elif line.startswith("light-to-temperature map:"):
        current_map = "light_to_temperature"
    elif line.startswith("temperature-to-humidity map:"):
        current_map = "temperature_to_humidity"
    elif line.startswith("humidity-to-location map:"):
        current_map = "humidity_to_location"
    elif current_map:
        values = list(map(int, line.split()))
        if len(values) == 3:
            if current_map not in maps:
                maps[current_map] = []
            maps[current_map].append(tuple(values))

  return maps

# Function to perform mapping
def map_value(value, mapping):
    # Iterate through the mapping rules
    for dest_start, source_start, length in mapping:
        # Check if the value falls within the source range
        if source_start <= value < source_start + length:
            # Calculate the corresponding value in the destination range
            return dest_start + (value - source_start)
    
    # If no mapping is found, return the original value
    return value

seeds = parse_seeds(data)
maps = parse_maps(data)
seed_to_soil_map = maps['seed_to_soil']
soil_to_fertilizer_map = maps['soil_to_fertilizer']
fertilizer_to_water_map = maps['fertilizer_to_water']
water_to_light_map = maps['water_to_light']
light_to_temperature_map = maps['light_to_temperature']
temperature_to_humidity_map = maps['temperature_to_humidity']
humidity_to_location_map = maps['humidity_to_location']

# Part 1

# Perform the mappings
for seed in seeds:
    soil = map_value(seed, seed_to_soil_map)
    fertilizer = map_value(soil, soil_to_fertilizer_map)
    water = map_value(fertilizer, fertilizer_to_water_map)
    light = map_value(water, water_to_light_map)
    temperature = map_value(light, light_to_temperature_map)
    humidity = map_value(temperature, temperature_to_humidity_map)
    location = map_value(humidity, humidity_to_location_map)

    if 'lowest_location' not in locals() or location < lowest_location:
        lowest_location = location

# Print the lowest location
print("Lowest Location:", lowest_location)