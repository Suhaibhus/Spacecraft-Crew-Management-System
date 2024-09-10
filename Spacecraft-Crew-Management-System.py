class Crew:
    '''
Purpose: Setting the roles, status, location and names of the crew. 
Instance variables: name: the name of the crew members
                    status:the status of the crew member
                    location: the location of the crew member
Methods:move:Moves the crew members to location
        repair: shows a message that the memeber doesnt know how to do that
        first_aid: shows a message that the memeber doesnt know how to do that
        fire_lasers: shows a message that the memeber doesnt know how to do that

        

'''


    def __init__(self, name):
        self.name = name
        self.status = 'Active'
        self.location = 'Sleep Pods'
    
    def __repr__(self):
        return (f'{self.name} : {self.status}, at {self.location}')
    def move(self, location):
        list = ["Bridge", "Medbay", "Engine", "Lasers", "Sleep Pods"]
        if location in list:
            self.location = location 
        else:
            print('Not a valid location.')
    def repair(self, ship):
        print(f"{self.name} doesn't know how to do that.")      
    def first_aid(self, ship):
        print(f"{self.name} doesn't know how to do that.")
    def fire_lasers(self, ship, target_ship, target_location):
        print(f"{self.name} doesn't know how to do that.")

if __name__ == '__main__':
    crew0 = Crew('Ava')
    print(crew0.name) #Ava
    print(crew0.status) #Active
    print(crew0.location) #Sleep Pods
    print(crew0) #Ava : Active, at Sleep Pods
 
import random
class Starship:
    '''
Purpose: To represent a teams starship in the game. 

Instance variables: name: the name of the crew members
                    crew_list :the crew list
                    damaged: the location of the crew member

Methods:  encounter: Represents a game/ encounter between 2 starship. 
'''

    def __init__(self, name, crew_list):
        self.name = name
        self.crew_list = crew_list
        self.damaged = {'Bridge':False, 'Medbay':False, 'Engine':False, 'Lasers':False, 'Sleep Pods':False}

    def encounter(self, enemy_ship):
        print("Welcome to STARSHIPS")
        input("Your Player 1, Press Enter to begin: ")
        print(f"{self.name} vs {enemy_ship.name}. Lets see whos the stronger ship!")

        for crew_mem in self.crew_list:
            if crew_mem.status == "Injured":
                print(f"{crew_mem.name} is injured, no move will allowed")
                print(f"{self.name} didnt move")
            else: 
                check_choice = False
                while not check_choice:
                    # choice = input("Pick your next move wisely, 'move' or 'nothing': ")
                    # if choice.lower() == 'move':
                        choice_of_move = {'Bridge', 'Medbay', 'Engine', 'Lasers', 'Sleep Pods'}
                        location_move = input(f"Where do you want to move? {choice_of_move} pick one:  ")
                        if location_move in choice_of_move:
                            crew_mem.move(location_move)
                            print(f"Move was succesful, {crew_mem.name} has moved to {location_move}")
                            check_choice = True

                        else:
                            print("Error, Not a valid location")
                    # elif choice.lower() == 'nothing':
                    #     print(f"Nothing was succesful, {crew_mem.name} has done nothing")
                    #     check_choice = True

                        # else: 
                        #     print("invalid location, try again.")
         #enemy
        for crew_mem in enemy_ship.crew_list:
            if crew_mem.status == "Injured":
                print(f"{crew_mem.name} is injured, no move will allowed")
                print(f"{self.name} no move")
            else: 
                # enemy_choice = random.choice(['move', 'nothing'])
                # if enemy_choice == 'move':
                    choice_of_move = random.choice(['Bridge', 'Medbay', 'Engine', 'Lasers', 'Sleep Pods'])
                    crew_mem.move(choice_of_move)
                    print(f"Enemy: {crew_mem.name} moved to {choice_of_move}")
                # else:
                #     print(f"Enemy: {crew_mem.name} has done nothing")
                


if __name__ == '__main__':
    crew1 = Crew('Sakshi')
    crew2 = Crew('Jina')
    crew3 = Crew('Daniel')
    space_boat = Starship('Ebon Hawk', [crew1, crew2, crew3])

        
    enemy_crew1 = Crew('Alex')
    enemy_crew2 = Crew('Bob')
    enemy_crew3 = Crew('Charlie')
    enemy_space_boat = Starship('Nebula', [enemy_crew1, enemy_crew2, enemy_crew3])

    space_boat.encounter(enemy_space_boat)
    print(space_boat.name) #Ebon Hawk
    print(space_boat.crew_list) #[Sakshi : Active, at Sleep Pods, Jina: Active, at Sleep Pods, Daniel : Active, at Sleep Pods]
    print(space_boat.damaged) #{'Bridge': False, 'Medbay': False,'Engine': False, 'Lasers': False, 'Sleep Pods': False}
if __name__ == '__main__':
    crew1 = Crew('Sakshi')
    crew2 = Crew('Jina')
    crew3 = Crew('Daniel')
    space_boat = Starship('Ebon Hawk', [crew1, crew2, crew3])
    print(space_boat.name) #Ebon Hawk
    print(space_boat.crew_list) #[Sakshi : Active, at Sleep Pods, Jina: Active, at Sleep Pods, Daniel : Active, at Sleep Pods]
    print(space_boat.damaged) #{'Bridge': False, 'Medbay': False, 'Engine': False, 'Lasers': False, 'Sleep Pods': False}
    crew1.move('Dungeon') #Not a valid location.
    print(crew1.location) #Sleep Pods
    crew1.move('Engine')
    print(crew1.location) #Engine
    crew2.repair(space_boat) #Jina doesn't know how to do that.
    crew3.first_aid(space_boat) #Daniel doesn't know how to do that.
    crew2.fire_lasers(space_boat, space_boat, "Engine") #Jina doesn't know how to do that.

class Engineer(Crew):
    '''
Purpose: Represent the Engineer of the crew 
Instance variables: No instance variable
Methods: repair: Repairs the ship if its damaged. 
'''
    def repair(self, ship):
        if ship.damaged[self.location]:
            ship.damaged[self.location] = False
            print(f"{self.name} fixed the damage to {self.location}.")
        else: 
            print(f"{self.location} isn't damaged.")


class Captain(Crew):
    '''
Purpose: Represent the captian of the crew 
Instance variables: No instance variable
Methods: fire_laser: Fires a laser at location
'''


    def fire_lasers(self, ship, target_ship, target_location):
        location = ["Bridge", "Medbay", "Engine", "Lasers", "Sleep Pods"]
        if target_location not in location:
            print("Not a valid location")
        elif self.location != "Bridge":
            print(f"{self.name} must be in the Bridge to fire lasers.")
        elif ship.damaged["Bridge"]:
            print(f"Bridge is too damaged to order lasers to be fired.")
        elif ship.damaged["Lasers"]:
            print(f"Lasers are too damaged to fire.")
        else:
            for crew_mem in target_ship.crew_list:
                if crew_mem.location == target_location:
                    crew_mem.status = "Injured"
            print(f"{ship.name} fires lasers at {target_ship.name}'s {target_location}.")
            target_ship.damaged[target_location] = True


class Doctor(Crew):
    '''
Purpose: Represent the Doctor of the crew 
Instance variables: medpacs: the medpacs the doctor has.
Methods: first_aid: heals the crew members when injured. 



'''

    def  __init__(self, name):
        Crew.__init__(self, name)
        self.medpacs = 3
    def first_aid(self, ship):
        if self.location == "Medbay":
                if ship.damaged["Medbay"] == False:
                    self.medpacs = 3 
                    print (f"{self.name}'s supply of medpacs has been replenished.")
                    for crew_mem in ship.crew_list:
                        if crew_mem.location == self.location and crew_mem.status == "Injured":
                            crew_mem.status = "Active"
                            print(f"{self.name} healed {crew_mem.name}'s injuries.")
                else:
                    print(f"{self.name} has no medpacs left.")
        elif self.medpacs == 0:
            print(f"{self.name} has no medpacs left.")
        else:
            self.medpacs -= 1
            for crew_mem in ship.crew_list:
                if crew_mem.location == self.location and crew_mem.status == "Injured":
                    crew_mem.status = "Active"
                    print(f"{self.name} healed {crew_mem.name}'s injuries.")

                



if __name__ == '__main__':
    engi1 = Engineer('Chris')
    print(isinstance(engi1, Crew)) #True
    cap1 = Captain('Emily')
    print(isinstance(cap1, Crew)) #True
    doc1 = Doctor('Audrey')
    print(isinstance(doc1, Crew)) #True
    print(doc1.medpacs) #3
    engi2 = Engineer('Mitali')
    engi2.move('Medbay')
    doc2 = Doctor('Jack')
    doc2.move('Bridge')
    cap2 = Captain('Andrew')
    engi3 = Engineer('Jess')
    doc3 = Doctor('Preston')
    cap3 = Captain('Abdul')
    cap3.move('Engine')
    ship1 = Starship('Voyager', [engi1, doc1, cap1])
    ship2 = Starship('Tempest', [engi2, doc2, cap2, engi3, doc3, cap3])
    cap1.fire_lasers(ship1, ship2, "Weak Point") #Not a valid location.
    cap1.fire_lasers(ship1, ship2, 'Medbay') #Emily must be in the Bridge to fire lasers.
    cap1.move('Bridge')
    cap1.fire_lasers(ship1, ship2, 'Sleep Pods') #Voyager fires lasers at Tempest's Sleep Pods.
    print(ship2.damaged) #{'Bridge': False, 'Medbay': False, 'Engine': False, 'Lasers': False, 'Sleep Pods': True}
    print(ship2.crew_list) #[Mitali : Active, at Medbay, Jack : Active, at Bridge, Andrew : Injured, at Sleep Pods, Jess : Injured, at Sleep Pods, Preston : Injured, at Sleep Pods, Abdul : Active, at Engine]
    engi2.move('Sleep Pods')
    engi2.first_aid(ship2) #Mitali doesn't know how to do that.
    engi2.repair(ship2) #Mitali fixed the damage to Sleep Pods.
    print(ship2.damaged) #{'Bridge': False, 'Medbay': False, 'Engine': False, 'Lasers': False, 'Sleep Pods': False}
    print(engi2) #Mitali : Active, at Sleep Pods
    doc2.move('Sleep Pods')
    doc2.first_aid(ship2) #Jack healed Andrew's injuries.
    #Jack healed Jess's injuries.
    #Jack healed Preston's injuries.
    print(ship2.crew_list) #[Mitali : Active, at Sleep Pods, Jack : Active, at Sleep Pods, Andrew : Active, at Sleep Pods, Jess : Active,  at Sleep Pods, Preston : Active, at Sleep Pods, Abdul : Active, atEngine]
    print(doc2.medpacs) #2
    doc2.first_aid(ship2)
    doc2.first_aid(ship2)
    print(doc2.medpacs) #0
    print(doc1.medpacs) #3
    doc2.first_aid(ship2) #Jack has no medpacs left.
    cap2.move('Medbay')
    cap1.fire_lasers(ship1, ship2, 'Medbay') #Voyager fires lasers at Tempest's Medbay.
    print(cap2) #Andrew : Injured, at Medbay
    print(ship2.damaged['Medbay']) #True
    doc2.move('Medbay')
    doc2.first_aid(ship2) #Jack has no medpacs left.
    print(doc2.medpacs) #0
    print(cap2) #Andrew : Injured, at Medbay
    engi3.repair(ship2) #Sleep Pods isn't damaged.
    engi3.move('Medbay')
    engi3.repair(ship2) #Jess fixed the damage to Medbay.
    doc2.first_aid(ship2) #Jack's supply of medpacs has been replenished.
    #Jack healed Andrew's injuries.
    print(doc2.medpacs) #3
    print(cap2) #Andrew : Active at Medbay
    doc2.first_aid(ship2) #Jack's supply of medpacs has been replenished.
    print(doc2.medpacs) #3
    cap3.move('Bridge')
    cap3.fire_lasers(ship2, ship1, 'Lasers') #Tempest fires lasers at Voyager's Lasers.
    cap1.fire_lasers(ship1, ship2, 'Engine') #Lasers are too damaged to fire.
    ship1.damaged['Bridge'] = True
    cap1.fire_lasers(ship1, ship2, 'Engine') #Bridge is too damaged to order lasers to be fired.








