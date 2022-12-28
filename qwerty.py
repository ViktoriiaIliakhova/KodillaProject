product_dictionary = {
    "bakery": ["bread", "donuts", "buns"],
    "grocery_store": ["carrot", "celery", "arugula"]
}
for key, val in product_dictionary.items():
    val = [i.title() for i in val]
    print(f"I am going to {key.capitalize()} and buy there {val}.")
    
print("Total number of products:")
print(sum([len(product_dictionary[val]) for val in product_dictionary]))
