def matching(n):
    match(n):
        case 1:
            return "Monday"
        case _:
            return"invalid "
print(matching(2))



# List of animals with their type and additional feature
animals = [
    {"name": "Lion", "type": "mammal", "has_fur": True},
    {"name": "Eagle", "type": "bird", "can_fly": True},
    {"name": "Crocodile", "type": "reptile", "is_carnivorous": True},
    {"name": "Frog", "type": "amphibian", "can_swim": True},
    {"name": "Penguin", "type": "bird", "can_fly": False}
]

# Function to classify animals
def classify_animal(animal):
    match animal["type"]:
        case "mammal":
            if animal.get("has_fur"):
                return f"{animal['name']} is a furry mammal."
            else:
                return f"{animal['name']} is a mammal without fur."
        
        case "bird":
            if animal.get("can_fly"):
                return f"{animal['name']} is a flying bird."
            else:
                return f"{animal['name']} is a bird that cannot fly."
        
        case "reptile":
            if animal.get("is_carnivorous"):
                return f"{animal['name']} is a carnivorous reptile."
            else:
                return f"{animal['name']} is a non-carnivorous reptile."
        
        case "amphibian":
            if animal.get("can_swim"):
                return f"{animal['name']} is an amphibian that can swim."
            else:
                return f"{animal['name']} is an amphibian that cannot swim."

        case _:
            return f"{animal['name']}'s type is unknown."

# Iterate through the list of animals and classify each one
for animal in animals:
    print(classify_animal(animal))


