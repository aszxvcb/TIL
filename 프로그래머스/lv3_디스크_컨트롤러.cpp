#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

/*
    작업의 요청이 시간이 빠르고, 작업시간이 짧은 프로세스부터 차례로 수행
*/

struct compare{ // 우선순위큐에서의 cmp 함수는 sort()에서 정의하던 sort와 반대부호를 가지고 있음!! https://urbangy.tistory.com/43
    bool operator()(pair<int, int> p1, pair<int,int> p2){
        if( p1.first > p2.first ){ // 오름차순
            return true;
        }
        else if( p1.first == p2.first ){
            if( p1.second <= p2.second ){ // 내림차순
                return true;
            }
        }
        
        return false;
    }
};

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int curTime = 0;
    int processTime = 0;
    int size = jobs.size();
    int cnt = 0;
    priority_queue<pair<int, int>, vector<pair<int,int>>, compare>  PQ;

    // jobs를 요청시간 순으로 정렬    
    sort(jobs.begin(), jobs.end());

    while( size != cnt ){ // 모든 jobs이 처리될때 까지 반복문 수행
        
        // 실행될 프로세스 체크
        while( jobs.front()[0] <= curTime && !jobs.empty()){
            PQ.push( make_pair(jobs.front()[1], jobs.front()[0]) );   // 수행시간이 짧은것부터 정렬되도록 우선순위큐에 삽입
            jobs.erase(jobs.begin());   // jobs에서 제거
        }
        
        cout << "======================" << endl;

        if( PQ.empty() ){ // 수행될 프로세스가 없을때는 다음 프로세스가 실행될 수 있도록 시간 조정
            curTime = jobs.front()[0];
        }
        else if( !PQ.empty() ){
            cout << "top : " <<  PQ.top().first << " " << PQ.top().second << endl;
            processTime += curTime - PQ.top().second + PQ.top().first;
            cout << curTime - PQ.top().second + PQ.top().first << endl;
            curTime += PQ.top().first;    // 수행시간 증가
            PQ.pop();                     // 프로세스 종료
            cnt++;
        }

    }
    answer = processTime / size; 
    return answer;
}

int main(void){

    vector<vector<int>> jobs = {{0, 10}, {2,9} ,{2, 10}, {9, 10}, {15, 2}};
    int ret;

    ret = solution(jobs);
    cout << ret;

    return 0;
}