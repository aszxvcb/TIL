#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

/*
    2중 for문으로 순회하는 경우, 시간초과 발생

    처음 문제 해결전략은 입력된 회의시간이 짧은 순서대로 정렬 후
    visit 배열을 선언하여 start-end 사이의 시간에 사용여부를 확인하여 count를 하여 문제를 해결하려 하였으나
    시간초과 발생.

    정답코드를 확인해보니,
    정렬을 회의가 끝나는 시간을 기준으로 정렬하여야 했고,
    현재 시간과 회의 시간을 비교하면 반복문을 한번만 확인하여도 문제를 해결할 수 있음.

*/

// bool comp(pair<int, int> a, pair<int, int> b ){
//     int distance_a, distance_b;
//     distance_a = a.second - a.first;
//     distance_b = b.second - b.first;

//     if( distance_a < distance_b){
//         return true;
//     }
//     else if( distance_a == distance_b ){
//         if( a.first < b.first ){
//             return true;
//         }
//         else {
//             return false;
//         }
//     }
//     else {
//         return false;
//     }
// }

bool comp(pair<int, int> a, pair<int, int> b){
    
    if( a.second < b.second ){
        return true;
    }
    else if ( a.second == b.second ){
        return a.first <= b.first ? true : false;
    }
    else {
        return false;
    }
}

int solution(vector<pair<int, int>> &schedule ){
    int answer = 0;
    bool visit[1000001] = {0,};
    sort(schedule.begin(), schedule.end(), comp);

    // cout << endl;
    // for( pair<int,int> a : schedule ){
    //     cout << a.first << " " << a.second << endl;
    // }

    for(int i=0; i<schedule.size(); i++ ){
        bool check = true;
        
    }

    /* 이중포문으로 인해 시간초과 발생*/
    // for(int i=0; i<schedule.size(); i++){
    //     bool check = true;
    //     int start = schedule[i].first;
    //     int end = schedule[i].second;

    //     for(int idx = start+1; idx < end; idx++ ){
    //         if( visit[idx] == 1 ){
    //             check = false;
    //             break;
    //         }
    //     }
        
    //     if( check == true ){
    //         for(int idx = start; idx <= end; idx++ ){
    //             visit[idx] = 1;
    //         }
    //         answer ++;
    //         // cout << "check " << start << " " << end << endl;
    //     }
    // }

    int cur_time = 0;
    for(int i=0; i<schedule.size(); i++){
        if( cur_time == schedule[i].first && cur_time == schedule[i].second ){ // todo
            answer ++;
        }
        else if( cur_time <= schedule[i].first ){
            cur_time = schedule[i].second;
            answer ++;
        }
    }

    return answer;
}

int main(void){
    int num;
    int ret;
    int start, end;
    vector<pair<int, int>> schedule;

    cin >> num;
    for(int i=0; i<num; i++ ){
        scanf("%d %d", &start, &end);
        schedule.push_back(make_pair(start, end));
    }

    ret = solution(schedule);
    cout << ret << endl;

    return 0;
}