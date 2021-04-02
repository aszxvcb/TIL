def solution(prices):
    answer = []

    for i in range(0, len(prices)):
        for j in range(i, len(prices)):
            if (prices[i] > prices[j]) or (j == len(prices)-1):
                answer.append(j-i)
                break

    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]	
    ret = solution(prices)
    print(ret)

