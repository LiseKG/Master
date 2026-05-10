import godclass_6_c as GCS
import godclass_6_c_RGC as GCS_RGC

import longmethod_6_c as LMS
import longmethod_6_c_RLM as LMS_RLM

import featureenvy_6_c as FES
import featureenvy_6_c_RFE as FES_RFE


import featureenvy_6_s_E as E1
import longmethod_6_s_E as E2
import featureenvy_6_s_E as E3

test_cases = [
    {
         "class": GCS, 
         "name": "Restaurant (GCS)"
     },
   
     
    {
        "class": LMS, 
        "name": "Restaurant (LMS)"
    },
    {
        "class": LMS_RLM, 
        "name": "Restaurant (LMS_RLM)"
    },
   
    {
        "class": FES, 
         "name": "Restaurant (FES)"
     },
    {
        "class": FES_RFE, 
        "name": "Restaurant (FES_RFE)"
    },
    
    {
        "class": E1, 
        "name": "Restaurant (FES_RFE_E)"
    },
    {
        "class": E2, 
        "name": "Restaurant (FES_RFE_E)"
    },
    {
        "class": E3, 
        "name": "Restaurant (FES_RFE_E)"
    },
]

# Testing Ramen order scenario
def test_ramen_order(imp):
    customer = imp.Customer("John")
    restaurant = imp.Restaurant("Ramen Shop")
    
    order_result = restaurant.take_order(customer, "Ramen")
    print(order_result)
    assert "Ramen" in order_result  and ("order" in order_result or "Order" in order_result), f"Failed on {restaurant_class.__name__} while taking order"
    
    functions = getattr(restaurant,"cook_food",None)
    if functions:
        cook_result = restaurant.cook_food("Ramen")
        assert "ramen" and "cook" in cook_result.lower(), f"Failed on {restaurant_class.__name__} while cooking food"
    
        deliver_result = restaurant.deliver_food(customer, "Ramen")
        assert "Ramen" in deliver_result and "John" in deliver_result, f"Failed on {restaurant_class.__name__} while delivering food"
    else:
        kitchen = imp.Kitchen()
        cook_result = kitchen.cook_food("Ramen")
        assert "ramen" and "cook" in cook_result.lower(), f"Failed on {restaurant_class.__name__} while cooking food"

        delivery = imp.Delivery()
        deliver_result = delivery.deliver_food(customer, "Ramen")
        assert "Ramen" in deliver_result and "John" in deliver_result, f"Failed on {restaurant_class.__name__} while delivering food"
    

    print(f"Successful test on {imp.Restaurant.__name__}")

# Run tests for all restaurant implementations
for test_case in test_cases:
    print(f"Testing {test_case['name']}...")
    test_ramen_order(test_case['class'])
