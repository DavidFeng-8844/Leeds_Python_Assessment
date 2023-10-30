"""
Introduction to Programming Coursework 1

@author: Yujie Feng
@date: 19-10-2023
"""

# Task 1.1 - Check if all strings in the puzzle have the same length
def valid_puzzle(puzzle: list) -> bool:
    if not isinstance(puzzle, list):
        return False
    # Generate a list of string lengths.
    # Create a set from the list of string lengths.
    # Set only allows unique values, so if the length set has a size of 1,
    # it means all strings have the same length.
    if len(set(len(s) for s in puzzle)) == 1:
        return True
    else:
        return False

# Task 1.2 - Group similar items in a list
def similarity_grouping(data: list) -> list:
    if not isinstance(data, list):
        return []   

    grouped_data = []  # List to store grouped data
    seen = set()  # Set to keep track of seen items

    for item in data:
        item_str = str(item)

        if item_str not in seen:
            seen.add(item_str)
            # A list contains the same elements as item_str in data.
            group = [x for x in data if str(x) == item_str]
            grouped_data.append(group)

    return grouped_data

# Task 1.3 - Find items with the highest count in a comma-separated string
def highest_count_items(data: str) -> list:
    if not isinstance(data, str):
        return []

    items = data.split(',')  # Split the input string into a list of items
    counts = {}  # Dictionary to store item counts
    max_count = 0  # Variable to keep track of the maximum count

    for item in items:
        item = item.strip()  # Remove leading and trailing spaces
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

        if counts[item] > max_count:
            max_count = counts[item]

    # Create a list of items with the highest count
    result = [[item, count] for item, count in counts.items() 
              if count == max_count]
    return result

# Task 1.4 - Check if all characters in a list of strings
# belong to a given character set
def valid_char_in_string(popList: list, charSet: list) -> bool:
    if not all(len(char) == 1 for char in charSet):
        return False

    for string in popList:
        for char in string:
            if char not in charSet:
                return False

    return True

# Task 1.5 - Calculate the total price of units with a discount
def total_price(unit: int) -> float:
    single_price = 1.25  # Price per single unit
    sixpack_price = 5.00  # Price for a six-pack

    if unit < 0:
        return 0

    # Calculate the total price, applying 
    # the six-pack discount if applicable
    total_price = (unit // 6) * sixpack_price + (unit % 6) * single_price

    if total_price >= 20.00:
        total_price *= 0.9  # Apply a 10% discount if the
                            #total price is $20 or more

    return round(total_price, 2)

if __name__ == "__main__":
    # Sample test for task 1.1
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    puzzle2 = ['NAROUNDDL', 'EDCIT', 'UWSWEDZYA', 'OTCONVOYV',
               'BOSEVRUCI', 'BLLCGLPBD', 'TEENAGEDL', 'TREWZLCGY',
               'RAPLEBAYG', 'ATYTBIWRA', 'YEMROFINU']

    puzzle3 = ['RUNAROU', ['EDCITOA'], ('ZYUWSWE'), 'AKOTCYV',
               'LSBOSEI', 'BOBLLCG', 'LKTEENA', 'ISTREWY',
               'AURAPLE', 'RDATYTB', 'TEYEMRO']
    puzzle4 = 'roundandround'
    print(valid_puzzle(puzzle1))
    print(valid_puzzle(puzzle2))
    print(valid_puzzle(puzzle3))
    print(valid_puzzle(puzzle4))

    # Sample test for task 1.2
    data1 = [2, 1, 2, 1]
    data2 = [5, 4, 5, 5, 4, 3]
    data3 = [1, 2, 1, 3, 'a', 'b', "a",  'c']
    print(similarity_grouping(data1))
    print(similarity_grouping(data2))
    print(similarity_grouping(data3))

    # Sample test for task 1.3
    data4 = ("3, 13, 7, 9, 3, 3, 5, 7, 12, 13, 11, 13, 8, 7, 5, 14, 15, 3, 9,"
             "7, 5, 9, 14, 3, 8, 2, 5, 5, 8, 14, 11, 11, 12, 8, 5, 3, 3, 10,"
             "3, 10, 7, 7, 10, 10, 2, 7, 4, 8, 1, 5")
    data5 = ("British Gas, British Gas, Ovo, Igloo, Igloo, Octopus, Bulb,"
             "Shell, E.ON, Npower, British Gas, Octopus, Igloo, Npower, Igloo,"
             "Shell, Scottish Power, Bulb, EDF, Bulb, EDF, Bulb,"
             "Scottish Power, Octopus, Scottish Power, Octopus, Octopus, EDF,"
             "Ovo, Shell, Octopus, E.ON, British Gas, Bulb, Npower, Shell,"
             "Scottish Power, Npower, Scottish Power, Npower")
    data6 = ("aac, ctt, gat, ccc, gcc, ctg, gtc, tcg, ccg, cca, ata, cca,"
             "tat, ata, cac, gcg, cca, gta, gtg, gac, taa, ata, gtc, aat, gct,"
             "gta, ggc, tgc, tca, ctt, tgt, ata, acc, tgc, gac, cgc, atc, cgt,"
             "tac, agg, ctt, cgc, cgc, tgg, gcg, tgg, taa, cta, aaa, tgc, cgt,"
             "tgc, gac, tta, aag, taa, act, cca, tac, agg, cgc, gtg, cca, gcg,"
             "gtt, gag, tca, aca, tct, gta, ata, ctt, gat, tcg, tcg, cac, cgt,"
             "tac, caa, aac, ctg, tgt, aag, ttc, ccc, tcc, ctc, cct, aga, gtt,"
             "tga, gaa, cct, ctc, tct, ggt, gcc, tct, ccc, agt, caa, gac, ccc,"
             "cgc")
    
    print(highest_count_items(data4))
    print(highest_count_items(data5))
    print(highest_count_items(data6))

    # sample test for task 1.4
    popList1 = ['00000', '00001', '00010', '00011', '00100']
    popList2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
                'ccg', 'cca', 'ata']
    popList3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
    charSet1 = ['0', '1']
    charSet2 = ['a', 'c', 't', 'g']
    charSet3 = ['a', 'c']
    charSet4 = '01'
    print(valid_char_in_string(popList1, charSet1))
    print(valid_char_in_string(popList2, charSet2))
    print(valid_char_in_string(popList3, charSet3))
    print(valid_char_in_string(popList1, charSet4))

    # sample test for task 1.5
    print(total_price(3))
    print(total_price(12))
    print(total_price(15))
    print(total_price(26))
