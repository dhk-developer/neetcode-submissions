class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #nested list, where for each element i within a nested list,
        # no elements inside the nested list must be duplicated (i.e., each list must exist as a set)
        # no elements, sharing the same index, i, must be duplicated
        # no elements within a 3x3 box must be duplicated...
        # So to identify the 3x3 box that the element exists in, we can use //3...
        """
            0,0        0,1      0,2
            
            1,0        1,1      1,2

            2,0        2,1      2,2

        """

        # make 3 passes

        #check each nested list contains no duplicates (except ".")

        for i in range(len(board)):
            row = []

            for value in board[i]:
                if value != ".":
                    row.append(value)

            if len(row) != len(set(row)):
                return False
    
        #check no elements sharing the same index i across nested lists are duplicates:
        for col in range(len(board)):
            column = []

            for row in range(len(board)):
                value = board[row][col]

        #ignore "."

                if value != ".":
                    column.append(value)

            if len(column) != len(set(column)):
                return False

        # check each NxN box contains no duplicates...
        boxes = {}
        box_size = int(len(board) ** 0.5)


        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]

                #skip all "."
                if value == ".":
                    continue

                colbox = col // box_size
                rowbox = row // box_size

                box = (rowbox,colbox)

                if box not in boxes:
                    boxes[box] = set()

                #check for the duplicates.
                if value in boxes[box]:
                    return False
                
                boxes[box].add(value)

        #all passes succeeded.
        return True
                

