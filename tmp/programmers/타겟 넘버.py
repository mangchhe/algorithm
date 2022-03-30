def solution(numbers, target):
    def traverse(idx, sumVal):
        if idx >= len(numbers):
            if sumVal == target:
                return 1
            return 0
        return traverse(idx + 1, sumVal + numbers[idx]) + traverse(idx + 1, sumVal - numbers[idx])
            
    return traverse(0, 0)
