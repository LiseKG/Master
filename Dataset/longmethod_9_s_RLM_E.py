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
    status = []
    for i in range(5):  
        game_platform.earn_points(10)
        status.append(game_platform.show_player_status())
        status.append(check_level_status(game_platform))

        game_platform.attack_mob("Goblin")
        status.append(f"Attacked Goblin. Points: {game_platform.points}")

        if i % 2 == 0:
            status.append(game_platform.mob_escaped("Orc"))
        else:
            game_platform.mob_killed("Orc")
            status.append(f"Killed Orc. Points: {game_platform.points}")

        status.append(f"Current status: {game_platform.show_player_status()}")
        status.append(additional_status_check(game_platform))

        if i >= 4:
            status.append("You've played enough for now!")

    return "\n".join(status)


def check_level_status(game_platform):
    if game_platform.points >= 200:
        return "Level 2 reached!"
    elif game_platform.points >= 100:
        return "Level 1 reached!"
    else:
        return "Keep playing to level up!"


def additional_status_check(game_platform):
    status = []
    if game_platform.level == 2:
        status.append("You're at the maximum level!")
    if game_platform.points > 300:
        status.append("You've got over 300 points!")
    elif game_platform.points < 100:
        status.append("Points are still low.")

    if game_platform.points == 250:
        status.append("Reward unlocked!")
    status.append("Even points!" if game_platform.points % 2 == 0 else "Odd points!")

    return "\n".join(status)


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
