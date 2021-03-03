#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 0;
    unordered_map<string, int> hashmap;

    // 옷 종류의 개수 계산
    for( int i=0; i<clothes.size(); i++ ){
        hashmap[clothes[i][1]]++;
    }

    answer = 1;
    for( auto elem : hashmap ){
        answer *= elem.second + 1; // +1 은 선택하지 않음에 해당하는 경우의 수
    }
    answer -= 1; // -1 은 모든 경우에서 선택하지 않음. 즉, 아무것도 입지 않음에 대한 경우의 수
    
    return answer;
}

int main(void){

    vector<vector<string>> clothes = {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
    int ret;

    ret = solution(clothes);
    cout << ret << endl;

    return 0;
}