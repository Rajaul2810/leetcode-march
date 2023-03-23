def maxWordCount(sentences):
    count = 0
    for i in sentences:
        count = max(count, len(i.split()))
    return count

print(maxWordCount(["alice and bob love leetcode", "i think so too b b b b", "this is great bbhs bsgssg bgs"]))