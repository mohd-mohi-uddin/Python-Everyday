>> What is OOP?

Imagine you're making a game.

The game has:

Players
Enemies
Cars
Dogs

Instead of storing everything in separate variables...

player_name = "Asim"
player_health = 100
player_level = 5

You can group everything into one object.

Think of it like this:

Player

Inside the box:

Name = Asim
Health = 100
Level = 5

That box is called an Object.

>>What is a Class?

A class is a blueprint.

Think about building houses.

Blueprint:

Bedroom
Kitchen
Bathroom

Actual houses:

House 1

2 Bedrooms
Owner = Ali

House 2

3 Bedrooms
Owner = Asim

The blueprint stays the same.

The houses are different.

Exactly like Python.

Class
   ↓
Objects
First Class
class Dog:
    pass

Explanation

class

means

I am creating a blueprint.

Dog

is the class name.

pass

means

Do nothing for now.

>> Making an Object
class Dog:
    pass

dog1 = Dog()

Read it like English.

Dog()

Create one Dog.

Store it inside

dog1

Now

dog1

is an object.

Another one

dog2 = Dog()

Now we have

Dog Class

↓

dog1
dog2

Both came from the same blueprint.

>> Objects Can Store Data

Let's give every dog a name.

class Dog:
    pass

dog1 = Dog()

dog1.name = "Tommy"

Now

dog1

name = Tommy

You can print it.

print(dog1.name)

Output

Tommy

Another object

dog2 = Dog()

dog2.name = "Bruno"

Now

dog1

name = Tommy

dog2

name = Bruno

Same blueprint.

Different data.

Multiple Variables
dog1.name = "Tommy"
dog1.age = 3
dog1.color = "Brown"

Now dog1 contains

Name
Age
Color

Print

print(dog1.name)
print(dog1.age)
print(dog1.color)

Output

Tommy
3
Brown
Problem

Imagine making 100 dogs.

dog1.name = ...
dog1.age = ...

dog2.name = ...
dog2.age = ...

dog3.name = ...
dog3.age = ...

Very repetitive.

Python has a better way.

>> __init__

This is the most important part of OOP.

class Dog:

    def __init__(self):
        print("A dog is created")

Now

dog1 = Dog()

Output

A dog is created

Every time you make an object...

Python automatically runs __init__.

You don't call it yourself.

Python does.

Think of __init__ as:

"Whenever someone creates a new object, run this code first."

Why self?

This is the biggest beginner confusion.

Don't memorize it.

Understand it.

Imagine two dogs.

dog1

dog2

When Python executes

dog1 = Dog()

it secretly does something like

Dog(dog1)

When

dog2 = Dog()

Python internally thinks

Dog(dog2)

That object is received by

self

So

self

means

THIS object.
Example
class Dog:

    def __init__(self):
        print(self)
dog1 = Dog()
dog2 = Dog()

Output

<Dog object>

<Dog object>

Different addresses.

Different objects.

Saving Data Using self

Instead of writing

dog1.name = "Tommy"

we do

class Dog:

    def __init__(self):
        self.name = "Tommy"

Now

dog1 = Dog()

print(dog1.name)

Output

Tommy
Passing Values

Instead of fixing every dog's name to Tommy...

class Dog:

    def __init__(self, name):
        self.name = name

Create dogs.

dog1 = Dog("Tommy")

dog2 = Dog("Bruno")

Python does

dog1

↓

self = dog1

name = Tommy

Then

dog2

↓

self = dog2

name = Bruno

So

print(dog1.name)
Tommy
print(dog2.name)
Bruno
Multiple Parameters
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

Create

dog1 = Dog("Tommy", 3)

dog2 = Dog("Bruno", 5)

Print

print(dog1.name)
print(dog1.age)

print(dog2.name)
print(dog2.age)

Output

Tommy
3

Bruno
5
What are Methods?

Functions inside a class are called methods.

Example

class Dog:

    def bark(self):
        print("Woof!")

Use it

dog1 = Dog()

dog1.bark()

Output

Woof!

>> Methods Can Use Object Data
class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")
dog1 = Dog("Tommy")

dog1.bark()

Output

Tommy says Woof!

Notice how bark() knows the dog's name because it accesses self.name.

>> Everything Together
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

dog1 = Dog("Tommy", 3)

dog1.bark()
dog1.birthday()

Output

Tommy says Woof!
Tommy is now 4 years old!
The Trick to Understanding OOP

Whenever you see a class, ask yourself two questions:

What data should each object have?
Store it as attributes using self.attribute inside __init__.
What actions should each object be able to perform?
Write them as methods