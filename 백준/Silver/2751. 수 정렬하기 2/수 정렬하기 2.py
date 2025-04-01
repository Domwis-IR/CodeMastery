def counting_sort(num_list):
    max_value = max(num_list)
    
    # Initialize the count array with zeros
    count = [0] * (max_value + 1)

    for num in num_list:
        count[num] += 1
    
    # Modify count array such that each element at each index stores the sum of previous counts.
    # Which is changing the array into a cumulative count array.
    for i in range(1, len(count)):
        count[i] += count[i-1]

    output = [0]*len(num_list)

    for num in reversed(num_list):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

def __main__():
    import sys
    input=sys.stdin.readline
    N = int(input())
    num_list = [int(input()) for _ in range(N)]
    
    result = sorted(num_list)
    for num in result:
        print(num)

if __name__ == "__main__":
    __main__()