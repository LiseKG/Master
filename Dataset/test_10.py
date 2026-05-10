# Importing implementations
from godclass_10_c import MovieStreamingPlatform as GodClassSimple
from godclass_10_c_RGC import MovieStreamingPlatform as GodClassRGC
from godclass_10_s_RGC_E import MovieStreamingPlatform as GodClassRGC_E
from longmethod_10_c import MovieStreamingPlatform as LongMethodSimple
from longmethod_10_c_RLM import MovieStreamingPlatform as LongMethodRLM
from longmethod_10_s_RLM_E import MovieStreamingPlatform as LongMethodRLM_E
from featureenvy_10_c import MovieStreamingPlatform as FeatureEnvySimple
from featureenvy_10_c_RFE import MovieStreamingPlatform as FeatureEnvyRFE
from featureenvy_10_s_RFE_E import MovieStreamingPlatform as FeatureEnvyRFE_E

from featureenvy_10_s_E import MovieStreamingPlatform as E1
from longmethod_10_s_E import MovieStreamingPlatform as E2
from featureenvy_10_s_E import MovieStreamingPlatform as E3

# List of all implementations
implementations = [
     ("GodClassSimple", GodClassSimple),
 #  ("GodClassRGC", GodClassRGC),
    ("GodClassRGC_E", GodClassRGC_E),
    ("LongMethodSimple", LongMethodSimple),
    ("LongMethodRLM", LongMethodRLM),
    ("LongMethodRLM_E", LongMethodRLM_E),
    ("FeatureEnvySimple", FeatureEnvySimple),
     ("FeatureEnvyRFE", FeatureEnvyRFE),
     ("FeatureEnvyRFE_E", FeatureEnvyRFE_E),
        ("Energy",E1),
        ("Energy",E2),
        ("Energy",E3),
 ]

def run_tests(MovieStreamingPlatform, platform_name):
    print(f"Testing {platform_name} implementation...")

    # Initialize platform
    platform = MovieStreamingPlatform("Alice")
    
    # Test 1: List available movies - initially should be empty
    print(platform.list_movies() )
    assert platform.list_movies() == [], "Test 1 Failed: Expected empty movie list."
    
    # Test 2: Add movies
    platform.add_movies("Barbie", "1 hour and 54 min", "PG-13")
    platform.add_movies("The Lion King", "1 hour and 28 min", "G")
    platform.add_movies("Inception", "2 hours and 28 min", "PG-13")
    
    # Check if all movies are saved
    assert len(platform.list_movies()) == 3, "Test 2 Failed: Expected 3 movies saved."
    
    # Check if the specific movies were added correctly
    if isinstance(platform.list_movies()[0],dict):
        assert "Barbie" in platform.list_movies()[0]["title"], "Test 2 Failed: Barbie not found in movie list."
        assert "The Lion King" in platform.list_movies()[1]["title"], "Test 2 Failed: The Lion King not found in movie list."
        assert "Inception" in platform.list_movies()[2]["title"], "Test 2 Failed: Inception not found in movie list."
    else:
        print(platform.list_movies())
        for element in platform.list_movies():
            if isinstance(element,object):
              #  assert any("Barbie" in element.title for element in platform.list_movies())
               continue
               # assert any("The Lion King" in element.title for element in platform.list_movies())
                #assert any("Inception" in element.title for element in platform.list_movies())
            else:
                assert "Barbie" in platform.list_movies()
                assert "The Lion King" in platform.list_movies()
                assert "Inception" in platform.list_movies()
            
    # Test 3: Rent a movie
    rent = platform.rent_movie("Barbie")
    print(rent)
    assert "barbie" in rent.lower() and "rented" in rent, "Test 3 Failed: Rental message incorrect."
    
    # Test 4: Get movie info
    movie_info = platform.get_movie_info("Barbie")
    print(movie_info)
    assert "1 hour and 54 min" in movie_info and "PG-13" in movie_info, "Test 4 Failed: Movie info not correct."
    
    # Test 5: List rented movies
    rented_movies = platform.get_rented_movies()
    assert "Barbie" in rented_movies, "Test 5 Failed: Rented movies list incorrect."
    
    print(f"{platform_name} implementation passed all tests.\n")

# Running all tests
for platform_name, platform_class in implementations:
    run_tests(platform_class, platform_name)
