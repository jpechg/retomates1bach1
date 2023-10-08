import itertools

# Generate all possible combinations of 5 numbers from 1 to 49
combinations = list(itertools.combinations(range(1, 50), 5))

total_combinations = len(combinations)

# Scenario a) Guessing all 5 numbers correctly
# There is only one correct combination, so the probability is 1 / total_combinations
prob_a = 1 / total_combinations

# Scenario b) 2 numbers being in the same tens place and the other 3 numbers in different tens places
count_b = 0
for combination in combinations:
    tens_places = [number // 10 for number in combination]
    if len(set(tens_places)) == 4 and tens_places.count(max(tens_places, key=tens_places.count)) == 2:
        count_b += 1
prob_b = count_b / total_combinations

# Scenario c) Only 2 numbers having the same ones place
count_c = 0
for combination in combinations:
    ones_places = [number % 10 for number in combination]
    if len(set(ones_places)) == 4 and ones_places.count(max(ones_places, key=ones_places.count)) == 2:
        count_c += 1
prob_c = count_c / total_combinations

print(f"Probability of guessing all 5 numbers correctly: {prob_a}")
print(f"Probability of 2 numbers being in the same tens place and the other 3 numbers in different tens places: {prob_b}")
print(f"Probability of only 2 numbers having the same ones place: {prob_c}")
