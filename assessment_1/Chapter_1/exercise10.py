# Creating a dictionary with film details
film = {
    "Title": "Oppenheimer",
    "Director": "Christopher Nolan",
    "Year": 2023,
    "Genre": "Documentary, Action, History, Thriller, Mystery",
}

# Displaying film details using a loop
print("Film Details:")
for key, value in film.items():
    print(f"{key}: {value}")