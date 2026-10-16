import random #Do not update or remove

def main():
    input_filename = "WorldCapitals.txt" #Do not update
    output_filename = "HighScores.txt" #Do not update
    username = "wxyz001" #use your username
    #To complete
    print_banner(username)
    world_capitals_dict = get_world_capitals_dictionary("WorldCapitals.txt")
    print(run_quiz(get_world_capitals_dictionary("WorldCapitals.txt")))

#To complete
def print_banner(username):
    banner_title = f"#  World Capitals Quiz For {username.upper()}  #"
    print("#" * len(banner_title))
    print(banner_title)
    print("#" * len(banner_title))

#To complete
def get_world_capitals_dictionary(filename):
    output_stream = open(filename, "r")
    lists = output_stream.readline().strip()
    result = {}
    while lists != "":
        lists = lists.split(":")
        result[lists[0]] = lists[1]
        lists = output_stream.readline().strip()
    output_stream.close()
    return result

#To complete
def get_player_answer(target_country, cities):
    print(f"Choices available: {cities}")
    print()
    user_input = input(f"Enter the captital city of {target_country} : {cities}")
    while user_input not in cities:
        print("You must choose from the city choices available!")
        user_input = input(f"Enter the captital city of {target_country} : {cities}")
    return user_input

#To complete
def run_round(world_capitals_dict, countries_tested):
    question_data = get_question_data(world_capitals_dict, countries_tested);
    correct_country = question_data[0]
    city_options = question_data[1]
    correct_city = world_capitals_dict[correct_country]

    print("coorect city", correct_city)

    score = 3

    
    while score > 0 :
        player_answer = get_player_answer(correct_country, city_options)
        if player_answer == correct_city:
            print("Yay")
            break
        else:
            if score != 1:
                print("try again")
            score -= 1
    return score

#To complete
def run_quiz(world_capitals_dict):
    countries_tested = []
    score  = 0

    score += run_round(world_capitals_dict, countries_tested)
    return score

#To complete
def read_high_scores(filename):
    pass

#To complete
def update_high_scores(filename, username, high_scores, new_score):
    pass

#To complete
def handle_high_scores(username, new_score, filename):
    pass

#Do not update or remove
def get_question_data(world_capitals_dict, countries_tested):
    countries = list(world_capitals_dict.keys())
    target_country = countries[random.randrange(0, len(countries))]
    while target_country in countries_tested:
        target_country = countries[random.randrange(0, len(countries))]
    countries_tested.append(target_country)
    countries.remove(target_country)
    cities = [world_capitals_dict[target_country]]
    while len(cities) < 5:
        country = countries[random.randrange(0, len(countries))]
        countries.remove(country)
        cities.append(world_capitals_dict[country])
    random.shuffle(cities)
    return target_country, cities

#Do not update or remove   
main()
