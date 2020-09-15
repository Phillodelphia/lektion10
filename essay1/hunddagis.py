class Dog_daycare:
    dogs = name = boss = "" 
    daycare = []

    def __init__(self, name, boss):
        self.name = name
        self.boss = boss
        self.dogs = []
        self.daycare.append(self)
    
    def select_daycare(self, name):
        for i in self.daycare:
            if i.name == name:
                return i

    def select_dog(self, name):
        for i in self.dogs:
            if(i.name == name):
                return i

        print("I'm sorry we don't know any dogs that goes by that name...")
        return False

    def get_dogs(self):
        for i in self.dogs:
            print(f"{i.name}, {i.age} ,{i.race}")

    def add_dog(self, Dog):
        self.dogs.append(Dog)
    
    def execute_dog(self, Dog):
        for i in self.dogs:
            if(i.name == Dog.name):
                index = self.dogs.index(i)
                self.dogs.pop(index)

    def set_boss_name(self, boss):
        self.boss = boss

class Dog:
    bestFriend = name = age = owner = race = favoriteToy = ""
    

    def __init__(self, name, age, race, owner):
        self.name = name
        self.age = age
        self.race = (race.lower()).replace(" ", "")
        self.owner = owner
        self.bestFriend = []

    def set_name(self, name):
        self.name = name 

    def set_age(self, age):
        self.age = age

    def set_owner(self, owner):
        self.owner = owner
    
    def add_favorite_toy(self, toy):
        self.favoriteToy = toy

    def add_best_friend(self, Dog):
        if (len(self.bestFriend) <= 0 or self.race == "goldenretriever"):
            self.bestFriend.append(Dog)

    def get_best_friend(self):
        for i in self.bestFriend:
            print(i.name)
daycare = Dog_daycare("Vacker Tass", "Tasspi")

dog1 = Dog("Test1", "5", "goldenretriever", "yourname")
dog2 = Dog("Test2", "3", "corgi", "yourname2")
dog3 = Dog("Test3", "10", "goldenretriever", "yourname3")

daycare.add_dog(dog1)
daycare.add_dog(dog2)
daycare.add_dog(dog3)

command = ""

while command != "EXIT": 
    print(f"----Welcome to {daycare.name} owned by our lord {daycare.boss}----")
    print(
    f'''
    1.adddog add a dog!
    2.seldog select a dog!
    3.list view all dogs!
    4.swboss switch manager!
    5.swdaycare switch current daycare!
    6.ccare create new daycare!
    '''
    
    )
    command = input(f"What can we help you with?").upper()

    if command == "ADDDOG" or command == "1":
        name = input("What is your dogs name?")
        age = input("How old is it?")
        race = input("What race is it?")
        owner = input("And finally what is your name?")
        myDog = Dog(name, age, race, owner)
        daycare.add_dog(myDog)
        print(f"----------Thank you for the dog {myDog.owner}!------------")

    elif command == "SELDOG" or command == "2":
        name = input("Which dog do you want to choose?")
        myDog = daycare.select_dog(name)
        
        while myDog:
            print(f"You have selected {myDog.name}!")
            print(f'''
        1.petdog pet the dog!
        2.info information about current dog.
        3.rmdog remove dog.
        4.dogname change {myDog.name}'s name!
        5.toy assign favorite toy!
        6.swowner assign new owner!
        7.friend befriend another dog!
        8.checkfriend check current dog's friends!
            '''
            )
            command = input("What do you want to do?").upper()
            if command == "PETDOG" or command == "1":
                print("You petted the dog!")

            elif command == "INFO" or command == "2":
                print(
                    f'''
                    name: {myDog.name}
                    age: {myDog.age}
                    race: {myDog.race}
                    favorite toy: {myDog.favoriteToy}
                    owner: {myDog.owner} 
                    '''
                )

            elif command == "RMDOG" or command == "3":
                print(f"-----------Removing {myDog.name}-------------")
                daycare.execute_dog(myDog)
                myDog = False

            elif command == "DOGNAME" or command == "4":
                newName = input("What is the dog's new name?")
                myDog.set_name(newName)

            elif command == "TOY" or command == "5":
                toy = input("What is the dog's favorite toy?")
                myDog.add_favorite_toy(toy)

            elif command == "SWOWNER" or command == "6":
                owner = input("Who is the new owner?")
                myDog.set_owner(owner)
            elif command == "FRIEND" or command == "7":
                friend = input("Which dog do you want to befriend?")
                dogFriend = daycare.select_dog(friend)

                myDog.add_best_friend(dogFriend)
                dogFriend.add_best_friend(myDog)

            elif command == "CHECKFRIEND" or command == "8":
                print("-----These are your dog's friends!-----")
                myDog.get_best_friend()
                print("---------------------------------------")

            else:
                myDog = False

    elif command == "LIST" or command == "3":
        print("---------------------------------------------------")
        daycare.get_dogs()
        print("---------------------------------------------------")
        

    elif command == "SWBOSS" or command == "4":
        name = input("Who is the new boss?")
        daycare.set_boss_name(name)
        print(f"The new boss here is now {daycare.boss}")
    
    elif command == "SWDAYCARE" or command == "5":
        name = input("Which daycare do you want to switch to?")
        daycare = daycare.select_daycare(name)
    
    elif command == "CCARE" or command == "6":
        name = input("What is the name of your new daycare?")
        owner = input("Who is the owner?")
        Dog_daycare(name, owner)

