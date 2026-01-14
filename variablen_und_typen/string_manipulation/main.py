grocery_items = "milk cheese bread apples oranges chicken"

# 1. String-Slicing nutzen, um die Items zu extrahieren
dairy1 = grocery_items[0:4]    # 'milk'
dairy2 = grocery_items[5:11]   # 'cheese'
bakery1 = grocery_items[12:17] # 'bread'

# 2. String-Konkatenation verwenden, um den Satz zu erstellen
print("We have dairy and bakery items: " + dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5")