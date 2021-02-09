def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    lst = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        if "\n" in line:
            lst.append(line[:-1])
        else:
            lst.append(line)
    return lst


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    if pivot != int(input_line[0]):
        return False
    res = 1
    k = 1
    while input_line[k + 1] != input_line[-1]:
        if input_line[k] < input_line[k + 1]:
            res += 1
        k += 1
    if res == int(input_line[0]):
        return True
    return False



def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.
    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board:
        if '?' in i:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(\
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(\
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(\
    ['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board:
        if i[0] != '*':
            for k in i:
                if k != '*':
                    if i[1:].count(k) > 1:
                        return False
        if i[0] == '*':
            for k in i:
                if k != '*':
                    if i[:-1].count(k) > 1:
                        return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    res_num = 0
    res = 1
    k = 1
    for i in board:
        if i[0] != '*':
            while i[k + 1] != i[-1]:
                if i[k] < i[k + 1]:
                    res += 1
                k += 1
            if res == int(i[0]):
                res_num = res_num
            else:
                res_num += 1

        if i[-1] != '*':
            i = i[::-1]
            while i[k + 1] != i[-1]:
                if i[k] < i[k + 1]:
                    res += 1
                k += 1
            if res == int(i[0]):
                res_num = res_num
            else:
                res_num += 1

        res = 1
        k = 1
    if res_num == 0:
        return True
    else:
        return False



def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    lst = []
    k = 1
    while k != 6:
        lst1 = [i[k] for i in board[1:-1]]
        lst.append(lst1)
        k += 1
    for i in lst:
        for k in i:
            if k != '*':
                if i.count(k) > 1:
                    return False 
    return True



def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    lst = read_input(input_path)
    if check_columns(lst) and\
    check_uniqueness_in_rows(lst) and\
    check_horizontal_visibility(lst) and\
    check_columns(lst) == True:
        return True
    return False

# if __name__ == "__main__":
#     print(check_skyscrapers("check.txt"))