print("Firstly, we must determine the amount of fuel, and whether it is proportional to the weight of your rocket:")
# Step 1: User input fuel amount
# Step 2: User input weight of rocket
# Step 3: Analyze whether the fuel amount >= 90 percent of the weight
# Step 4: If enough output yes can fly else list how much less by and refuel
Rocket_fuel = float(input("How much Fuel does your Rocket have? "))
Rocket_weight = float(input("How much does your Rocket weigh? "))
if Rocket_fuel < 0.9 * Rocket_weight:  # Check if fuel is less than 90% of the weight
    print("You need this much more fuel:", Rocket_weight - Rocket_fuel)  # Output how much more fuel is needed
else:
    print("You're good on fuel, you have more than or equal to 90% your rocket's weight!")  # Output if fuel is sufficient
print("Enter Details Below to start calculating the thrust needed to start the rocket: ")
mass = int(input("What is the mass of the rocket (kg)? "))
exhaust_velo = int(input("What is the exhaust velocity? "))
Exhaust_pressure = int(input("What is the exhaust pressure? "))
ambient_pressure = int(input("What is the ambient pressure? "))
nozz_exit = int(input("What is the nozzle exit area? "))
Thrust = mass * exhaust_velo + (Exhaust_pressure - ambient_pressure) * nozz_exit
print("The Thrust required to start your rocket is " + str(Thrust) + " Newtons")
print("Great we've completed the basic checklist of calculations needed, have a fun flight!")