print("Weight\n")

Weight = input()

print("Reps\n")

Reps = input()

Results = float(Weight) / ( 1.0278 - 0.0278 * float(Reps) )

print("Your 1rm is", Results)


# 1RM = weight / ( 1.0278 – 0.0278 × reps )