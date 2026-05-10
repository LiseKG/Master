
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


def check_levels(points, level, log, verb, include_300):
    thresholds = [(100, "1"), (200, "2")] + ([(300, "3")] if include_300 else [])
    for threshold, label in thresholds:
        if points >= threshold:
            level = int(label)
            log.append("Level " + verb + " " + label)
    return level


def process_game_session(player_name, actions):
    name = player_name
    points = 0
    level = 0
    log = []
    log.append("Session started for " + name)

    for current_action in actions:
        action_type = current_action[0]
        if action_type == "earn":
            points = points + current_action[1]
            log.append(name + " earned " + str(current_action[1]) + " points")
            level = check_levels(points, level, log, "updated to", True)
        elif action_type == "kill":
            points = points + 50
            log.append(name + " killed " + current_action[1])
            level = check_levels(points, level, log, "updated to", True)
        elif action_type == "escape":
            log.append(current_action[1] + " escaped")
            level = check_levels(points, level, log, "checked at", False)
        elif action_type == "item":
            log.append("used " + current_action[1])
            level = check_levels(points, level, log, "rechecked at", False)
        elif action_type == "status":
            log.append(name + " | Points: " + str(points) + " | Level: " + str(level))
            level = check_levels(points, level, log, "confirmed at", True)

    log.append(name + " finished with " + str(points) + " points at level " + str(level))
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



