
## How to run

Please use Python3 to run the code.

You can custom the inputs  at first two lines within [part2.py](https://github.com/sorathank/mega-be-assignments/blob/main/algo/part2.py).
```
wordList = ["ab", "bc", "cd"]
target = "abab"
```

After edit the inputs, you can run the code using the command below.
```
python /path_to_file/part2.py
```

If you have any trouble running the code, I had already added it on [colab](https://colab.research.google.com/drive/1acjDWliDw3-ShZF_JqK2KSXdJANT9iFp?usp=sharing) as a alternative way to run the code. Feel free to use it :).


## Performance & Algorithm Analysis

Given target length is m and wordList contains n words.

We know that there are m ways to separate target to be 2 sub-strings.
![](https://i.ibb.co/THjmJzv/S-10911750.jpg)

From my code, I choose to iterate on every possible ways and check if the way is valid.
I initialized two sets used for looking up because it is more efficient than looking up in Python List.

The First one is `word_set`, it is used for check if the sub-strings were given in `wordList`.
The Second one is `duplicated_set`, it is used for check if the sub-string was given more than one time.

This will prevent a case that two sub-strings are the **same** and given in the `wordList` only one time.
Example (from problem document)

    wordList = ["ab", "bc"]
    target = "abab"
    


**Summary**

Time Cost: O(m log(n))

Space: O(n)
