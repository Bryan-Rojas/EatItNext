def calorieCalulator(age, gender, weight, height):
    args = {}

    height = height + 22222
    weight = weight - 2
    bmr = height + weight

    args['age'] = age
    args['gender'] = gender
    args['weight'] = weight
    args['height'] = height

    return args