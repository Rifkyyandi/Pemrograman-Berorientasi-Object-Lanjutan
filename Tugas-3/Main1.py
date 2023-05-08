from playsound import playsound

# define a dictionary with animal names and their sound files
animal_sounds = {
    "lion": "lion.wav",
    "elephant": "elephant.wav",
    "tiger": "tiger.wav",
    "dog": "dog.wav",
    "cat": "cat.wav",
    "chimpanzee": "chimpanzee.wav",
    "cow": "cow.wav",
    "pig": "pig.wav",
    "duck": "duck.wav",
    "fox": "fox.wav"
}

# play the sound of the animal with the given name
def play_animal_sound(animal_name):
    sound_file = animal_sounds.get(animal_name)
    if sound_file:
        playsound(sound_file)
    else:
        print("Sound file not found for animal:", animal_name)

# main program loop
while True:
    # ask the user to input an animal name
    animal_name = input("Enter an animal name (or 'exit' to quit): ")
    if animal_name == "exit":
        break
    else:
        play_animal_sound(animal_name.lower())