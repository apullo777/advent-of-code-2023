
data_dict = {}  # Initialize the data_dict as an empty dictionary

with open("input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            hand, bet = parts
            rank = 0  # Default rank
            data_dict[hand] = {"bet": bet, "rank": rank}

def max_two_counts_from_string_with_wild(hand_str):
  rank_count = {}
  wild_card = 0

  for rank in hand_str:
      if rank == 'J':
          wild_card += 1
      else:
          rank_count[rank] = rank_count.get(rank, 0) + 1

  max_counts = sorted([count for count in rank_count.values() if count > 1], reverse=True)

  if wild_card == 5: # five wild cards
      return [wild_card]
  if wild_card > 0:
      if not max_counts: # high card
          return [wild_card + 1]
      max_counts[0] += wild_card # wild card(s) add to the highest count
      return max_counts[:2] if len(max_counts) > 1 else max_counts
  else:
      return max_counts[:2] if len(max_counts) > 1 else max_counts

def is_hand1_stronger(hand1_str, hand2_str):
  card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T':10}

  for card1, card2 in zip(hand1_str, hand2_str):
    card1_value = card_values[card1] if card1 in card_values else (int(card1) if card1.isdigit() else None)
    card2_value = card_values[card2] if card2 in card_values else (int(card2) if card2.isdigit() else None)
    
    if card1_value != card2_value:
        return card1_value > card2_value

  return False

def selection_sort_in_place(arr):
  n = len(arr)

  for i in range(n):
      max_index = i
      for j in range(i + 1, n):
          if is_hand1_stronger(arr[j], arr[max_index]):  # Compare in reverse order
              max_index = j

      # Swap the maximum element with the current element (in-place)
      arr[i], arr[max_index] = arr[max_index], arr[i]

def classify_poker_hand(hand_str, classifications):
  max_counts = max_two_counts_from_string_with_wild(hand_str)
  
  if max_counts == [5]:
    classifications["five_of_a_kind"].append(hand_str)
  elif max_counts == [4]:
    classifications["four_of_a_kind"].append(hand_str)
  elif max_counts == [3, 2]:
    classifications["full_house"].append(hand_str)
  elif max_counts == [3]:
    classifications["three_of_a_kind"].append(hand_str)
  elif max_counts == [2, 2]:
    classifications["two_pair"].append(hand_str)
  elif max_counts == [2]:
    classifications["one_pair"].append(hand_str)
  else:
    classifications["high_card"].append(hand_str)

  return classifications


def update_ranking(classifications, data_dict):
  # Create a list of keys to iterate over in the desired order
  keys_order = ['five_of_a_kind', 'four_of_a_kind', 'full_house',
                'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']

  # Initialize a rank counter
  rank = 1

  # Loop through each key in the desired order
  for key in keys_order:
    hands = classifications[key]
    selection_sort_in_place(hands)

    for hand in hands:
      data_dict[hand]["rank"] = rank
      rank += 1


classifications = {
  "five_of_a_kind": [],
  "four_of_a_kind": [],
  "full_house": [],
  "three_of_a_kind": [],
  "two_pair": [],
  "one_pair": [],
  "high_card": []
}

# Print the list of dictionaries

for hand in list(data_dict.keys()) :
  classify_poker_hand(hand, classifications)

update_ranking(classifications, data_dict)

total_winnings = 0
for hand, info in data_dict.items():
  bet = int(info['bet'])
  rank = info['rank']
  point = len(data_dict) - rank + 1
  winnings = bet * point
  total_winnings += winnings

print("Total Winnings:", total_winnings)
print(classifications)
print(data_dict)
