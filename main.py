import csv


def get_quest_data():
    sorted_quests = []
    csv_path = input('Please input the path to the .csv file where your quests are stored: ')
    try:
        with open(csv_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_number = 0
            for row in csv_reader:
                if line_number == 0:
                    line_number += 1
                sorted_quests.append({
                    'name': row['quest'],
                    'start': int(row['start']),
                    'duration': int(row['duration']),
                    'reward': int(row['reward']),
                    'difficulty': row['difficulty'],
                    'location': row['location'],
                    'quest_giver': row['quest_giver']
                })
                line_number += 1
    except PermissionError:
        print('Could not access file.')
    except KeyError:
        print('The .csv file is not correctly formatted.')
    except FileNotFoundError:
        print('Could not find the file you entered.')
    except Exception as e:
        print(f'An unknown error occurred, please try again. {e}')
    return sorted_quests


print('Make sure you have a .csv file with quests arranged in columns of "quest", "start", "duration", "reward", '
      '"difficulty", "location", and "quest_giver".')
print('Reference "example.csv" for formatting questions.')
quest_log = []
attempts = 0
while quest_log.__len__() == 0 and attempts < 5:
    quest_log = get_quest_data()
    attempts += 1
if quest_log.__len__() == 0:
    print('No quests were found or the program timed out.')
    exit(0)
quest_log.sort(key=lambda x: x['reward'], reverse=True)
maximum_reward = 0
maximized_quests = []
for initial_quest in quest_log:
    test_log = [initial_quest]
    possible_reward = initial_quest['reward']
    for possible_quest in quest_log:
        quest_validity = 0
        for quest in test_log:
            current_start = quest['start']
            comparison_start = possible_quest['start']
            current_end_date = current_start + quest['duration']
            comparison_end_date = comparison_start + possible_quest['duration']
            if (comparison_start < current_start and comparison_end_date <= current_start) or (
                    comparison_start >= current_end_date):
                quest_validity += 1
        if quest_validity == test_log.__len__():
            test_log.append(possible_quest)
            possible_reward += possible_quest['reward']
    if possible_reward > maximum_reward:
        maximum_reward = possible_reward
        maximized_quests = test_log
print(f'Maximum Reward: {maximum_reward} rupees')
maximized_quests.sort(key=lambda x: x['start'])
print(f'Quests:')
quest_number = 1
for quest in maximized_quests:
    print(f'{quest_number}. {quest["name"]}\n'
          f'   Start: {quest["start"]}\n'
          f'   Duration: {quest["duration"]} days\n'
          f'   Reward: {quest["reward"]} rupees\n'
          f'   Difficulty: {quest["difficulty"]}\n'
          f'   Location: {quest["location"]}\n'
          f'   Quest Giver: {quest["quest_giver"]}')
    quest_number += 1
