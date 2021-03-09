#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

/*  정석 풀이 투포인터

    왼쪽 끝, 오른쪽 끝을 의미하는 포인터 두가지를 가지고
    오른쪽으로 늘리면서 범위를 찾고 -> 왼쪽을 줄여가며 범위를 줄여나가는 방법
    초기 포인터의 위치는 첫번째 인덱스를 가리킨다.

    이렇게하면 범위를 0부터 다시 계산하지 않아도 됨
*/



int main(void){
    vector<string> gems = {"ZZZ", "YYY", "NNNN", "YYY", "BBB"};
    vector<int> ret;

    // ret = solution({"DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"});
    // for(auto elem: ret){
    //     cout << elem << " ";
    // }
    // cout << endl;

    // ret = solution({"AA", "AB", "AC", "AA", "AC"});
    // for(auto elem: ret){
    //     cout << elem << " ";
    // }
    // cout << endl;

    // ret = solution({"XYZ", "XYZ", "XYZ"});
    // for(auto elem: ret){
    //     cout << elem << " ";
    // }
    // cout << endl;

    ret = solution({"ZZZ", "YYY", "NNNN", "YYY", "BBB"});
    for(auto elem: ret){
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}

/*  두번째 풀이

    반복문 중첩이 짧아졌지만, 여전히 시간초과 발생

    각 인덱스마다 충족하는 범위를 찾는다.
    아마 각 인덱스마다 범위를 0부터 다시 계산해서 시간초과가 나는 것 같다.

vector<int> solution(vector<string> gems) {
    vector<int> answer;
    unordered_map<string, int> hash;
    int cnt=0;
    int size=gems.size();

    // 보석의 종류갯수 파악
    for(string elem : gems){
        if( hash.find(elem) == hash.end()){
            hash.insert(make_pair(elem, 0));
        }
    }
    // cout << hash.size() << endl;

    // 각 인덱스에서부터 모든 원소를 채우기위해 몇개가 필요한지 체크
    for(int i=0; i<gems.size(); i++){
        // 해시 초기화
        cnt = 0;
        for(auto iter = hash.begin(); iter != hash.end(); iter++){
            iter->second = 0;
        }
        // cout << "idx : " << i << endl;

        for(int j=0; j<gems.size(); j++){
            if( i+j >= gems.size() || size < j ){
                break;
            }
            // cout << j << endl ;
            auto check = &hash.find(gems[i+j])->second;
            if( *check == 0 ){
                *check = 1;
                cnt++;
                if( cnt == hash.size() ){
                    // cout << "check" << endl;
                    if( answer.empty() ){
                        answer.push_back(i+1);
                        answer.push_back(i+j+1);
                    }
                    else{
                        int start = answer[0];
                        int end = answer[1];
                        size = end - start;

                        if( size > j){
                            answer.clear();
                            answer.push_back(i+1);
                            answer.push_back(i+j+1);
                        }
                    }
                    break;
                }
            }
        }
    }
    return answer;
}
*/

/*
    결과는 맞지만, 시간초과가 나는 코드
    정해진 범위 만큼 모든 인덱스를 탐색하다보니 최선의 경우 빠를 수 있지만,
    최악의 경우 모든 너무 많은 경우를 탐색하게 된다.

vector<int> solution(vector<string> gems) {
    vector<int> answer;
    unordered_map<string, int> hash;
    int cnt=0;

    // 보석의 종류갯수 파악
    for(string elem : gems){
        if( hash.find(elem) == hash.end()){
            hash.insert(make_pair(elem, 0));
        }
    }
    // cout << hash.size() << endl;

    for(int range=hash.size(); range <= gems.size(); range++){ // 보석 종류의 수~전체개수로 나눠서 판단
        // cout << "range : "  << range << endl;
        for(int idx=0; idx<=gems.size()-range; idx++){
            // 해시 초기화
            for(auto iter = hash.begin(); iter != hash.end(); iter++){
                iter->second = 0;
            }
            // cout << "idx : " << idx << endl;
            cnt = 0;
            for(int cur=0; cur<range; cur++){
                auto check = &(hash.find(gems[idx+cur])->second);
                if( *check == 0 ){
                    *check = 1;
                    cnt ++;
                    if( cnt == hash.size() ){
                        answer.push_back(idx+1);
                        answer.push_back(idx+cur+1);
                        return answer;
                    }
                }
            }
        }
    }

    return answer;
}
*/
