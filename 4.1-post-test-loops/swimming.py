import time

swimmer1 = "GALLANT"
# Gallant is careful and checks the water temperature before he dives right in.
swimmer2 = "GOOFUS "
# Goofus dives into the lake before checking the water temperature.

minimum_temperature = 79.0  # degrees Fahrenheit
current_temperature = 0.0
saved_temperature = 0.0
swim_time = 0

current_temperature = float(input("What is the current water temperature? "))
# Inputting 80.5: outputs the same amount of time for both Goofus and Gallant.
# Inputting 78: Gallant now doesn't start swimming, and Goofus only swims for a total of 1 min.
saved_temperature = current_temperature  # saves a copy of this value so we can get it back later.

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer1} approaches the lake....")

swim_time = 0
while current_temperature >= minimum_temperature:
    print(f"\t{swimmer1} swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)  # pauses for 600 milliseconds
    current_temperature -= 0.5  # subtracts 1/2 a degree from the water temperature
    print(f"\tThe current water temperature is now {current_temperature} F.")

print(f"{swimmer1} stops swimming. Total swim time: {swim_time} min.")

current_temperature = saved_temperature  # restores original water temperature

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer2} approaches the lake....")

swim_time = 0
while True:
    print("\t" + swimmer2 + " swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)
    current_temperature -= 0.5
    print(f"\tThe current water temperature is now {current_temperature} F.")

    if current_temperature < minimum_temperature:
        break # This keyword breaks out of the while loop when it is false, which is why Goofus only leaves the lake after he has dived in and evaluated the temperature.

# The differences between the first and second while loops is that the first one only runs while a condition is true, whereas the second one runs no matter what condition, but it breaks out when a condition is evaluated to false.
# Pre-test loop: The first loop is a pre-test loop because it tests the condition BEFORE entering it.
# Post-test loop: The second loop is a post-test loop because it performs the action and tests the condition AFTER entering it.

print(f"{swimmer2} stops swimming. Total swim time: {swim_time} min.")
