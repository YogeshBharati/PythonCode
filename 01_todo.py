# Program that ask user to enter n no of todo and display it.
fruits = []
total_fruit = int(input("Enter total number of fruts: "))

for i in range(1,total_fruit+1):
    frut = input(f"Enter fruts {i}: ")
    fruits.append(frut) # Append 

print("\n------------\n")

print("All fruts are: ")
# Display all result
for frut in fruits:
    print(frut)
    

# Ask user to enter n number of fruits 
# and display all fruits