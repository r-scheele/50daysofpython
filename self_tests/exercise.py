travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, number_of_visits, cities_visited):
    new_entry = {
        'country': country,
        'visits': number_of_visits,
        'cities': cities_visited
    }
    travel_log.append(new_entry)

def summary_of_visit(entry):
  return print(f"You've visited {entry['country']} {entry['visits']} times.\nYou've been to {entry['cities'][0]} and {entry['cities'][0]}.")



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
summary_of_visit(travel_log[2])
print(travel_log)
