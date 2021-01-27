#include <string>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    bool re_push = false;

    vector<pair<int, int>> v;
    pair<int, int> cur;
    
    // location이 포함된 새로운 벡터 생성
    for( int i=0; i<priorities.size(); i++){
        v.push_back(make_pair(priorities[i],i));
    }

    while(1){
        cur = v.front();
        v.erase(v.begin());
        re_push = false;

        for( int j=0; j<v.size(); j++){
            // 원소중 현재 선택된 원소의 우선순위보다 큰게 있다면 마지막으로 푸쉬
            if(cur.first < v[j].first ){
                v.push_back(cur);
                re_push = true;
                break;
            }
        }
        // 현재 선택된 원소보다 우선순위가 큰 원소가 없다면
        if( re_push == false ){
            answer++;
            if( re_push == false && cur.second == location){
                return answer;
            }
        }
    }


    return answer;
}

int main(void){

    vector<int> priorities = {1,1,9,1,1,1};
    int location = 0;
    int ret;

    ret = solution(priorities, location);

    printf("%d\n", ret);

    return 0;
}  