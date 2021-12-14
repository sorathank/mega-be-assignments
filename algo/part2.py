def solve(wordList, target):
    for separator_idx in range(1, len(target)):
        print(target[:separator_idx], target[separator_idx:])

wordList = []
target = "a"

if __name__ == "__main__":
    solve(wordList, target)

