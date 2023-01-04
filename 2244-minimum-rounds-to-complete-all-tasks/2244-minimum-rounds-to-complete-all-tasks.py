class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks)
        rounds = 0

        for count in tasks.values():
            if count == 1:
                return -1
            # rounds += (count + 2) // 3 OR
            count_of_3 = (count - 2) // 3
            count_of_2 = (count - count_of_3 * 3) // 2
            rounds += count_of_3 + count_of_2

        return rounds