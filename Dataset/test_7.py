import godclass_7_c as G
import godclass_7_c_RGC as RG
import godclass_7_s_RGC_E as RGE
import longmethod_7_c as L
import longmethod_7_c_RLM as RLM
import longmethod_7_s_RLM_E as RME
import featureenvy_7_c as F
import featureenvy_7_c_RFE as RFE
import featureenvy_7_s_RFE_E as RFE_E

import featureenvy_7_s_E as E1
import longmethod_7_s_E as E2
import featureenvy_7_s_E as E3

test_cases = [
    {
        "start": "A",
        "end": "B",
        "cost": 2
    },
    {
        "start": "B",
        "end": "C",
        "cost": 5
    },
]

implementations = [
    ("G.CostAlgorithm", G),
   # ("RG.CostAlgorithm", RG),
  #   ("RGE.CostAlgorithm", RGE),
    ("L.CostAlgorithm", L), 
    ("RLM.CostAlgorithm", RLM),
    ("RME.CostAlgorithm", RME),
    ("F.CostAlgorithm", F),
    ("RFE.CostAlgorithm", RFE),
    ("RFE_E.CostAlgorithm", RFE_E),
    ("Energy", E1),("Energy 2", E2),("Energy", E3),

]

def run_tests():
    for impl_name, impl_class in implementations:
        print(f"Testing implementation from {impl_name}")
        instance = impl_class.CostAlgorithm()

        functions = getattr(instance,"get_node_manager",None)
        if functions:
            nm = instance.get_node_manager()
            for case in test_cases:
                nm.add_node(case["start"], case["end"], case["cost"])
            
            for case in test_cases:
                start, end = case["start"], case["end"]
                expected_cost = case["cost"]

                # Testing find_cost
                actual_cost = nm.find_cost(start, end)
                assert actual_cost == expected_cost, f"Failed on find_cost for {start} to {end}: Expected {expected_cost}, got {actual_cost}"
                
                # Testing print_path_cost
                actual_print = instance.print_path_cost(start, end)
                assert str(expected_cost) in actual_print, f"Failed on print_path_cost for {start} to {end}: Expected print containing {expected_cost}, got {actual_print}"

        else:
            # Set up nodes based on test cases
            for case in test_cases:
                instance.add_node(case["start"], case["end"], case["cost"])
            
            for case in test_cases:
                start, end = case["start"], case["end"]
                expected_cost = case["cost"]

                # Testing find_cost
                actual_cost = instance.find_cost(start, end)
                assert actual_cost == expected_cost, f"Failed on find_cost for {start} to {end}: Expected {expected_cost}, got {actual_cost}"
                
                # Testing print_path_cost
                actual_print = instance.print_path_cost(start, end)
                assert str(expected_cost) in actual_print, f"Failed on print_path_cost for {start} to {end}: Expected print containing {expected_cost}, got {actual_print}"

        print(f"Passed all tests for {impl_name}")

if __name__ == "__main__":
    run_tests()
