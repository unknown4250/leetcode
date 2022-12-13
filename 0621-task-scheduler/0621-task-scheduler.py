class Solution(object):
    def leastInterval(self, tasks, n):
        
        if n == 0:
            return len(tasks)

        dict = {}

        # 카운터 만들기
        for task in tasks:
            dict[task] = dict.get(task, 0) + 1

        counts_list = [dict[task] for task in dict]
        max_count = max(counts_list)

        # 가장 많은 task는 여러 개일 수 있음 (예를 들어, 'A' 3개, 'B' 3개)
        max_count_tasks = counts_list.count(max_count)

        result = max_count + (max_count - 1) * n + (max_count_tasks) - 1
        return max(len(tasks), result)