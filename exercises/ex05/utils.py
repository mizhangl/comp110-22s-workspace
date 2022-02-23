"""Creates functions 'only_evens', 'sub', 'concat'!"""

__author__ = "730490943"


def main() -> None:
    """The entrypoint of my code!"""
    print(only_evens([1, 3, 4, 6, 1, 3]))
    print(sub([10, 20, 30, 40, 50, 60], 1, 9))
    print(concat([1, 2, 3], [4]))


def only_evens(x: list[int]) -> list[int]:
    """Given a list of integers, return only even numbers.."""
    i: int = 0
    new_list: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            new_list.append(x[i])
        i += 1
    return new_list
    

def sub(x: list[int], start_index: int, end_index: int) -> list[int]:  # Recall that end_index is non-inclusive.
    """Given a list of integers and a start and end index, 'sub' will a subset of the original list.
    
    This will be noninclusive, meaning the new sublist will be between the specified start index and the end index - 1.
    """
    i: int = 0 
    sub_list: list[int] = []
    if start_index < 0:  # Ensures that if the starting index is less than 0, it will automatically be assigned to the first index. 
        start_index = i
    if end_index > len(x):  # Ensures if the ending index is greater than the length of the list, it will be assigned to the last index.
        end_index = (len(x))
    if len(x) == 0 or start_index > len(x) or end_index <= 0:
        return sub_list
    while start_index <= (end_index - 1):
        sub_list.append(x[start_index])
        start_index += 1
    return sub_list

        
def concat(x: list[int], y: list[int]) -> list[int]:
    """Given two lists of integers, 'concat' will concat the two lists and form a new list.
    
    The new list will contain all of the elements of the first list followed by all of the elements of the second list.
    """
    i: int = 0
    concat_list: list[int] = x
    while i < len(y):
        concat_list.append(y[i])
        i += 1
    return concat_list

    
if __name__ == "__main__":
    main()