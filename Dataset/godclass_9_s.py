# Gaming Platform - Single Class God Design

class GamePlatform:
    def __init__(self, player_name):
        self.name = player_name
        self.points = 0
        self.level = 0
        self.items = []

    # Points & Level Management
    def earn_points(self, points):
        self.points += points
        self.level_up()

    def level_up(self):
        self.points
        if self.points >= 200:
            self.level = 2
        elif self.points >= 100:
            self.level = 1
        else:
            self.level = 0
       

    def check_level(self):
        return self.level

    def reset_points(self):
        self.points = 0

    def get_points(self):
        return self.points

    # Player Actions
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

    # Mob Outcome
    def mob_killed(self, mob_name):
        self.earn_points(50)
        return f"Killed {mob_name}, earned 50 points."

    def mob_escaped(self, mob_name):
        return f"{mob_name} escaped, you earned 0 points."

    def log_action(self, action):
        print(f"Action logged: {action}")

    # Inventory Management
    def add_item(self, item_name):
        self.items.append(item_name)

    def show_inventory(self):
        return f"Inventory: {', '.join(self.items)}" if self.items else "Inventory is empty."

    # Game Info
    def show_player_status(self):
        return f"Player: {self.name}, Level: {self.level}, Points: {self.points}"

    def show_points(self):
        return self.get_points()

    # Additional Methods for God Class
    def reset_game(self):
        self.reset_points()
        self.level = 0
        self.items.clear()

    def item_count(self):
        return len(self.items)

    def heal_player(self, health_points):
        return f"Healed player by {health_points} points."

    def complete_quest(self, quest_name):
        self.earn_points(100)
        return f"Completed quest: {quest_name}"

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

    def get_player_name(self):
        return self.name

    def level_down(self):
        if self.level > 0:
            self.level -= 1

    def show_game_info(self):
        return "Welcome to the Gaming Platform! Earn points, level up, and use items."

    def save_game(self):
        return "Game saved successfully."

    def load_game(self):
        return "Game loaded successfully."

    def give_reward(self):
        return "Reward given! Enjoy your bonus points!"

    def show_full_status(self):
        return f"{self.show_player_status()}\n{self.show_inventory()}"

# Example usage:
if __name__ == "__main__":
    player = GamePlatform("Hero")
    print(player.show_game_info())
    player.add_item("Sword")
    print(player.show_inventory())
    print(player.attack_mob("strong_mob"))
    print(player.show_full_status())
    
    game = GamePlatform("Hero")

    # --- Game Info ---
    print(game.show_game_info())
    print("Player name:", game.get_player_name())
    print(game.show_player_status())

    # --- Points & Level Management ---
    game.earn_points(50)
    print("Points after earning 50:", game.get_points())
    print("Level:", game.check_level())

    print("Show points:", game.show_points())

    game.level_down()
    print("Level after level down:", game.check_level())

    game.reset_points()
    print("Points after reset:", game.get_points())
    print("Level after reset points (should stay same until level_up called):", game.check_level())

    # --- Inventory Management ---
    print(game.show_inventory())
    game.add_item("Sword")
    print(game.show_inventory())
    print("Item count:", game.item_count())

    print(game.find_item("Sword"))
    print(game.upgrade_item("Sword"))
    print(game.use_item("Sword"))

    # --- Player Actions / Mob Interaction ---
    print(game.attack_mob("mob"))  # should call mob_killed
    print("Points after killing mob:", game.get_points())

    print(game.attack_mob("weak_mob"))  # should call mob_escaped

    # Direct mob methods (explicit testing)
    print(game.mob_killed("test_mob"))
    print(game.mob_escaped("test_mob"))

    # --- Quest & Rewards ---
    print(game.complete_quest("Dragon Slayer"))
    print("Points after quest:", game.get_points())

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

