def find_difference_to_exceed_target(number, target):
  for i in range(1, number):
    if i * (number - i) > target:
      return (number - i) - i + 1
  return None

def product_of_differences_in_range(start, end, target):
  product = 1
  for number in range(start, end + 1):
      difference = find_difference_to_exceed_target(number, target)
      if difference is not None:
          product *= difference
  return product

# Part 1
data = "[49, 356], [87, 1378], [78, 1502], [95, 1882]"
pairs = [pair.strip('[]').split(', ') for pair in data.split('], [')]
product = 1

for pair in pairs:
  time = int(pair[0])
  distance = int(pair[1])
  difference = find_difference_to_exceed_target(time, distance)
  product *= difference

print(f"The product of differences is {product}")

# Part2
difference = find_difference_to_exceed_target(49877895, 356137815021882)
print(f"The result is {difference}")