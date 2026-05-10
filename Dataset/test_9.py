import godclass_9_c as GodClass

import longmethod_9_c as LongMethod
import featureenvy_9_c as FeatureEnvy
import longmethod_9_s_RLM as LongMethodRLM
import longmethod_9_s_RLM_E as LongMethodRLM_E
import godclass_9_s_RGC as GodClassRGC
import godclass_9_s_RGC_E as GodClassRGC_E
import featureenvy_9_s_RFE as FeatureEnvyRFE
import featureenvy_9_s_RFE_E as FeatureEnvyRFE_E

import featureenvy_9_s_E as E1
import longmethod_9_s_E as E2
import featureenvy_9_s_E as E3

def run_tests(implementation):
    print(f"Testing {implementation.__name__}")
    
    GP = implementation.GamePlatform('TestPlayer')
    Player = implementation.Player("jon")

    #functions = getattr(implementation,"Player",None)
    functions = False

    if functions:
        player = GP.player
        player.earn_points(150)
    
        # Test level check
        
        assert player.check_level() == 1, "Level check should return the current level."
        ga = implementation.GameActions(player)
        # Test use_item functionality
        item_usage = ga.use_item("Health Potion")
        assert "Health Potion" in item_usage and "used" in item_usage.lower(), "Should state that the item was used."

        # Test attack_mob functionality
        ga.attack_mob("Goblin")
        
        # Test mob killed functionality
        ga.mob_killed("Goblin")
        assert player.check_level() == 2, "Points should increase by 50 after killing a mob."

        # Test mob escaped functionality
        escape_message = ga.mob_escaped("Orc")
        assert "escaped" in escape_message, "Should state that mob escaped."

        # Test player status and points
        status = GP.show_player_status()
        points = GP.show_points()
        assert points == player.points, "Should return the total points."

    else:
        # Test earn_points and level_up
        GP.register_player(Player)
        GP.earn_points(150)
    
        # Test level check
       
        print(GP.check_level())
        
        assert GP.check_level() == 1, "Level check should return the current level."

        # Test use_item functionality
        item_usage = GP.use_item("Health Potion")
        #assert "Health Potion" in item_usage and "used" in item_usage.lower(), "Should state that the item was used."

        # Test attack_mob functionality
        GP.attack_mob("Goblin")
        
        # Test mob killed functionality
        GP.mob_killed("Goblin")
        #assert GP.check_level() == 2, "Points should increase by 50 after killing a mob."

        # Test mob escaped functionality
        escape_message = GP.mob_escaped("Orc")
        assert "escaped" in escape_message, "Should state that mob escaped."

        # Test player status and points
        status = GP.show_player_status()
        points = GP.show_points()
        assert points == GP.points, "Should return the total points."

# List of implementations to test
implementations = [
   GodClass,
 LongMethod,
  FeatureEnvy,
LongMethodRLM,
    LongMethodRLM_E,
    GodClassRGC,
    GodClassRGC_E,
     FeatureEnvyRFE,
    FeatureEnvyRFE_E,
    E1,E2,E3,
]

# Execute tests against all implementations
for impl in implementations:
    run_tests(impl)
