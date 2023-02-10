import random

class SqueezeIn:
	def __init__(self, worked_hard, important_message):
		self.worked_hard = worked_hard
		self.important_message = important_message

		# Prints the important message
		print(self.important_message)



	# Function to determine whether the opportunity came or not
	def opportunity_came(self):
		# Returns True or False randomly
		return random.choice([True, False])



	# Function to return a random quote from the TikTok user @mshwishwiri_official
	def quote_mshwishwiri(self):
		quotes = [
			"O sa reng?",
			"O tlo re gafela wen'",
			"'a e nyake ka mokg'o",
			"'gwete!"
		]

		return random.choice(quotes)



	# Function to determine whether the 'Squeeze' is loaded or not
	def determine_squeezing(self, window_is_open):

		# Check if the user worked hard and the window is open
		if self.worked_hard and window_is_open:
			return "..loading the 'Squeeze'!"
		else:
			return "Hard luck bozza!"




request = SqueezeIn(True, "'Re squeezeng-In, le re na re nyaka go ba gona mo industr-ing. Re lokeleng!!!'\n")

open_window = request.opportunity_came()

print("[" + str(open_window) + "] - " + request.determine_squeezing(open_window) + "\n")
print(request.quote_mshwishwiri())



"""
	[ OUTPUT ]

	'Re squeezeng-In, le re na re nyaka go ba gona mo industr-ing. Re lokeleng!!!'

	[False] - Hard luck bozza!

	'a e nyake ka mokg'o



	Context = https://www.tiktok.com/@debongz_d/video/7189919607459728645?lang=en

"""