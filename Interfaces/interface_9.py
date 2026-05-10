
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
        pass
    
    def level_up(self):
    	#add points and level up if needed
        #if points more than 100 then lvl print lvl 1, change self.level to 1, 200 then lvl 2 so on
        pass

    def check_level(self):
        pass
        #return an int - level

    # Player Actions
    def use_item(self, item_name):
        pass
        #return a string saying used item_name

    def attack_mob(self, mob_name):
        pass

    # Mob Outcome
    def mob_killed(self, mob_name):
        pass
        #increase 50 points

    def mob_escaped(self, mob_name):
        pass
        #return a string saying mob escaped

    # Game Info
    def show_player_status(self):
        pass

    def show_points(self):
        pass
        #return number of points


