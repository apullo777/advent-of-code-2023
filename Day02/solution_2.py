with open('input.txt') as file:
    data = file.read().strip()

def sum_of_min_sets_product(game_strings):
    sum_of_products = 0
    for game_string in game_strings.split("\n"):
        product_of_sets = 1
        # Extracting components after the colon and splitting by semicolon
        components = game_string.split(':')[1].split(';')
        min_set = {"red": 0, "green": 0, "blue": 0}
        
        # Process each component and compare with max values
        for component in components:
            # Splitting each component into color-quantity pairs
            color_quantity_pairs = component.split(',')
            for pair in color_quantity_pairs:
                if pair.strip():  # Check if not empty
                    parts = pair.strip().split(' ')
                    color = parts[1]
                    quantity = int(parts[0])
                    # Update the minimum set quantity for each color
                    if quantity > min_set[color]: 
                        min_set[color] = quantity

        # Calculating the product of the quantities in the min set
        for color, quantity in min_set.items():
            product_of_sets *= quantity
      
        sum_of_products += product_of_sets

    return sum_of_products


# Part 2

result = sum_of_min_sets_product(data)
print("Sum of Min Sets Products:", result)
  
