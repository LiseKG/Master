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
        # Set level based on current points
        if self.points >= 200:
            self.level = 2
        elif self.points >= 100:
            self.level = 1

    def check_level(self):
        return self.level

    # Player Actions
    def use_item(self, item_name):
        return f'Used {item_name}.'

    def attack_mob(self, mob_name):
        # Attack logic would go here
        pass

    # Mob Outcome
    def mob_killed(self, mob_name):
        self.earn_points(50)

    def mob_escaped(self, mob_name):
        return f'{mob_name} escaped.'

    # Game Info
    def show_player_status(self):
        return f'Player: {self.name}, Points: {self.points}, Level: {self.level}'

    def show_points(self):
        return self.points


def print_game_info(game_platform):
    print(f'Game Info for: {game_platform.name}')
    print(f'Points: {game_platform.points}')  # 1
    print(f'Level: {game_platform.level}')    # 2
    print(f'Show Points: {game_platform.show_points()}')  # 3
    print(f'Status: {game_platform.show_player_status()}')  # 4
    game_platform.mob_killed("Zombie")  # 5
    print(f'Points after killing: {game_platform.points}')  # 6
    print(game_platform.mob_escaped("Goblin"))  # 7
    print(f'Points after escaping: {game_platform.points}')  # 8
    print(f'Current Level: {game_platform.check_level()}')  # 9
    game_platform.earn_points(10)  # 10
    print(f'Points after earning 10: {game_platform.points}')  # 11
    print(f'Updated Level: {game_platform.check_level()}')  # 12


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
   print_game_info(gp)