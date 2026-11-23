from typing import List


def create_list_of_odds(n: int) -> List[int]:
    arr = list(range(1, n + 1))
    arr_of_odds = [i for i in arr if i % 2 == 1]
    return arr_of_odds


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
