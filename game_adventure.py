class Board:
    def __init__(self, size):
        self.size = size

    def theBoard(self):
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
             
board = Board(25)
board.theBoard()

class NPE(Board):
    def __init__(self, size, herb, bread, block1, block2):
        super().__init__(size)
        self.herb = herb
        self.bread = bread
        self.block1 = block1
        self.block2 = block2

    def npe_herb(self):
            print("#")

npe = NPE(25, '#', '@', '^', '^^')
