
def solution(participant, completion):
    answer = ''

    hashtable = {}
    for people in participant:
        if people in hashtable:
            hashtable[people] += 1
        else:
            hashtable[people] = 1

    for people in completion:
        hashtable[people] -= 1

    for people in hashtable:
        if hashtable[people] != 0:
            answer = people
    
    print(hashtable)

    return answer

if __name__ == "__main__":

    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    ret = solution( participant, completion )
    print ( ret )