# Define a Dog class
class Dog:
    # Method that makes the dog sound
    def make_sound(self):
        return "Bark"


# Define a Cat class
class Cat:
    # Method that makes the cat sound
    def make_sound(self):
        return "Meow"


# Function that works with any object that has a make_sound() method
def process_sound(sound_object):
    # Call the make_sound method of the object passed in
    sound = sound_object.make_sound()
    print("The animal makes sound:", sound)


# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Pass both objects to the same function
process_sound(dog)  # Output: The animal makes sound: Bark
process_sound(cat)  # Output: The animal makes sound: Meow
