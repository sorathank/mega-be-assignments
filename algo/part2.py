wordList = ["abab", "bc", "cd", "", ""]
target = ""

def solve(wordList, target):

    duplicated_set = set()
    word_set = set()

    for word in wordList:
        if word in word_set:
            duplicated_set.add(word)
        else:
            word_set.add(word)

    ## EMPTY STRING EDGE CASE HANDLER
    EMPTY_STRING = ""
    if target == EMPTY_STRING and EMPTY_STRING in duplicated_set: return f'("{EMPTY_STRING}", "{EMPTY_STRING}")'

    for separator_idx in range(0, len(target)):
        first_subword = target[:separator_idx]
        second_subword = target[separator_idx:]

        if first_subword in word_set and second_subword in word_set:
            if first_subword == second_subword:
                if first_subword in duplicated_set:
                    return f'("{first_subword}", "{second_subword}")'
            else:
                return f'("{first_subword}", "{second_subword}")'
        
    return None

if __name__ == "__main__":
    print(solve(wordList, target))

