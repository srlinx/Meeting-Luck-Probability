import math

# Calculate total possible pairs of encounters
total_pairs = math.comb(7900000000, 2)

# Calculate total number of people we can encounter twice
people_twice = 7900000000

# Calculate probability of meeting a random person twice
prob_twice = math.comb(people_twice, 2) / total_pairs

print("Probability of meeting a random person twice in life: {:.10f}".format(prob_twice))
