import godclass_8_c as GodClass_S
import godclass_8_s_RGC as GodClass_RGC
import godclass_8_s_RGC_E as GodClass_RGC_E
import longmethod_8_c as LongMethod_S
import longmethod_8_s_RLM as LongMethod_RLM
import longmethod_8_s_RLM_E as LongMethod_RLM_E
import featureenvy_8_c as FeatureEnvy_S
import featureenvy_8_s_RFE as FeatureEnvy_RFE
import featureenvy_8_s_RFE_E as FeatureEnvy_RFE_E

import featureenvy_8_s_E as E1
import longmethod_8_s_E as E2
import featureenvy_8_s_E as E3

def run_tests(implementation, class_name):
    print(f'Testing {class_name} from {implementation.__name__}')
    
    user_alice = implementation.User("Alice")
    user_jon = implementation.User("Jon Pork")
    user_chris = implementation.User("Chris P Bacon")

    platform = implementation.SocialMediaPlatform()
    
    # Test: Alice can post a picture
    assert "posted" in platform.add_picture(user_alice, "Pic1") 
    
    # Test: Jon and Chris can like the picture
    assert "liked" in platform.add_like(user_chris, "Pic1") 
    assert "liked" in platform.add_like(user_jon, "Pic1") 

    # Test: Show total number of likes
    print(platform.show_total_likes(user_chris, "Pic1"))
    #assert "2" in platform.show_total_likes(user_chris, "Pic1")
    
    # Test: Jon can unlike, decreasing total likes
    assert "unliked" in platform.remove_like(user_jon, "Pic1") 

    # Test: Show updated total number of likes
    #assert "1" in 
    print(platform.show_total_likes(user_chris, "Pic1"))
    
    # Test: Show picture details 
    assert "Pic1" in platform.show_picture_details("Pic1")

# List of implementations to run tests on
implementations = [
 #   (GodClass_S, "GodClass_S"),
    (GodClass_RGC, "GodClass_RGC"),
    (GodClass_RGC_E, "GodClass_RGC_E"),
    #(LongMethod_S, "LongMethod_S"),
    #(LongMethod_RLM, "LongMethod_RLM"),
     (LongMethod_RLM_E, "LongMethod_RLM_E"),
    (FeatureEnvy_S, "FeatureEnvy_S"),
     (FeatureEnvy_RFE, "FeatureEnvy_RFE"),
     (FeatureEnvy_RFE_E, "FeatureEnvy_RFE_E"),
     (E1,"Energy"),(E2,"Energy"),(E3,"Energy")
]

# Execute all tests for each implementation
for implementation, class_name in implementations:
    run_tests(implementation, class_name)

print("All tests executed successfully.")
