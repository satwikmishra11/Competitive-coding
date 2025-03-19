class Solution:
  def subarrayGCD(self, nums: list[int], k: int) -> int:
    ans = 0
    gcds = collections.Counter()

    for num in nums:
      if num % k == 0:
        nextGcds = collections.defaultdict(int)
        nextGcds[num] += 1
        for prevGcd, count in gcds.items():
          nextGcds[math.gcd(prevGcd, num)] += count
        ans += nextGcds.get(k, 0)
        gcds = nextGcds
      else:
        gcds.clear()

    return ans
