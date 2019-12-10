import collections

nums = [3, 2, 3]
counts = collections.Counter(nums)
print(max(counts.keys(), key=counts.get))
print(counts.get)
