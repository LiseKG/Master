class GamePlatform:
    def __init__(self, player_name):
        self.name = player_name
        self.points = 0
        self.level = 0

    # Points & Level Management
    def earn_points(self, points):
        self.points += points
        self.level_up()

    def level_up(self):
        if self.points >= 200:
            self.level = 2
        elif self.points >= 100:
            self.level = 1
        else:
            self.level = 0

    def check_level(self):
        return self.level

    # Player Actions
    def use_item(self, item_name):
        return f"Used {item_name}"

    def attack_mob(self, mob_name):
        self.mob_killed(mob_name)

    # Mob Outcome
    def mob_killed(self, mob_name):
        self.earn_points(50)


    def mob_escaped(self, mob_name):
        return f"{mob_name} escaped"

    # Game Info
    def show_player_status(self):
        return f"Player: {self.name}, Level: {self.level}, Points: {self.points}"

    def show_points(self):
        return self.points


def long_method_example(game_platform):
    status = ""
    for i in range(5):  # Loop to simulate multiple actions
        game_platform.earn_points(10)  # #1
        status += game_platform.show_player_status() + "\n"  # #2
        if game_platform.points >= 200:  # #3
            status += "Level 2 reached!\n"  # #4
        elif game_platform.points >= 100:  # #5
            status += "Level 1 reached!\n"  # #6
        else:  # #7
            status += "Keep playing to level up!\n"  # #8
            
        game_platform.attack_mob("Goblin")  # #9
        status += f"Attacked Goblin. Points: {game_platform.points}\n"  # #10
        
        if i % 2 == 0:  # #11
            status += game_platform.mob_escaped("Orc") + "\n"  # #12
        else:  # #13
            game_platform.mob_killed("Orc")  # #14
            status += f"Killed Orc. Points: {game_platform.points}\n"  # #15
            
        status += f"Current status: {game_platform.show_player_status()}\n"  # #16

        if game_platform.level == 2:  # #17
            status += "You're at the maximum level!\n"  # #18
        if game_platform.points > 300:  # #19
            status += "You've got over 300 points!\n"  # #20
        elif game_platform.points < 100:  # #21
            status += "Points are still low.\n"  # #22
        
        # More unnecessary logic just to fill lines
        if game_platform.points == 250:  # #23
            status += "Reward unlocked!\n"  # #24
        if game_platform.points % 2 == 0:  # #25
            status += "Even points!\n"  # #26
        else:  # #27
            status += "Odd points!\n"  # #28

        if i >= 4:  # #29
            status += "You've played enough for now!\n"  # #30

    return status  # #31


# Example of how to call the long method with an instance
if __name__ == '__main__':
   gp = GamePlatform("Gamer")
   gp.earn_points(150)
   gp.level_up()
   gp.check_level()
   gp.use_item("health potion")
   gp.attack_mob("Goblin")
   gp.mob_killed("Goblin")
   gp.mob_escaped("Goblin")
   gp.show_player_status()
   gp.show_points()
   print(long_method_example(gp))