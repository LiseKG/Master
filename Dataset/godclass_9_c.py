# Gaming Platform - God Class Design

# Requirements:
# - Player earns points to level up
# - 100 points -> Level 1, 200 points -> Level 2
# - Player can use items
# - Player can attack mobs
# - Killing a mob gives 50 points
# - Escaping mob gives 0 points


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.level = 0
        self.inventory = []
        self.kill_count = 0
        self.escape_count = 0


class Mob:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.alive = True


class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
        self.used = False


class GamePlatform:
    def __init__(self, player_name):
        self.name = player_name
        self.points = 0
        self.level = 0
        self.event_log = []
        self.active_player = None
        self.mob_roster = []
        self.leaderboard = []

    # Method 1
    def register_player(self, player: Player):
        self.active_player = player
        self.leaderboard.append(player)
        print(f"Player '{player.name}' registered.")

    # Method 2
    def log_event(self, message):
        self.event_log.append(message)

    # Method 3
    def earn_points(self, points):
        if self.active_player is None:
            print("No active player.")
            return
        self.active_player.points += points
        self.points = self.active_player.points
        self.level_up()

    # Method 4
    def level_up(self):
        if self.active_player is None:
            return
        new_level = self.active_player.points // 100
        if new_level > self.active_player.level:
            self.active_player.level = new_level
            self.level = new_level
            print(f"Level {new_level}")

    # Method 5
    def check_level(self):
        if self.active_player is None:
            return 0
        return self.active_player.level

    # Method 6
    def add_item_to_inventory(self, player: Player, item: Item):
        player.inventory.append(item)
        print(f"Item '{item.name}' added to {player.name}'s inventory.")

    # Method 7
    def use_item(self, item_name):
        if self.active_player is None:
            return f"No active player."
        for item in self.active_player.inventory:
            if item.name == item_name and not item.used:
                item.used = True
                print(f"used {item_name}")
                return f"used {item_name}"
        print(f"{item_name} not available.")
        return f"{item_name} not available."

    # Method 8
    def register_mob(self, mob: Mob):
        self.mob_roster.append(mob)
        print(f"Mob '{mob.name}' (difficulty: {mob.difficulty}) added to roster.")

    # Method 9
    def attack_mob(self, mob_name):
        for mob in self.mob_roster:
            if mob.name == mob_name and mob.alive:
                print(f"{self.name} attacks {mob_name}!")
                return mob
        print(f"Mob '{mob_name}' not found or already defeated.")
        return None

    # Method 10
    def mob_killed(self, mob_name):
        for mob in self.mob_roster:
            if mob.name == mob_name:
                mob.alive = False
                if self.active_player is not None:
                    self.active_player.kill_count += 1
                self.earn_points(50)
                print(f"{mob_name} killed")
                return f"{mob_name} killed"
        return f"{mob_name} not found."

    # Method 11
    def mob_escaped(self, mob_name):
        if self.active_player is not None:
            self.active_player.escape_count += 1
        print(f"{mob_name} escaped")
        return f"{mob_name} escaped"

    # Method 12
    def show_player_status(self):
        if self.active_player is None:
            print("No active player.")
            return
        p = self.active_player
        print(f"Player: {p.name} | Points: {p.points} | Level: {p.level} | Kills: {p.kill_count} | Escapes: {p.escape_count}")

    # Method 13
    def show_points(self):
        if self.active_player is None:
            return 0
        print(f"{self.active_player.name} has {self.active_player.points} point(s).")
        return self.active_player.points

    # Method 14
    def show_inventory(self, player: Player):
        if not player.inventory:
            print(f"{player.name}'s inventory is empty.")
            return []
        items = [item.name for item in player.inventory if not item.used]
        print(f"{player.name}'s inventory: {items}")
        return items

    # Method 15
    def show_mob_roster(self):
        print("Mob roster:")
        for mob in self.mob_roster:
            status = "alive" if mob.alive else "dead"
            print(f"  {mob.name} (difficulty: {mob.difficulty}) [{status}]")

    # Method 16
    def show_kills(self, player: Player):
        print(f"{player.name} has {player.kill_count} kill(s).")
        return player.kill_count

    # Method 17
    def show_escapes(self, player: Player):
        print(f"{player.name} has escaped {player.escape_count} time(s).")
        return player.escape_count

    # Method 18
    def reset_player_stats(self, player: Player):
        player.points = 0
        player.level = 0
        player.kill_count = 0
        player.escape_count = 0
        self.points = 0
        self.level = 0
        print(f"{player.name}'s stats have been reset.")

    # Method 19
    def show_event_log(self):
        print("Event log:")
        for entry in self.event_log:
            print(f"  {entry}")

    # Method 20
    def show_leaderboard(self):
        print("Leaderboard:")
        sorted_players = sorted(self.leaderboard, key=lambda p: p.points, reverse=True)
        for i, player in enumerate(sorted_players, 1):
            print(f"  {i}. {player.name} - {player.points} pts (Level {player.level})")

    # Method 21
    def award_bonus(self, player: Player, bonus_points):
        player.points += bonus_points
        self.points = player.points
        print(f"Bonus of {bonus_points} points awarded to {player.name}.")

    # Method 22
    def get_alive_mobs(self):
        alive = [mob.name for mob in self.mob_roster if mob.alive]
        print(f"Alive mobs: {alive}")
        return alive


if __name__ == "__main__":
    # All data objects created externally — receiving style
    platform = GamePlatform("GameSession")

    player = Player("Alice")
    sword = Item("Sword", "attack boost")
    potion = Item("Potion", "heal")
    goblin = Mob("Goblin", "easy")
    dragon = Mob("Dragon", "hard")
    troll = Mob("Troll", "medium")

    # Method 1 - register_player
    platform.register_player(player)

    # Method 6 - add_item_to_inventory
    platform.add_item_to_inventory(player, sword)
    platform.add_item_to_inventory(player, potion)

    # Method 8 - register_mob
    platform.register_mob(goblin)
    platform.register_mob(dragon)
    platform.register_mob(troll)

    # Method 7 - use_item
    platform.use_item("Sword")

    # Method 9 - attack_mob
    platform.attack_mob("Goblin")

    # Method 10 - mob_killed (calls earn_points -> level_up)
    platform.mob_killed("Goblin")
    platform.mob_killed("Dragon")
    platform.mob_killed("Troll")

    # Method 11 - mob_escaped
    platform.mob_escaped("Shadow Wolf")

    # Method 3 - earn_points (calls level_up)
    platform.earn_points(75)

    # Method 5 - check_level (standalone)
    print(f"Current level: {platform.check_level()}")

    # Method 12 - show_player_status (standalone)
    platform.show_player_status()

    # Method 13 - show_points (standalone)
    platform.show_points()

    # Method 14 - show_inventory (standalone)
    platform.show_inventory(player)

    # Method 15 - show_mob_roster (standalone)
    platform.show_mob_roster()

    # Method 16 - show_kills (standalone)
    platform.show_kills(player)

    # Method 17 - show_escapes (standalone)
    platform.show_escapes(player)

    # Method 21 - award_bonus (standalone)
    platform.award_bonus(player, 30)

    # Method 22 - get_alive_mobs (standalone)
    platform.get_alive_mobs()

    # Method 20 - show_leaderboard (standalone)
    platform.show_leaderboard()

    # Method 2 - log_event (standalone, called directly)
    platform.log_event("Game session completed.")

    # Method 19 - show_event_log (standalone)
    platform.show_event_log()

    # Method 18 - reset_player_stats (standalone)
    platform.reset_player_stats(player)
    platform.show_player_status()

    # Method 4 - level_up (called via earn_points above; also direct)
    platform.earn_points(100)
    platform.level_up()


