def recommend(age, interest):

    data = {
        "technology": ["Learn Python", "Build AI Projects", "Web Development Course"],
        "sports": ["Join Gym", "Play Football", "Yoga Training"],
        "music": ["Guitar Classes", "Piano Lessons", "Music Production"],
        "art": ["Painting Course", "Graphic Design", "Photography"]
    }

    interest = interest.lower()

    if interest in data:
        return data[interest]

    return ["No recommendations found"]