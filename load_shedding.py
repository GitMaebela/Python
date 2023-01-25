import random

# South Africa Diesel prices, 23-Jan-2023
# Fuel Type			|	 Fuel Price
# Diesel 50			|	 R21.41

# Sample Generator Spec
# Power output – 24KW (30kVa)
# Power factor: 0.8
# Rated voltage – Three Phase (380V)
# Current Output – 43.2A
# Fuel consumption – 5.89 LPH

# Parameters
generator_fuel_price = 21.41
generator_fuel_consumption = 5.89
generator_fuel_capacity = 3785.41

load_shedding_stages = {
	"stage1": {
		"name": "Stage 1",
		"duration": 2
	},
	"stage2": {
		"name": "Stage 2",
		"duration": 2
	},
	"stage3": {
		"name": "Stage 3",
		"duration": 4
	},
	"stage4": {
		"name": "Stage 4",
		"duration": 6
	},
	"stage5": {
		"name": "Stage 5",
		"duration": 8
	},
	"stage6": {
		"name": "Stage 6",
		"duration": 8
	},
	"stage7": {
		"name": "Stage 7",
		"duration": 10
	},
	"stage8": {
		"name": "Stage 8",
		"duration": 12
	}
}

# Initialize generator fuel level
generator_fuel_level = generator_fuel_capacity

# Number of days in 3 months
days_in_3_months = 3*30

# Initialize counter for days with no outage
no_outage_counter = 0

# Function to determine the shedding stage
def determine_shedding_stage():
	stage_number = random.randint(1,8)
	return load_shedding_stages[f'stage{stage_number}']['duration']

# Simulate 3 months of operation
for day in range(days_in_3_months):
	# Check for an outage
	outage_duration = determine_shedding_stage()
	if outage_duration > 0:
		if generator_fuel_level >= generator_fuel_consumption*outage_duration:
			# Decrease fuel level based on consumption rate
			generator_fuel_level -= generator_fuel_consumption*outage_duration
			print(f'Outage on day {day}, using generator for {outage_duration} hours. Fuel level: {generator_fuel_level:.2f} liters')
		else:
			# Outage occurs but generator out of fuel
			print(f'Outage on day {day}, generator out of fuel. Cost: R{generator_fuel_capacity * generator_fuel_price:.2f}')
	else:
		# No outage, increment counter
		no_outage_counter += 1

# Print final generator fuel level and cost
final_fuel_cost = generator_fuel_price * (generator_fuel_capacity - generator_fuel_level)
final_fuel_level_percentage = (generator_fuel_level/generator_fuel_capacity)*100

# Print the number of days with no outage
print(f'No outage for {no_outage_counter} days')
print(f'Final generator fuel level: {final_fuel_level_percentage:.2f}%. Cost: R{final_fuel_cost:.2f}')
