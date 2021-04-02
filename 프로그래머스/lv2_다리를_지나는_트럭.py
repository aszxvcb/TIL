def solution(bridge_length, weight, truck_weights):
    answer = 0

    success = 0
    now_time = 0
    now_weight = 0
    on_truck = []
    out_time = []
    size = len(truck_weights)

    while( success != size ):
        now_time += 1
        if ( len(truck_weights)!=0 and now_weight + truck_weights[0] <= weight ):
            on_truck.append(truck_weights[0])
            out_time.append(now_time + bridge_length - 1)
            now_weight += truck_weights.pop(0)

        # print( now_time, on_truck, out_time )
        
        if ( len(out_time) != 0 and now_time == out_time[0] ):
            now_weight -= on_truck.pop(0) 
            out_time.pop(0)
            success += 1

    answer = now_time + 1

    return answer

if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    ret = solution(bridge_length, weight, truck_weights)
    print(ret)