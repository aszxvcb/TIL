'''
    skill_trees의 원소를 skill_tree 라고 하였을 때
    skill에 있는 각각의 원소들이 skill_tree에 어느 인덱스에 있는지 확인하여 idx_list 에 저장
    idx_list에 -1이 있다면 99로 변경하고
    전체 idx_list를 순회하면서 모든 원소가 이전 원소보다 클때 count

    다른 답안 코드를 확인하니
    skill 을 list 로 만들어놓고
    skill_tree에서 skill 에 존재하는 원소가 있을 때
    그것이 skill_list.pop(0)과 같은지 확인
    하는 방법으로 문제를 더 간결하게 해결함.
    
'''

def solution(skill, skill_trees):
    answer = 0

    idx_list = list()

    for skill_tree in skill_trees:
        idx_list.clear()

        for elem in skill:
            idx_list.append( skill_tree.find(elem) )

        for i in range (0, len(idx_list)):
            if( idx_list[i] == -1 ):
                idx_list[i] = 99

        # print(idx_list, " ", end = '') # log

        check = True
        for i in range (0, len(idx_list)-1 ):
            if( idx_list[i] > idx_list[i+1] ):
                check = False
                break
        
        # print(check) # log

        if ( check == True ):
            answer += 1             
            

    return answer



if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    ret = solution(skill, skill_trees)
    print(ret)
