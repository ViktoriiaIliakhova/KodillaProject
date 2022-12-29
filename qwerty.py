product_dictionary12 = {
    "bakery": ["cake", "donuts", "buns"],
    "grocery_store": ["tomato", "celery", "arugula"]
}
for key, val in product_dictionary12.items():
    val = [i.title() for i in val]
    print(f"I am going to {key.capitalize()} and buy there {val}.")
    
print("Total number of products:")
print(sum([len(product_dictionary12[val]) for val in product_dictionary12]))
