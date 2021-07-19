## Paint The Walls
## Objective: Using a predetermined rate, find the time it takes a certain number of people to paint a certain number of walls



rate = {
    "people" : 10,
    "walls" : 10,
    "minutes" : 22
}

def Time(rate, people, walls):
    walls_people = rate["walls"] / rate["people"]
    minutes_people = rate["minutes"] / rate["people"]
    final_rate = minutes_people / walls_people
    print(final_rate * walls)

Time(rate, 14, 14)