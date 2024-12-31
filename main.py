print("\033[32mSTAR WARS NAME GENERATOR\033[0m")
print()
all = input("Enter your first name, last name, Mum's maiden name and the city you were born in: ").split()
print()
first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")
