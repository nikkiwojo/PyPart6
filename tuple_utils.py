from typing import Iterable, Tuple, List, Union
TicTacToeRow = List[str]
TicTacToeBoard = Tuple[TicTacToeRow, TicTacToeRow, TicTacToeRow]


def tic_tac_toe_finish(board: TicTacToeBoard, pos_y: int, pos_x: int, symbol: str) -> None:
    
    board[pos_y][pos_x] = symbol


def count_instances(collection: Tuple, instance: Union[int, str]) -> int:
    
    count = 0
    for element in collection:
        if element == instance:
            count += 1
    return count

 
def print_indexes_and_entries(indexes: Iterable, entries: Iterable) -> None:
    count = 0
    while count < len(indexes):
        print("Index: " + str(indexes[count]) + "   Entry: " + str(entries[count]))
        count += 1



def print_items_with_index(items: Iterable):
    
    n = 0
    while n < len(items):
        print(str((n+1)) + ": " + str(items[n]))
        n += 1
    


