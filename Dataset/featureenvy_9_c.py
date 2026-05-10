
# Gaming Platform - Single Class God Design

# Requirements:
# - Player earns points to level up
# - 100 points → Level 1, 200 points → Level 2
# - Player can use items
# - Player can attack mobs
# - Killing a mob gives 50 points
# - Escaping mob gives 0 points


class GamePlatform:
    def __init__(self, player_name):
        self.name = player_name
        self.points = 0
        self.level = 0
        self.actions = []

    def earn_points(self, points):
        self.points += points
        self.level_up()

    def level_up(self):
        new_level = self.points // 100
        if new_level > self.level:
            self.level = new_level
            print(f"Level {self.level}")

    def check_level(self):
        return self.level

    def use_item(self, item_name):
        return f"used {item_name}"

    def attack_mob(self, mob_name):
        return f"{self.name} attacks {mob_name}"

    def mob_killed(self, mob_name):
        self.earn_points(50)
        return f"{mob_name} killed"

    def mob_escaped(self, mob_name):
        return f"{mob_name} escaped"

    def show_player_status(self):
        print(f"{self.name} | Level: {self.level} | Points: {self.points}")

    def show_points(self):
        return self.points


def run_game_session(game, mobs, items):
    game.actions = []
    game.actions.append(game.attack_mob(mobs[0]))
    game.mob_killed(mobs[0])
    game.actions.append(game.use_item(items[0]))
    game.actions.append(game.attack_mob(mobs[1]))
    game.mob_escaped(mobs[1])
    game.actions.append(game.use_item(items[1]))
    game.actions.append(game.attack_mob(mobs[2]))
    game.mob_killed(mobs[2])
    game.show_player_status()
    print(f"Total actions: {len(game.actions)}")
    print(f"Points after session: {game.show_points()}")
    print(f"Level after session: {game.check_level()}")
    game.actions.append("session complete")
    print(f"Final actions log: {game.actions}")


if __name__ == "__main__":
    game = GamePlatform("Alice")

    game.earn_points(100)
    game.earn_points(100)
    print(game.check_level())
    print(game.use_item("Sword"))
    print(game.attack_mob("Goblin"))
    print(game.mob_killed("Goblin"))
    print(game.mob_escaped("Dragon"))
    game.show_player_status()
    print(game.show_points())

    run_game_session(game, ["Orc", "Troll", "Wolf"], ["Potion", "Shield"])



