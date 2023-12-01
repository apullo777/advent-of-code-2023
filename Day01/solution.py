with open('input.txt') as file:
    data = file.read().strip()

def find_digit(input_string, mode):
    if mode == 1:
        for char in input_string:
            if char.isdigit():
                return int(char)
    elif mode == -1:
        for char in reversed(input_string):
            if char.isdigit():
                return int(char)
    return None  # Return None if no digit is found

def find_first_number(s, mode='forward'):
  # Dictionary mapping number words to their numeric equivalents
  number_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                  "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

  # Function to check if a substring is a number word and return its numeric value
  def check_number_word(word):
      if word in number_words:
          return number_words[word]
      return None

  if mode == 'forward':
      # Check both standalone digits and number words
      # Using a sliding window approach to examine each substring
      # The window starts from each character and expands to include subsequent characters
      for start in range(len(s)):
          for end in range(start + 1, len(s) + 1):
              current_word = s[start:end].lower()
              # Check if the current substring is a digit and return it if true
              if current_word.isdigit():
                  return int(current_word)

              # Check if the current substring matches a number word
              number = check_number_word(current_word)
              if number is not None:
                  return number

  # Scanning the string in backward mode
  else:
      # Check both standalone digits and number words in backward mode
      for start in range(len(s), 0, -1):
          for end in range(start - 1, -1, -1):
              current_word = s[end:start].lower()
              if current_word.isdigit():
                  return int(current_word)

              number = check_number_word(current_word)
              if number is not None:
                  return number

  return None  # No number found


# Part 1

total_1 = 0
for line in data.split("\n"):
    forward_digit = find_digit(line, 1)
    backward_digit = find_digit(line, -1)
    total_1 += 10 * forward_digit + backward_digit

print(total_1)

# Part 2

total_2 = 0
for line in data.split("\n"):
    forward_digit = find_first_number(line, "forward")
    backward_digit = find_first_number(line, "backward")
    total_2 += 10 * forward_digit + backward_digit

print(total_2)