# winelist
Command line based Wine List to keep track of wine and basic information. Support for fridge and rack space.

### Get Started
1. Clone the latest version master into a folder where you would like the app and the data to live.
2. Add a file named `bottles.json` in the folder and initialize with the example at the bottom of this page.
3. To run, open terminal and cd into the folder with the app and json file.
4. Run `python3 winelist.py`

### Command Guide
Viewing the List
`ls` --> dumps list to output for both fridge and rack modules
`ls -f` --> dumps fridge list only to output
`ls -r` --> dumps rack list only to output

Adding a Bottle
`add -f` OR `add -r` to add to either fridge or rack
follow the instructions and for any quantity greater than 1, enter your custom location tag for each bottle at each prompt

Removing a Bottle
`rm -f` OR `rm -r` for removing from either fridge or rack
Enter the locationof bottle to be removed and confirm

### JSON file 
Paste this into your new `bottles.json` to get started
`{
    "fridge": [],
    "rack": []
}`
