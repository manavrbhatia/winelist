import json

def main():
	print("Running Wine List 1.0.0")
	command = ""
	while command != "quit":
		print("~> ", end = " ")
		command = input()
		if command == "ls":
			dumpList(False, False)
		elif command == "ls -r":
			dumpList(False, True)
		elif command == "ls -f":
			dumpList(True, False)
		elif command == "rm -r":
			removeBottle(False)
		elif command == "rm -f":
			removeBottle(True)
		elif command == "add -f":
			addBottle(True)
		elif command == "add -r":
			addBottle(False)
		elif command == "quit":
			pass
		else:
			print("Incorrectly Formatted Command")

def removeBottle(fridge):
	deleteConfirm = ""
	with open('bottles.json') as f:
	  	json_object = json.load(f)
	if fridge:
		storageUnit = "fridge"
	else:
		storageUnit = "rack"

	print("Enter Bottle Location")
	print("~~ ", end = " ")
	location = input()
	i = 0
	for bottle in json_object[storageUnit]:
		if bottle["Location"] == location:
			print("------------------------------------")
			print(bottle["Name"], end = " ")
			print(bottle["Year"], end = " ")
			print(bottle["Variety"])
			print("------------------------------------")
			print("Is this the bottle you want to remove? (yes/no)")
			print("~~ ", end = " ")
			deleteConfirm = input()
			if deleteConfirm == "yes":
				if bottle["Quantity"] == 1:
					json_object[storageUnit].pop(i)
					break
				else:
					bottleName = bottle["Name"]
					json_object[storageUnit].pop(i)
					for b in json_object[storageUnit]:
						if b["Name"] == bottleName:
							b["Quantity"] -= 1
					break
		i += 1
	if deleteConfirm != "yes":
		print("List Delete Failed")
	open("bottles.json", "w").write(json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': ')))

def addBottle(fridge):
	if fridge:
		storageUnit = "fridge"
	else:
		storageUnit = "rack"
	print("Quantity of Bottle(s): ")
	print("~~ ", end = " ")
	bottleQuantity = int(input())
	print("Name of Bottle(s): ")
	print("~~ ", end = " ")
	bottleName = input()
	print("Notes of Bottle(s): ")
	print("~~ ", end = " ")
	bottleNotes = input()
	print("Origin of Bottle(s): ")
	print("~~ ", end = " ")
	bottleOrigin = input()
	print("Rating of Bottle(s): ")
	print("~~ ", end = " ")
	bottleRating = input()
	print("Price of Bottle(s): ")
	print("~~ ", end = " ")
	bottlePrice = float(input())
	print("Variety of Bottle(s): ")
	print("~~ ", end = " ")
	bottleVariety = input()
	print("Year of Bottle(s): ")
	print("~~ ", end = " ")
	bottleYear = int(input())
	with open('bottles.json') as f:
	  	json_object = json.load(f)
	for i in range(0, bottleQuantity):
		print("Location of Bottle: ")
		print("~~ ", end = " ")
		bottleLocation = input()
		json_object[storageUnit].append({
			"Location": bottleLocation,
			"Name": bottleName,
			"Notes": bottleNotes,
			"Origin": bottleOrigin,
			"Personal Rating": bottleRating,
			"Price": bottlePrice,
			"Quantity": bottleQuantity,
			"Variety": bottleVariety,
			"Year": bottleYear
			})
	open("bottles.json", "w").write(json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': ')))
	print("Success")


def dumpList(fridge, rack):
	if fridge and not rack:
		print("Fridge")
		printList("fridge")
	elif not fridge and rack:
		print("Rack")
		printList("rack")
	else:
		print("Fridge")
		printList("fridge")
		print("\nRack")
		printList("rack")

def printList(storageUnit):
	listedBottles = {}
	with open('bottles.json', "r") as f:
	  	json_object = json.load(f)
	for bottle in json_object[storageUnit]:
		if bottle["Name"] not in listedBottles:
			listedBottles[bottle["Name"]] = 1
			print("--------------------------------------------------------------------")
			print(bottle["Name"], end = "\t")
			print(bottle["Year"], end = " ")
			print(bottle["Variety"] + "\t\t" + bottle["Origin"] + "\n" + "$", end = "")
			print(bottle["Price"], end = "\t\t")
			print("Quantity:", end = " ")
			print(bottle["Quantity"], end = "\t\t")
			if(bottle["Quantity"] == 1):
				print("Location(s): " + bottle["Location"])
			else:
				locationChain = ""
				for b in json_object[storageUnit]:
					if b["Name"] == bottle["Name"]:
						locationChain += b["Location"] + " | "
				print("Location(s): " + locationChain)
			print("Personal Rating: " + bottle["Personal Rating"])
			print("\n" + bottle["Notes"])
		else:
			listedBottles[bottle["Name"]] += 1
	print("--------------------------------------------------------------------")

main()

