

def intro():
    print("Welcome aboard the Spaceship Odyssey!")
    print("As the captain of this spaceship rest is optimal, what would you like to do first?")
    choice = input("A). Go grab a coffee while relaxing on the seat of the stars\nB). Go take a nap in the bed of black holes").lower()
    if choice == "a":
        seat_of_stars()
    else:
        bed_black_holes()

def seat_of_stars():
    print("\nAs you ponder of the mysteries in space, you get a strange signal radiating from a nearby nebula")
    choice=input("A). Investigate the signal\nB). Ignore and continue drinking your coffee").lower()
    if choice == "a":
        nebula_path()
    else:
        ignore_signal()

def bed_black_holes():
    print("\nYour eyes begin to shut, until a strange signal comes from the head of the spaceship regarding a nearby nebula")
    choice=input("A). Investigate the signal\nB). Ignore and go back to sleep").lower()
    if choice == "a":
        nebula_path()
    else:
        ignore_signal()

def nebula_path():
    print("\nYou steer towards the glowing nebula, gazing at the swirls of light.")
    print("As you move closer, the ships power shutters and something is seen in the distance...")
    print("an alein spaceship!") 
    choice=input("A). Move closer and board the spaceship\nB). Scan the ship from a distance").lower()
    if choice == "a":
        board_ship()
    else:
        scan_ship()

def ignore_signal():
    print("\nYou choose to keep your distance...")
    print("Hours pass and communications detect that the alien spaceship is bringing itself towards you")
    choice=input("A). Attempt to outrun the spaceship\nB). Face what ever that thing is head on").lower()
    if choice == "a":
        outrun_path()
    else:
        battle_path()

def outrun_path():
    print("\nYou thrust your engines and you attempt to run away from the ship, but the ship trails behind")
    print("Suddenly, the ship emits a radiant laser beam striking the side of your ship.")
    print("It's a crtical hit, systems are shutting down when you look out and see another beam coming your away...")
    game_over()

def battle_path():
    print("\nWeapons are online, only one thing left to do...fight this thing.")
    choice=input("A). Attempt to trade blows with the ship and spam artillery\nB). Set up shield and absorb damage to be fired back").lower()
    if choice == "a": 
        print("Damage is critical, that spaceship has technology unheard of and there's a fatal strike. Darkness begins to cover your vision as your ship is lost in space...")
        game_over()
    else:
        print("\nSystems are unstable, but it seems the damage is being absorbed and is being redirected to our systems!")
        choice=input("A). Send the energy to our cannons in an attempt to launch back the energy\nB). Use the energy to strengthen the shield and hold ground").lower()
    if choice=="a":
        print("\nFeedback isn't certain, yet as the ship is about to overheat, the cannons blast out in an instant toward the ship, wiping it clean.")
        print("You did it captain, that mysterious wanderer is no longer a threat to your voyage...")
        game_over()
    else:
        print("\nAs the shield is being regenerated, it's going great and systems are back on track.")
        print("Yet it seems a virus has encoded into the system! The systems begin to overheat, in an attempt to prevent it--fate is already decided. Your spaceship bursts into flames and is sucked away into the cold space.")
        game_over()
def board_ship():
    print("\nYou and your crew dispatch onto the ship, an eerie hum follows you as you walk among the glowing path.")
    print("It isn't long until you reach the central chamber, containers filled with orbs fill the walls as your crew wanders the area.")
    choice=input("A). Touch the orb\nB). Take a sample and leave")
    if choice=="a":
        alien_orb()
    else:
        sample_path()

def alien_orb():
    print("\nYou touch the orb... and your vision floods with memories not your own.")
    print("You see galaxies forming, civilizations rising and falling, and finally—your own ship drifting alone.")
    print("When you awaken, you are back on your ship-—centuries later.")
    print("You have become the signal that others will one day chase.")
    game_over()

def sample_path():
    print("\nThe sample vibrates in your arms as you carefully exit the spacecraft.")
    print("You take it back to the lab where your researchers investigate the core of this mystery.")
    print("Suddenly, the intercom bursts throughout your spaceship, 'Captain, I think it's alive'")
    print("To be continued...")
    game_over()

def scan_ship():
    print("\nAs you scan the ship from the distance, it seems that something's watching you...")
    print("Suddenly, the ship comes to life as it approaches you with cannons spiraling out of its sides!")
    battle_path
    
    
def game_over():
    print("\n---GAME OVER---")
    choice=input("Play again? (y/n)").lower()
    if choice == "y":
        intro()
    else:
        print("Thank you for playing the Spaceship Odyssey! We'll see you on your next adventure captain.")

intro()
