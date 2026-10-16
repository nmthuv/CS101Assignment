import random #Do not update or remove

def main():
    input_filename = "WorldCapitals.txt" #Do not update
    output_filename = "HighScores.txt" #Do not update
    username = "wxyz001" #use your username
    #To complete
    print_banner(username)
    world_capitals_dict = get_world_capitals_dictionary(input_filename)
    overall_score = run_quiz(world_capitals_dict)
    handle_high_scores(username, overall_score, output_filename)

#To complete
def print_banner(username):
    banner_title = f"#  World Capitals Quiz For {username.upper()}  #"
    print("#" * len(banner_title))
    print(banner_title)
    print("#" * len(banner_title))
    print()

#To complete
def get_world_capitals_dictionary(filename):
    input_stream = open(filename, "r")
    line_contents = input_stream.readline().strip()
    world_capitals_dict = {}
    while line_contents != "":
        line_contents = line_contents.split(":")
        world_capitals_dict[line_contents[0]] = line_contents[1]
        line_contents = input_stream.readline().strip()
    input_stream.close()
    return world_capitals_dict

#To complete
def get_player_answer(target_country, cities):
    print(f"Choices available: {cities}")
    print()
    user_input = input(f"What is the capital city of {target_country}? ")
    while user_input not in cities:
        print("You must choose from the city choices available!")
        user_input = input(f"What is the capital city of {target_country}? ")
    return user_input

#To complete
def run_round(world_capitals_dict, countries_tested):
    question_data = get_question_data(world_capitals_dict, countries_tested)
    target_country = question_data[0]
    city_options = question_data[1]
    correct_city = world_capitals_dict[target_country]
    round_score = 3
    answer_is_correct = False
    while round_score > 0 and not answer_is_correct:
        player_answer = get_player_answer(target_country, city_options)
        if player_answer == correct_city:
            print("Your answer is correct! Well done!")
            answer_is_correct = True
        else:
            if round_score > 1:
                print("Your answer is incorrect! Please try again!\n")
            else:
                print("Your answer is incorrect! Better luck next time!\n")
            round_score -= 1
    return round_score

#To complete
def run_quiz(world_capitals_dict):
    countries_tested = []
    overall_score  = 0
    total_rounds = 6

    for i in range(1, total_rounds + 1) :
        print()
        print(f"Round {i}")
        print()

        overall_score += run_round(world_capitals_dict, countries_tested)
    return overall_score

#To complete
def read_high_scores(filename):
    input_stream = open(filename, "r")
    line_contents = input_stream.readline().strip()
    line_contents = input_stream.readline().strip()
    top5_high_scores_list = []
    while line_contents != "":
        line_contents = line_contents.split()
        top5_high_scores_list.append(int(line_contents[1]))
        line_contents = input_stream.readline().strip()
    input_stream.close()
    return top5_high_scores_list

#To complete
def update_high_scores(filename, username, high_scores, new_score):
    output_stream = open(filename, "w")
    output_stream.write(f"High Scores for {username}")
    if len(high_scores) < 5 or new_score > min(high_scores):
        high_scores.append(new_score)
        high_scores.sort(reverse=True)
        high_scores = high_scores[:5]
    for i in range(len(high_scores)):
        output_stream.write(f"\n{i + 1}. {high_scores[i]}")
    output_stream.close()

#To complete
def handle_high_scores(username, new_score, filename):
    high_scores = read_high_scores(filename)
    update_high_scores(filename, username, high_scores, new_score)

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
