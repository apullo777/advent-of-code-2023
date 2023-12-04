with open('input.txt') as file:
  data = file.read().strip()

def count_matching_numbers(winning_numbers, your_numbers):
  winning_set = set(map(int, winning_numbers.split()))
  your_set = set(map(int, your_numbers.split()))
  return len(winning_set.intersection(your_set))

def calculate_points(num_matches):
  if num_matches == 0: 
    return 0
  else: 
    return 2**(num_matches-1)

def add_copies_to_array(card_num, win_num, arr):
  max_cards = 207
  for i in range(1, win_num + 1):
      target_index = card_num + i - 1
      if target_index < max_cards:
          arr[target_index] += 1 if arr[card_num - 1] == 0 else arr[card_num - 1]
      else:
          break

# Part 1
total_points = 0
for line in data.split("\n"):
  parts = line.split(':')[1]
  winning, your = parts.split('|')
  num_matches = count_matching_numbers(winning, your)
  total_points += calculate_points(num_matches)
print(f"Total points: {total_points}")

# Part 2
card_num = 0
arr = [1] * 207  # Initialize the array with 1s

for line in data.strip().split("\n"):
  card_num += 1
  parts = line.split(':')[1]
  winning = parts.split('|')[0].strip()
  your = parts.split('|')[1].strip()
  num_matches = count_matching_numbers(winning, your)
  add_copies_to_array(card_num, num_matches, arr)

total_copies = sum(arr)
print(f"Total copies: {total_copies}")




