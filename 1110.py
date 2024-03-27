# chatgpt 참고함

def get_next_number(n):
    # 각 자리의 숫자를 더하여 새로운 수를 반환합니다.
    return (n % 10) * 10 + (n // 10 + n % 10) % 10


def cycle_length(n):
    count = 1
    original = n

    # 주어진 수와 새로운 수를 비교하여 사이클의 길이를 계산합니다.
    next_num = get_next_number(n)
    while next_num != original:
        next_num = get_next_number(next_num)
        count += 1
    return count


# 입력을 받고 사이클의 길이를 출력합니다.
n = int(input())

print(cycle_length(n))
