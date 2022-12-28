product_dictionary = {
    "bakery": ["bread", "donuts", "buns."],
    "grocery_store": ["carrot", "celery", "arugula."]
}
for key, val in product_dictionary.items():
    val = [i.title() for i in val]
    print(f'I am going to {key.capitalize()} and buy there {val}')
