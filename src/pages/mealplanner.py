from random import randint

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
    breakfastOptions = {}
    lunchOptions = {}
    dinnerOptions = {}
    snackOptions = {}

    breakfastOptions['Green Eggs & Ham'] = 700
    breakfastOptions['Waffles'] = 400
    breakfastOptions['Ham & Cheese Sandwich'] = 500
    breakfastOptions['Fruity Pebbles Cereal'] = 350
    lunchOptions['Chicken Strips'] = 700
    lunchOptions['Ramen'] = 400
    dinnerOptions['Chicken Alfredo'] = 800
    snackOptions['Fruit Roll Up'] = 250

    breakfastKeys = list(breakfastOptions.keys())

    randomBreakfastNum = randint(0, len(breakfastOptions)-1)
    randomBreakfastKey = breakfastKeys[randomBreakfastNum]

    anyMeal = {
            'breakfast': {
                'title': randomBreakfastKey,
                'calories': breakfastOptions[randomBreakfastKey]
            },
            'lunch': {
                'title': 'Mac and Cheese',
                'calories': 600
            },
            'dinner': {
                'title': 'Sirloin Steak',
                'calories': 1200
            },
            'snack': {
                'title': 'Me',
                'calories': 50000
            }
    }
    
    return anyMeal

def veganDiet(calories_wanted: 'int') -> {}:

    anyMeal = {
            'breakfast': {
                'title': 'Vegan Green Eggs & Ham',
                'calories': 700
            },
            'lunch': {
                'title': 'Vegan Mac and Cheese',
                'calories': 600
            },
            'dinner': {
                'title': 'Vegan Steak',
                'calories': 1200
            },
            'snack': {
                'title': 'Me',
                'calories': 50000
            }
    }
    
    return anyMeal

def vegetarianDiet(calories_wanted: 'int') -> {}:

    anyMeal = {
            'breakfast': {
                'title': 'Vegetarian Green Eggs & Ham',
                'calories': 700
            },
            'lunch': {
                'title': 'Mac and Cheese',
                'calories': 600
            },
            'dinner': {
                'title': 'Sirloin Steak',
                'calories': 1200
            },
            'snack': {
                'title': 'Me',
                'calories': 50000
            }
    }
    
    return anyMeal

def paleoDiet(calories_wanted: 'int') -> {}:

    anyMeal = {
            'breakfast': {
                'title': 'Paleo Green Eggs & Ham',
                'calories': 700
            },
            'lunch': {
                'title': 'Mac and Cheese',
                'calories': 600
            },
            'dinner': {
                'title': 'Sirloin Steak',
                'calories': 1200
            },
            'snack': {
                'title': 'Me',
                'calories': 50000
            }
    }
    
    return anyMeal

def ketoDiet(calories_wanted: 'int') -> {}:

    anyMeal = {
            'breakfast': {
                'title': 'Keto Green Eggs & Ham',
                'calories': 700
            },
            'lunch': {
                'title': 'Mac and Cheese',
                'calories': 600
            },
            'dinner': {
                'title': 'Sirloin Steak',
                'calories': 1200
            },
            'snack': {
                'title': 'Me',
                'calories': 50000
            }
    }
    
    return anyMeal


    anyMeal = {
            'breakfast': {
                'title': 'Green Eggs & Ham',
                'calories': 700
            },
            'lunch': {
                'title': 'Mac and Cheese',
                'calories': 600
            },
            'dinner': {
                'title': 'Sirloin Steak',
                'calories': 1200
            },
            'snack': {
                'title': 'Me',
                'calories': 50000
            }
    }
    
    return anyMeal



