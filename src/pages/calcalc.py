# age (years)
# gender - male, female (choices)
# weight (pounds)
# height (inches)
# activity_level - none, light, moderate, heavy, extreme (choices)
# goal - maintain, lose, gain (choices)
# gain_amount - 0, 1, 2 (pounds)

def calorieCalulator(age, gender, weight, height_ft, height_in, activity_level, goal):
    height = (height_ft * 12) + height_in
    
    args = {}

    args['age'] = age
    args['gender'] = gender
    args['weight'] = weight
    args['height_ft'] = height_ft
    args['height_in'] = height_in
    args['height'] = height
    args['activity_level'] = activity_level
    args['goal'] = goal

    if gender == 'Male':
        c1 = 66
        hm = 6.2 * height
        wm = 12.7 * weight
        am = 6.76 * age

    if gender == 'Female':
        c1 = 655.1
        hm = 4.35 * height
        wm = 4.7 * weight
        am = 4.7 * age

    bmr_result = c1 + hm + wm - am

    if activity_level == 'None':
        activity_level = 1.2 * bmr_result

    if activity_level == 'Light':
        activity_level = 1.375 * bmr_result

    if activity_level == 'Moderate':
        activity_level = 1.55 * bmr_result

    if activity_level == 'Heavy':
        activity_level = 1.725 * bmr_result

    if activity_level == 'Extreme':
        activity_level = 1.9 * bmr_result

    if goal == 'Lose':
        calories = activity_level - 500

    if goal == 'Gain':
        calories = activity_level + 500
        
    if goal == 'Gain Heavily':
        calories = activity_level + 1000

    args['calories'] = int(calories)

    return args