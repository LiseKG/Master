class GamePlatform:
    def __init__(self, player_name):
        self.name = player_name
        self.points = 0
        self.level = 0

    # Points & Level Management
    def earn_points(self, points):
        self.points += points
        self._level_up()

    def _level_up(self):
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
        # Placeholder for attack logic
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
    print_basic_statistics(game_platform)
    mob_outcome_info(game_platform, "Zombie")
    print(f'Current Level: {game_platform.check_level()}')
    
    game_platform.earn_points(10)
    print(f'Points after earning 10: {game_platform.points}')
    print(f'Updated Level: {game_platform.check_level()}')

def print_basic_statistics(game_platform):
    print(f'Game Info for: {game_platform.name}')
    print(f'Points: {game_platform.points}')
    print(f'Level: {game_platform.level}')
    print(f'Show Points: {game_platform.show_points()}')
    print(f'Status: {game_platform.show_player_status()}')

def mob_outcome_info(game_platform, mob_name):
    game_platform.mob_killed(mob_name)
    print(f'Mob killed: {mob_name}')
    print(f'Points after killing: {game_platform.points}')
    print(f'Mob escaped: {game_platform.mob_escaped("Goblin")}')
    print(f'Points after escaping: {game_platform.points}')

if __name__ == '__main__':
    gp = GamePlatform("Gamer")
    gp.earn_points(150)
    gp.check_level()
    gp.use_item("health potion")
    gp.attack_mob("Goblin")
    gp.mob_killed("Goblin")
    gp.mob_escaped("Goblin")
    print(gp.show_player_status())
    print(gp.show_points())
    print_game_info(gp)
