
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

    # Points & Level Management
    def earn_points(self, points):
        self.points = self.points + points

    def level_up(self):
        if self.points >= 100:
            self.level = 1
            print("Level 1")
        if self.points >= 200:
            self.level = 2
            print("Level 2")

    def check_level(self):
        return self.level

    # Player Actions
    def use_item(self, item_name):
        return "used " + item_name

    def attack_mob(self, mob_name):
        return "attacking " + mob_name

    # Mob Outcome
    def mob_killed(self, mob_name):
        self.points = self.points + 50

    def mob_escaped(self, mob_name):
        return mob_name + " escaped"

    # Game Info
    def show_player_status(self):
        return self.name + " | Points: " + str(self.points) + " | Level: " + str(self.level)

    def show_points(self):
        return self.points


def process_game_session(player_name, actions):
    name = player_name
    points = 0
    level = 0
    log = []

    points = points + 0
    level = level + 0
    log.append("Session started for " + name)

    action_count = len(actions)
    index = 0
    result = ""

    while index < action_count:
        current_action = actions[index]
        action_type = current_action[0]

        if action_type == "earn":
            earned = current_action[1]
            points = points + earned
            result = name + " earned " + str(earned) + " points"
            log.append(result)
            if points >= 100:
                level = 1
                log.append("Level updated to 1")
            if points >= 200:
                level = 2
                log.append("Level updated to 2")
            if points >= 300:
                level = 3
                log.append("Level updated to 3")

        if action_type == "kill":
            mob = current_action[1]
            points = points + 50
            result = name + " killed " + mob
            log.append(result)
            if points >= 100:
                level = 1
                log.append("Level updated to 1")
            if points >= 200:
                level = 2
                log.append("Level updated to 2")
            if points >= 300:
                level = 3
                log.append("Level updated to 3")

        if action_type == "escape":
            mob = current_action[1]
            result = mob + " escaped"
            log.append(result)
            if points >= 100:
                level = 1
                log.append("Level checked at 1")
            if points >= 200:
                level = 2
                log.append("Level checked at 2")

        if action_type == "item":
            item = current_action[1]
            result = "used " + item
            log.append(result)
            if points >= 100:
                level = 1
                log.append("Level rechecked at 1")
            if points >= 200:
                level = 2
                log.append("Level rechecked at 2")

        if action_type == "status":
            result = name + " | Points: " + str(points) + " | Level: " + str(level)
            log.append(result)
            if points >= 100:
                level = 1
                log.append("Level confirmed at 1")
            if points >= 200:
                level = 2
                log.append("Level confirmed at 2")
            if points >= 300:
                level = 3
                log.append("Level confirmed at 3")

        index = index + 1

    final_status = name + " finished with " + str(points) + " points at level " + str(level)
    log.append(final_status)
    return log

if __name__ == "__main__":
    game = GamePlatform("Alice")

    game.earn_points(100)
    game.level_up()
    print(game.check_level())
    print(game.use_item("Sword"))
    print(game.attack_mob("Goblin"))
    game.mob_killed("Goblin")
    print(game.mob_escaped("Dragon"))
    print(game.show_player_status())
    print(game.show_points())

    actions = [
        ("earn", 100),
        ("kill", "Orc"),
        ("escape", "Troll"),
        ("item", "Potion"),
        ("status",),
    ]
    result = process_game_session("Alice", actions)
    for line in result:
        print(line)

