# Using edamam recipe api: https://developer.edamam.com/edamam-docs-recipe-api
from random import randint
import requests
import json

url = 'https://api.edamam.com/search'
user = '97a59ced'
key = '5fed61ed8cfad28dafda078fd8a9a2a9'

def randomMealPlan(diet_type: 'string', calories_wanted: 'int') -> '{}':
    mealPlanType = {
        'Any': anyDiet,
        'Vegan': veganDiet,
        'Vegetarian': vegetarianDiet,
        'Paleo': paleoDiet,
        'Ketogenic': ketoDiet,
    }

    return mealPlanType[diet_type](calories_wanted)

def anyDiet(calories_wanted: 'int') -> {}:
    min = (calories_wanted // 4) - 20
    max = (calories_wanted // 4) + 20

    range = str(min) + '-' + str(max)
    try:
        response = requests.get(
            url,
            params={'q': '',                # Word filter, blank gets all.
                    'calories': range,  # Calorie range, can also be an exact int.
                    #'health': 'paleo',      # Health is basically "diet type"
                    'diet': 'balanced',     # Balanced makes sure the call gets real food.
                    'from': 0,              # With queries that have many hits from - to
                    'to': 40,               # returns the results in that range.
                    'app_id': user,         
                    'app_key': key}
        )

        data = response.json()
    except:
        return {}

    options = {}
    index = 0

    for x in data['hits']:
        options[index] = [x['recipe']['label'], x['recipe']['calories']/x['recipe']['yield'], x['recipe']['image']]
        index = index + 1

    randomNums = set()
    while len(randomNums) is not 4:
        randomNums.add(randint(0, len(options) - 1))

    random_b = randomNums.pop()
    random_l = randomNums.pop()
    random_d = randomNums.pop()
    random_s = randomNums.pop()

    #Remove blacklisted words
    blacklist = ['recipes', 'recipe']
    for blacklistedWord in blacklist:
        options[random_b][0] = options[random_b][0].replace(blacklistedWord, '')
        options[random_b][0] = options[random_b][0].title()

        options[random_l][0] = options[random_l][0].replace(blacklistedWord, '')
        options[random_l][0] = options[random_l][0].title()

        options[random_d][0] = options[random_d][0].replace(blacklistedWord, '')
        options[random_d][0] = options[random_d][0].title()

        options[random_s][0] = options[random_s][0].replace(blacklistedWord, '')
        options[random_s][0] = options[random_s][0].title()

    anyMeal = {
            'breakfast': {
                'title': options[random_b][0],
                'calories': int(options[random_b][1]),
                'image': options[random_b][2]
            },
            'lunch': {
                'title': options[random_l][0],
                'calories': int(options[random_l][1]),
                'image': options[random_l][2]
            },
            'dinner': {
                'title': options[random_d][0],
                'calories': int(options[random_d][1]),
                'image': options[random_d][2]
            },
            'snack': {
                'title': options[random_s][0],
                'calories': int(options[random_s][1]),
                'image': options[random_s][2]
            }
    }
    
    return anyMeal

def veganDiet(calories_wanted: 'int') -> {}:
    min = (calories_wanted // 4) - 20
    max = (calories_wanted // 4) + 20

    range = str(min) + '-' + str(max)
    try:
        response = requests.get(
            url,
            params={'q': '',                # Word filter, blank gets all.
                    'calories': range,  # Calorie range, can also be an exact int.
                    'health': 'vegan',      # Health is basically "diet type"
                    'diet': 'balanced',     # Balanced makes sure the call gets real food.
                    'from': 0,              # With queries that have many hits from - to
                    'to': 20,               # returns the results in that range.
                    'app_id': user,         
                    'app_key': key}
        )

        data = response.json()
    except:
        return {}

    options = {}
    index = 0

    for x in data['hits']:
        options[index] = [x['recipe']['label'], x['recipe']['calories']/x['recipe']['yield'], x['recipe']['image']]
        index = index + 1

    randomNums = set()
    while len(randomNums) is not 4:
        randomNums.add(randint(0, len(options) - 1))

    random_b = randomNums.pop()
    random_l = randomNums.pop()
    random_d = randomNums.pop()
    random_s = randomNums.pop()

        #Remove blacklisted words
    blacklist = ['recipes', 'recipe']
    for blacklistedWord in blacklist:
        options[random_b][0] = options[random_b][0].replace(blacklistedWord, '')
        options[random_b][0] = options[random_b][0].title()

        options[random_l][0] = options[random_l][0].replace(blacklistedWord, '')
        options[random_l][0] = options[random_l][0].title()

        options[random_d][0] = options[random_d][0].replace(blacklistedWord, '')
        options[random_d][0] = options[random_d][0].title()

        options[random_s][0] = options[random_s][0].replace(blacklistedWord, '')
        options[random_s][0] = options[random_s][0].title()

    veganMeal = {
            'breakfast': {
                'title': options[random_b][0],
                'calories': int(options[random_b][1]),
                'image': options[random_b][2]
            },
            'lunch': {
                'title': options[random_l][0],
                'calories': int(options[random_l][1]),
                'image': options[random_l][2]
            },
            'dinner': {
                'title': options[random_d][0],
                'calories': int(options[random_d][1]),
                'image': options[random_d][2]
            },
            'snack': {
                'title': options[random_s][0],
                'calories': int(options[random_s][1]),
                'image': options[random_s][2]
            }
    }
    
    return veganMeal

def vegetarianDiet(calories_wanted: 'int') -> {}:
    min = (calories_wanted // 4) - 20
    max = (calories_wanted // 4) + 20

    range = str(min) + '-' + str(max)
    try:
        response = requests.get(
            url,
            params={'q': '',                # Word filter, blank gets all.
                    'calories': range,  # Calorie range, can also be an exact int.
                    'health': 'vegetarian',      # Health is basically "diet type"
                    'diet': 'balanced',     # Balanced makes sure the call gets real food.
                    'from': 0,              # With queries that have many hits from - to
                    'to': 20,               # returns the results in that range.
                    'app_id': user,         
                    'app_key': key}
        )

        data = response.json()
    except:
        return {}
        # no JSON returned

    options = {}
    index = 0

    for x in data['hits']:
        options[index] = [x['recipe']['label'], x['recipe']['calories']/x['recipe']['yield'], x['recipe']['image']]
        index = index + 1

    randomNums = set()
    while len(randomNums) is not 4:
        randomNums.add(randint(0, len(options) - 1))

    random_b = randomNums.pop()
    random_l = randomNums.pop()
    random_d = randomNums.pop()
    random_s = randomNums.pop()

    #Remove blacklisted words
    blacklist = ['recipes', 'recipe']
    for blacklistedWord in blacklist:
        options[random_b][0] = options[random_b][0].replace(blacklistedWord, '')
        options[random_b][0] = options[random_b][0].title()

        options[random_l][0] = options[random_l][0].replace(blacklistedWord, '')
        options[random_l][0] = options[random_l][0].title()

        options[random_d][0] = options[random_d][0].replace(blacklistedWord, '')
        options[random_d][0] = options[random_d][0].title()

        options[random_s][0] = options[random_s][0].replace(blacklistedWord, '')
        options[random_s][0] = options[random_s][0].title()

    vegetarianMeal = {
            'breakfast': {
                'title': options[random_b][0],
                'calories': int(options[random_b][1]),
                'image': options[random_b][2]
            },
            'lunch': {
                'title': options[random_l][0],
                'calories': int(options[random_l][1]),
                'image': options[random_l][2]
            },
            'dinner': {
                'title': options[random_d][0],
                'calories': int(options[random_d][1]),
                'image': options[random_d][2]
            },
            'snack': {
                'title': options[random_s][0],
                'calories': int(options[random_s][1]),
                'image': options[random_s][2]
            }
    }
    
    return vegetarianMeal

def paleoDiet(calories_wanted: 'int') -> {}:
    min = (calories_wanted // 4) - 20
    max = (calories_wanted // 4) + 20

    range = str(min) + '-' + str(max)
    try:
        response = requests.get(
            url,
            params={'q': '',                # Word filter, blank gets all.
                    'calories': range,  # Calorie range, can also be an exact int.
                    'health': 'paleo',      # Health is basically "diet type"
                    'diet': 'balanced',     # Balanced makes sure the call gets real food.
                    'from': 0,              # With queries that have many hits from - to
                    'to': 20,               # returns the results in that range.
                    'app_id': user,         
                    'app_key': key}
        )

        data = response.json()
    except:
        return {}

    options = {}
    index = 0

    for x in data['hits']:
        options[index] = [x['recipe']['label'], x['recipe']['calories']/x['recipe']['yield'], x['recipe']['image']]
        index = index + 1

    randomNums = set()
    while len(randomNums) is not 4:
        randomNums.add(randint(0, len(options) - 1))

    random_b = randomNums.pop()
    random_l = randomNums.pop()
    random_d = randomNums.pop()
    random_s = randomNums.pop()

    #Remove blacklisted words
    blacklist = ['recipes', 'recipe']
    for blacklistedWord in blacklist:
        options[random_b][0] = options[random_b][0].replace(blacklistedWord, '')
        options[random_b][0] = options[random_b][0].title()

        options[random_l][0] = options[random_l][0].replace(blacklistedWord, '')
        options[random_l][0] = options[random_l][0].title()

        options[random_d][0] = options[random_d][0].replace(blacklistedWord, '')
        options[random_d][0] = options[random_d][0].title()

        options[random_s][0] = options[random_s][0].replace(blacklistedWord, '')
        options[random_s][0] = options[random_s][0].title()

    paleoMeal = {
            'breakfast': {
                'title': options[random_b][0],
                'calories': int(options[random_b][1]),
                'image': options[random_b][2]
            },
            'lunch': {
                'title': options[random_l][0],
                'calories': int(options[random_l][1]),
                'image': options[random_l][2]
            },
            'dinner': {
                'title': options[random_d][0],
                'calories': int(options[random_d][1]),
                'image': options[random_d][2]
            },
            'snack': {
                'title': options[random_s][0],
                'calories': int(options[random_s][1]),
                'image': options[random_s][2]
            }
    }
    
    return paleoMeal

def ketoDiet(calories_wanted: 'int') -> {}:
    min = (calories_wanted // 4) - 20
    max = (calories_wanted // 4) + 20

    range = str(min) + '-' + str(max)
    try:
        response = requests.get(
            url,
            params={'q': '',                # Word filter, blank gets all.
                    'calories': range,  # Calorie range, can also be an exact int.
                    #'health': 'paleo',      # Health is basically "diet type"
                    'diet': 'low-carb',     # Balanced makes sure the call gets real food.
                    'from': 0,              # With queries that have many hits from - to
                    'to': 20,               # returns the results in that range.
                    'app_id': user,         
                    'app_key': key}
        )

        data = response.json()
    except:
        return {}

    options = {}
    index = 0

    for x in data['hits']:
        options[index] = [x['recipe']['label'], x['recipe']['calories']/x['recipe']['yield'], x['recipe']['image']]
        index = index + 1

    randomNums = set()
    while len(randomNums) is not 4:
        randomNums.add(randint(0, len(options) - 1))

    random_b = randomNums.pop()
    random_l = randomNums.pop()
    random_d = randomNums.pop()
    random_s = randomNums.pop()

    #Remove blacklisted words
    blacklist = ['recipes', 'recipe']
    for blacklistedWord in blacklist:
        options[random_b][0] = options[random_b][0].replace(blacklistedWord, '')
        options[random_b][0] = options[random_b][0].title()

        options[random_l][0] = options[random_l][0].replace(blacklistedWord, '')
        options[random_l][0] = options[random_l][0].title()

        options[random_d][0] = options[random_d][0].replace(blacklistedWord, '')
        options[random_d][0] = options[random_d][0].title()

        options[random_s][0] = options[random_s][0].replace(blacklistedWord, '')
        options[random_s][0] = options[random_s][0].title()

    ketoMeal = {
            'breakfast': {
                'title': options[random_b][0],
                'calories': int(options[random_b][1]),
                'image': options[random_b][2]
            },
            'lunch': {
                'title': options[random_l][0],
                'calories': int(options[random_l][1]),
                'image': options[random_l][2]
            },
            'dinner': {
                'title': options[random_d][0],
                'calories': int(options[random_d][1]),
                'image': options[random_d][2]
            },
            'snack': {
                'title': options[random_s][0],
                'calories': int(options[random_s][1]),
                'image': options[random_s][2]
            }
    }
    
    return ketoMeal



