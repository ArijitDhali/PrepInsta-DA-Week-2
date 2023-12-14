def rules():                     # Dsiplaying th general rules of the game
    print("\nAIM : To move all \U0001f7e2 frogs to right and \U0001f7e4 frogs to left ")
    print("1. A frog can only jump in a given direction")
    print("2. A frog can jump over only 1 frog at a time")
    print("3. A frog can also jump to nearby vacant rock in given direction")
    print("4. 5 Invalid moves and you loose.")
    print("CROAKS! \U0001F438 Good Luck!")


def difficulty(level):
    arr=[]
    B="\U0001f7e4"               # Displays 🟤
    G="\U0001f7e2"               # Displays 🟢
    for i in range(level):       # Appends level times 🟢 in the beginning of list
        arr.append(G)
    arr.append('-')              # Appends '-' in the middle of list
    for i in range(level):       # Appends level times 🟤 in the ending of list
        arr.append(B) 
    return arr

def indx(level):                
    ind=[]
    for i in range(2*level+1):   # List ranging from 0 to difficulty level*2 + 1
        ind.append(str(i))       # Appending numbers
    return ind
    
def check(positions,level):
    B="\U0001f7e4"                # Displays 🟤
    G="\U0001f7e2"                # Displays 🟢
    checkarr=[]
    for i in range(level):        # Appends level times 🟤 in the beginning of list
        checkarr.append(B)
    checkarr.append('-')          # Appends '-' in the middle of list
    for i in range(level):        # Appends level times 🟢 in the ending of list
        checkarr.append(G)
    if positions==checkarr:       # Checks if the reverese of beginning positions and immediate positions are equal or not
        return True               # Return True if condition matches
    return False
    

#def main
lvl=0
rules()                           # Displays the general rules before the acual game
while(lvl>7 or lvl<1):                                                            # Will loop unless and until the input lies between a desired range
    print("\n\nChoose your Difficulty between [1\U0001F913 to 7\U0001F60F]")
    lvl=int(input("Enter your choice: "))                                         # Takes input for number of frogs at same kind
    if (lvl>7 or lvl<1):                                                          # Checks if the input strictly lies between the range or not
        print("REALLY?!! \U0001F611 Choose between 1 and 7")
        print("Try Again")

positions=difficulty(lvl)         # Passing the values to the functions
arr=indx(lvl)
# Step 1

G="\U0001f7e2"                    # Displays 🟢
B="\U0001f7e4"                    # Displays 🟤
count=0                           # Initializing Count = 0 For measuring "Invalid Move"
# Initial Display

print('    '.join(arr))           # Displays the index list in string for visual presentation
print('   '.join(positions))      # Displays the frog positioning list in string for visual presentation

while True:
    print("\nPress 'q' to quit else")
    position = input("Enter position of piece: ")     # Players enter the input    

    if position == 'q':                               # If player enters 'q' then they quit the game
        print("You Lose!")
        break
    if count==4:                                      # If player has more than 4 Invalid Moves, it will automatically quit the game
        print("Uh-oh! Looks like you are stuck!")
        print("Start Again!")
        break

    position = int(position)                          # Converts the input string to interger [Type Conversion]

    # Step 2: Check Validity of Move
    if position < 0 or position > (lvl*2):            # Check the presence of the position within the given range
        print('Invalid Move')
        continue

    if positions[position] == '-':                    # If player tries to select the blank place
        print('Invalid Move')
        continue

    pos2 = 0                                          # Intializing pos2=0

    # Step 3: Check frog color and conditions for valid moves
    if positions[position] == G:                                      # Determining if the selected position contains G
        if position + 1 <= (lvl*2) and positions[position + 1] == '-':      # Determing the possibility of 1 Jump
            pos2 = position + 1
        elif position + 2 <= (lvl*2) and positions[position + 2] == '-' and positions[position + 1] == B:   # Determing the possibility of 2 Jump
            pos2 = position + 2
        else:                                   # Will Display on erroneous input
            print('Invalid Move')
            count+=1
            continue
    elif positions[position] == B:                                    # Determining if the selected position contains B
        if position - 1 >= 0 and positions[position - 1] == '-':      # Determing the possibility of 1 Jump
            pos2 = position - 1
        elif position - 2 >= 0 and positions[position - 2] == '-' and positions[position - 1] == G:   # Determing the possibility of 2 Jump
            pos2 = position - 2
        else:                                   # Will Display on erroneous input
            print('Invalid Move')
            count+=1
            continue

    # Step 4: Swap elements to make the move
    positions[position], positions[pos2] = positions[pos2], positions[position]   # Swap the places of frog and blank space

    # Display game
    print('    '.join(arr))             # Displays the index list in string for visual presentation
    print('   '.join(positions))        # Displays the frog positioning list in string for visual presentation

    # Check winning condition
    if check(positions,lvl):            # If check() return True, then the player is declared as winner
        print('You Win!')
        break
