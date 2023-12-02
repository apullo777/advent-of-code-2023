with open('input.txt') as file:
    data = file.read().strip()

def sum_valid_game_ids(game_strings, max_values):
  sum_of_ids = 0

  for game_string in game_strings.split("\n"):
      # Extract the game ID
      game_id = int(game_string.split(':')[0].split(' ')[1])

      # Split the string into components
      components = game_string.split(':')[1].split(';')

      # Assume the game is valid until proven otherwise
      game_valid = True

      # Process each component and compare with max values
      for component in components:
          color_quantity_pairs = component.split(',')
          component_color_quantities = {}
          for pair in color_quantity_pairs:
              if pair.strip():  # Check if not empty
                  parts = pair.strip().split(' ')
                  color = parts[1]
                  quantity = int(parts[0])
                  component_color_quantities[color] = component_color_quantities.get(color, 0) + quantity

          # Compare with max values
          for color, quantity in component_color_quantities.items():
              if quantity > max_values.get(color, float('inf')):
                  game_valid = False
                  break

          if not game_valid:
              break

      if game_valid:
          sum_of_ids += game_id

  return sum_of_ids


# Part 1
max_values = {"red": 12, "green": 13, "blue": 14}

result = sum_valid_game_ids(data, max_values)
print("Sum of Valid Game IDs:", result)

  
