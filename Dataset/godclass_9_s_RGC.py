class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.points = 0
        self.level = 0

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

    def level_down(self):
        if self.level > 0:
            self.level -= 1

    def check_level(self):
        return self.level

    def reset_points(self):
        self.points = 0

    def get_points(self):
        return self.points


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        self.items.append(item_name)

    def show_inventory(self):
        return f"Inventory: {', '.join(self.items)}" if self.items else "Inventory is empty."

    def item_count(self):
        return len(self.items)

    def find_item(self, item_name):
        if item_name in self.items:
            return f"{item_name} found."
        else:
            return f"{item_name} not found."

    def upgrade_item(self, item_name):
        if item_name in self.items:
            return f"Upgraded {item_name}."
        else:
            return f"{item_name} not found in inventory."


class GameActions:
    def __init__(self, player):
        self.player = player

    def use_item(self, item_name):
        return f"Used {item_name}"

    def attack_mob(self, mob_name):
        outcome = self.decide_outcome(mob_name)
        return outcome

    def decide_outcome(self, mob_name):
        if mob_name == "strong_mob":
            return self.mob_killed(mob_name)
        else:
            return self.mob_escaped(mob_name)

    def mob_killed(self, mob_name):
        self.player.earn_points(50)
        return f"Killed {mob_name}, earned 50 points."

    def mob_escaped(self, mob_name):
        return f"{mob_name} escaped, you earned 0 points."


class GamePlatform:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.inventory = Inventory()
        self.actions = GameActions(self.player)

    def reset_game(self):
        self.player.reset_points()
        self.player.level = 0
        self.inventory.items.clear()

    def show_player_status(self):
        return f"Player: {self.player.name}, Level: {self.player.level}, Points: {self.player.points}"

    def show_points(self):
        return self.player.get_points()

    def show_game_info(self):
        return "Welcome to the Gaming Platform! Earn points, level up, and use items."

    def show_full_status(self):
        return f"{self.show_player_status()}\n{self.inventory.show_inventory()}"

    def add_item(self, item_name):
        self.inventory.add_item(item_name)

    def complete_quest(self, quest_name):
        self.player.earn_points(100)
        return f"Completed quest: {quest_name}"

    def heal_player(self, health_points):
        return f"Healed player by {health_points} points."

    def log_action(self, action):
        print(f"Action logged: {action}")

    def save_game(self):
        return "Game saved successfully."

    def load_game(self):
        return "Game loaded successfully."

    def give_reward(self):
        return "Reward given! Enjoy your bonus points."


# Example usage:
if __name__ == "__main__":
    player = GamePlatform("Hero")
    print(player.show_game_info())
    player.add_item("Sword")
    print(player.inventory.show_inventory())
    print(player.actions.attack_mob("strong_mob"))
    print(player.show_full_status())
    
    game = GamePlatform("Hero")

    # --- Game Info ---
    print(game.show_game_info())
    print("Player name:", game.player.name)
    print(game.show_player_status())

    # --- Points & Level Management ---
    game.player.earn_points(50)
    print("Points after earning 50:", game.player.get_points())
    print("Level:", game.player.check_level())

    print("Show points:", game.show_points())

    game.player.level_down()
    print("Level after level down:", game.player.check_level())

    game.player.reset_points()
    print("Points after reset:", game.player.get_points())
    print("Level after reset points (should stay same until level_up called):", game.player.check_level())

    # --- Inventory Management ---
    print(game.inventory.show_inventory())
    game.add_item("Sword")
    print(game.inventory.show_inventory())
    print("Item count:", game.inventory.item_count())

    print(game.inventory.find_item("Sword"))
    print(game.inventory.upgrade_item("Sword"))
    print(game.actions.use_item("Sword"))

    # --- Player Actions / Mob Interaction ---
    print(game.actions.attack_mob("mob"))  # should call mob_killed
    print("Points after killing mob:", game.player.get_points())

    print(game.actions.attack_mob("weak_mob"))  # should call mob_escaped

    # Direct mob methods (explicit testing)
    print(game.actions.mob_killed("test_mob"))
    print(game.actions.mob_escaped("test_mob"))

    # --- Quest & Rewards ---
    print(game.complete_quest("Dragon Slayer"))
    print("Points after quest:", game.player.get_points())

    print(game.give_reward())

    # --- Healing ---
    print(game.heal_player(30))

    # --- Logging ---
    game.log_action("Player attacked a mob")

    # --- Save / Load ---
    print(game.save_game())
    print(game.load_game())

    # --- Full Status ---
    print(game.show_full_status())

    # --- Reset Game ---
    game.reset_game()
    print("After full reset:")
    print(game.show_full_status())
