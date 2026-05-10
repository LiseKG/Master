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
        game_platform.earn_points(10)
        status += game_platform.show_player_status() + "\n"
        status += check_level_status(game_platform)

        game_platform.attack_mob("Goblin")
        status += f"Attacked Goblin. Points: {game_platform.points}\n"

        if i % 2 == 0:
            status += game_platform.mob_escaped("Orc") + "\n"
        else:
            game_platform.mob_killed("Orc")
            status += f"Killed Orc. Points: {game_platform.points}\n"

        status += f"Current status: {game_platform.show_player_status()}\n"
        status += additional_status_check(game_platform)

        if i >= 4:
            status += "You've played enough for now!\n"

    return status


def check_level_status(game_platform):
    if game_platform.points >= 200:
        return "Level 2 reached!\n"
    elif game_platform.points >= 100:
        return "Level 1 reached!\n"
    else:
        return "Keep playing to level up!\n"


def additional_status_check(game_platform):
    status = ""
    if game_platform.level == 2:
        status += "You're at the maximum level!\n"
    if game_platform.points > 300:
        status += "You've got over 300 points!\n"
    elif game_platform.points < 100:
        status += "Points are still low.\n"

    if game_platform.points == 250:
        status += "Reward unlocked!\n"
    if game_platform.points % 2 == 0:
        status += "Even points!\n"
    else:
        status += "Odd points!\n"

    return status


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