import game_data
import random
import diagram

print(diagram.title_logo)

def random1():
    global random_value1
    random_value1 = random.randint(0,len(game_data.data))

def random2():
    global random_value2
    random_value2 = random.randint(0,len(game_data.data))

random1()
random2()
start = True
count = 0
a = f"{game_data.data[random_value1]['name']}, a {game_data.data[random_value1]['description']}, from {game_data.data[random_value1]['country']}."
while start:

    #a = f"{game_data.data[random_value1]['name']}, a {game_data.data[random_value1]['description']}, from {game_data.data[random_value1]['country']}."

    b = f"{game_data.data[random_value2]['name']}, a {game_data.data[random_value2]['description']}, from {game_data.data[random_value2]['country']}."

    print(a+"\n")
    print(diagram.vs+"\n")
    print(b+"\n")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice.lower() == 'a':
        if game_data.data[random_value1]['follower_count'] > game_data.data[random_value2]['follower_count'] or game_data.data[random_value1]['follower_count'] == game_data.data[random_value2]['follower_count'] :
            a = b
            random2()
            count += 1
            continue
        elif game_data.data[random_value1]['follower_count'] < game_data.data[random_value2]['follower_count']:
            print(f"Sorry, that's wrong. Final score: {count} ")
            break
    elif choice.lower() == 'b':
        if game_data.data[random_value2]['follower_count'] > game_data.data[random_value1]['follower_count'] or game_data.data[random_value2]['follower_count'] == game_data.data[random_value1]['follower_count']:
            a = b
            random2()
            count += 1
            continue
        elif game_data.data[random_value2]['follower_count'] < game_data.data[random_value1]['follower_count']:
            print(f"Sorry, that's wrong. Final score: {count}")
            break

    


