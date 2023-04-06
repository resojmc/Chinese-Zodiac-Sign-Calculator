#Imports tkinter module as tk
import tkinter as tk

#Tkinter Gui main elements
root = tk.Tk()
root.geometry("300x600")
root.title("Zodiac Calculator")

def find_zodiac(year):
    #Function that takes a given year and determines zodiac
    rat = range(1912, 2044, 12)
    ox = range(1913, 2045, 12)
    tiger = range(1914, 2046, 12)
    rabbit = range(1915, 2047, 12)
    dragon = range(1916, 2048, 12)
    snake = range(1917, 2049, 12)
    horse = range(1918, 2050, 12)
    sheep = range(1919, 2051, 12)
    monkey = range(1920, 2052, 12)
    rooster = range(1921, 2053, 12)
    dog = range(1922, 2054, 12)
    pig = range(1923, 2055, 12)

    if year in rat:
        rat = "Rat 🐀 is your animal!"
        return rat
    
    if year in ox:
        ox = "Ox 🐂 is your animal!"
        return ox
    
    if year in tiger:
        tiger = "Tiger 🐅 is your animal!"
        return tiger
    
    if year in rabbit:
        rabbit = "Rabbit 🐇 is your animal!"
        return rabbit
    
    if year in dragon:
        dragon = "Dragon 🐉 is your animal!"
        return dragon
    
    if year in snake:
        snake = "Snake 🐍 is your animal!"
        return snake
    
    if year in horse:
        horse = "Horse 🐎 is your animal!"
        return horse
    
    if year in sheep:
        sheep = "Sheep 🐑 is your animal!"
        return sheep
    
    if year in monkey:
        monkey = "Monkey 🐒 is your animal!"
        return monkey
    
    if year in rooster:
        rooster = "Rooster 🐓 is your animal!"
        return rooster
    
    if year in dog:
        dog = "Dog 🐕 is your animal!"
        return dog
    
    if year in pig:
        pig = "Pig 🐖 is your animal!"
        return pig
    
    else:
        error = "Invalid Entry, Birth Years 1912 - 2043 Only."
        return error

def update_zodiac():
    #Executes main function and updates results
    year = int(top_entry.get())
    result = find_zodiac(year)
    result_label.config(text=f"{result}")

#Tkinter Gui Structure
top_label = tk.Label(root, text="Enter Birth Year")
top_label.pack()
top_entry = tk.Entry(root, )
top_entry.pack()
button = tk.Button(root, text="Go", command=update_zodiac)
button.pack()
result_label = tk.Label(root, text="Result: ")
result_label.pack()

#Executes main loop
root.mainloop()