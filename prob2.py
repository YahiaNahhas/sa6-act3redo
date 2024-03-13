#redo for sa6-act3 problem 2

fruit = ["Banana", "Apple", "Kiwi", "Coconut", "Cherry", "Watermelon", "Mango", "Blueberry", "Pear"]

new_fruit = sorted(fruit, key=lambda x: (len(x), x))

print(new_fruit)