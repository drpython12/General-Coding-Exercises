## Paint The Walls
## Objective: Using a predetermined rate, find the time it takes a certain number of people to paint a certain number of walls



rate = {
    "people" : 10,
    "walls" : 10,
    "minutes" : 22
}

def Time(dct, people, walls):
	walls_people = dct["walls"] / dct["people"]
	minutes_people = dct["minutes"] / dct["people"]
	final_rate = minutes_people / walls_people
	print(int(final_rate * walls))

Time(rate, 14, 14)