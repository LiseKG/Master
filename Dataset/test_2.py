import godclass_2_c as Reviewer1
import godclass_2_c_RGC as Reviewer2

import longmethod_2_c as Reviewer4
import longmethod_2_c_RLM as Reviewer5

import featureenvy_2_c as Reviewer7
import featureenvy_2_c_RFE as Reviewer8



# List of implementations to test
implementations = [
    (Reviewer1, 'godclass_2_s'),
    (Reviewer2, 'godclass_2_RGC'),
 #   (Reviewer3, 'godclass_2_RGC_E'),
    (Reviewer4, 'longmethod_2_s'),
    (Reviewer5, 'longmethod_2_RLM'),
  #  (Reviewer6, 'longmethod_2_RLM_E'),
    (Reviewer7, 'featureenvy_2_s'),
    (Reviewer8, 'featureenvy_2_RFE'),
   # (Reviewer9, 'featureenvy_2_RFE_E'),
  
]

# Test each implementation
for implementation, name in implementations:
    print(f"Testing {name}...")
    
    # Instantiate classes
    product = implementation.Product("Banana", 0.5)
    user = implementation.User("Alice",200)
    cart = implementation.Cart()
    shop = implementation.Shop()

    # Test Product
    prodoutput = product.get_info()
    assert "Banana" in prodoutput and "0.5" in prodoutput, f"Failed Product Test in {name}"

    # Test Cart
    cart.add(product)
    assert cart  # We assume adding product does not return anything but modifies cart state

    # Test User buying a product
    user.buy(product)
    receipt = implementation.Receipt(user, product)

    # Test Shop process
    shop.process(user, product)

    # Test Receipt
    output = receipt.show()
    assert "Banana" in output and "0.5" in output, f"Failed Receipt Test in {name}"

print("All tests completed successfully.")
