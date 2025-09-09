# List of names
names = ["Jasmine", "Namitha", "Adithyan", "Sravan", "Adhil"]

# Ask the user for input
choice = int(input("Enter a number (1 to 5): "))

# Check if input is valid
if 1 <= choice <= len(names):
    print("You selected:", names[choice - 1])
else:
    print("Invalid choice! Please enter a number between 1 and", len(names))
