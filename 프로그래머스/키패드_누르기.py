def solution(numbers, hand):
    # print(numbers, hand)

    ret = []

    leftHand = {"x": 0, "y": 3}
    rightHand = {"x": 2, "y": 3}

    leftNums = [1,4,7]
    rightNums = [3,6,9]
    centerNums = [2,5,8,0]

    for elem in numbers:
        if elem in leftNums:
            leftHand["x"] = 0
            leftHand["y"] = leftNums.index(elem)
            ret.append("L")

        elif elem in rightNums:
            rightHand["x"] = 2
            rightHand["y"] = rightNums.index(elem)
            ret.append("R")

        else: # centerNums
            ## 왼손과 오른손 중 거리를 계산해서 가까운 손으로 클릭
            l_distance = abs(leftHand["x"] - 1) + abs(leftHand["y"] - centerNums.index(elem))
            r_distance = abs(rightHand["x"] - 1) + abs(rightHand["y"] - centerNums.index(elem))

            # print("check _L_ " , elem, leftHand["x"], leftHand["y"], centerNums.index(elem), l_distance)
            # print("check _R_ " , elem, rightHand["x"], rightHand["y"], centerNums.index(elem), r_distance)

            if l_distance < r_distance:
                leftHand["x"] = 1
                leftHand["y"] = centerNums.index(elem)
                ret.append("L")
            elif l_distance > r_distance:
                rightHand["x"] = 1
                rightHand["y"] = centerNums.index(elem)
                ret.append("R")
            else : # 두 거리가 같을때는 주 손잡이로 선택
                if hand == "left":
                    leftHand["x"] = 1
                    leftHand["y"] = centerNums.index(elem)
                    ret.append("L")
                else : # right
                    rightHand["x"] = 1
                    rightHand["y"] = centerNums.index(elem)
                    ret.append("R")
    
    # print( "".join(ret) )
    return "".join(ret)