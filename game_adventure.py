a_board = [(0,0),(0,1),(0,2),(0,3),(0,4),
          (1,0),(1,1),(1,2),(1,3),(1,4),
          (2,0),(2,1),(2,2),(2,3),(2,4),
          (3,0),(3,1),(3,2),(3,3),(3,4),
          (4,0),(4,1),(4,2),(4,3),(4,4)]

class Board:
    
    def __init__(self, size, mylist):
        self.size = size
        self.mylist = [None] * size
             
board = Board(25, "mylist")
board.mylist[0] = "herb"
# print(board.mylist)

print("-----------------------------------")
for i in [1,2,3,4,5,6]:
    if i == 1:
        i = ""
    print("| ", end="")
    print(i, end="")
    print("  | ", end="")
    for j in [0,1,2,3,4,5]:
        if j == 1:
            j = ""
        print(j, end="")
        print("  | ", end="")
    print("\n")

    print("------------------------------------")
                
