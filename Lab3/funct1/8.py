def spy_game(nums):
    code = [0, 0, 7, 'True']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
nums = list(map(int, input().split()))
print(spy_game(nums))