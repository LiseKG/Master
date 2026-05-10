import godclass_3_c as Reviewer1
import godclass_3_c_RGC as Reviewer2
#import godclass_3_c_RGC_E as Reviewer3
import longmethod_3_c as Reviewer4
import longmethod_3_c_RLM as Reviewer5
#import longmethod_3_c_RLM_E as Reviewer6
#import featureenvy_3_c as Reviewer7
#import featureenvy_3_c_RFE as Reviewer8

test_cases = [
     {
         "class": Reviewer1,
         "name": "godclass_3_s"
     },
  
 
     {
         "class": Reviewer4,
         "name": "longmethod_3_s"
     },
     {
         "class": Reviewer5,
         "name": "longmethod_3_c_RLM"
     },
  
    # {
    #     "class": Reviewer7,
    #     "name": "featureenvy_3_s"
    # },
   # {
    #    "class": Reviewer8,
     #   "name": "featureenvy_3_c_RFE"
    #},
 
    
]

def run_tests():
    for test in test_cases:
        print(f"Running tests for {test['name']}")
        navigation_system = test["class"].NavigationSystem()
        user = test["class"].User("test_user")
        home_location = test["class"].Location("Home")
        work_location = test["class"].Location("Work")
        
        user.save_place("home", home_location)
        user.save_place("work", work_location)

        # Test navigate
        destination = test["class"].Location("Park")
        navigation_system.navigate(home_location, destination)
        
        # Test alternatives
        alternatives = navigation_system.get_alternatives(home_location, destination)
        
        if isinstance(alternatives,dict):
            alternatives = " ".join(alternatives)
            alternatives = "".join(alternatives)
        if isinstance(alternatives,list):
            alternatives = "".join(alternatives)
        print(alternatives,"her")
        assert "highway" in alternatives and "without" or "avoiding" or "non-highway" or "Scenic" in alternatives or "non-highway" in alternatives[1]

        # Test arrival time
        #arrival_time = navigation_system.get_arrival_time(0,0)
        #print(arrival_time)

        # Test go to saved
        #navigation_system.go_to_saved(user, "home")
        # Check saved locations
        
        

if __name__ == "__main__":
    run_tests()
