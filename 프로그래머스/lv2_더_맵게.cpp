#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;
/*
    set을 구현하는 내부 자료구조는 이진트리로 되어있음
     내부 데이터의 존재유무를 파악할 떄 주로 사용하며, 기본적으로 중복데이터를 허용하지 않는다.
     또한 이진탐색트리(red-block트리) 이기에 삽입시 자동으로 정렬이 이루어진다.
     - 주로 Lookup(데이터가 있는지 탐색)에 사용
     - 특정한 순서를 기대할 수 없음
     * 레드블랙트리
     - 효율적인 삽입, 삭제, 임의의 값 조회 및 찾기
     - 트리 내의 노드가 정렬되어있기 때문에, 사전순 출력 등 모든 노드를 탐색하는 데에 효과적

    우선순위큐의 내부 자료구조는 힙으로 되어있음
     힙은 완전이진트리이며, 부모-자식 노드간의 크기 비교를 통해 정렬되어있다.
     - 값을 삽입하고 최소값을 검색하는 데에 최적화되어 있는 자료구조
     - 검색, 삭제에는 비교적 비효율적
     - 최대, 최소를 뽑아내는데에 효과적
*/

// 우선순위큐를 이용한 구현
int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> heap;
    int num1 = 0, num2 = 0;

    for(int i=0; i<scoville.size(); i++ ){
        heap.push(scoville[i]);
    }

    while( heap.top() < K ){
        if( heap.size() < 2 ){
            return -1;
        }
        num1 = heap.top();
        heap.pop();
        num2 = heap.top();
        heap.pop();
        heap.push( num1 + (num2 * 2) );
        answer++;
    }

    return answer;
    }

/* 
    // set을 이용한 구현
    int solution(vector<int> scoville, int K) {
    int answer = 0;
    multiset<int> heap;

    for(int i=0; i<scoville.size(); i++ ){
        heap.insert(scoville[i]);
    }

    // for( auto elem : heap ){
    //     cout << elem << " " ;
    // }
    // cout << endl;
    // cout << "=============" << endl;

    while( *heap.begin() < K ){
        if( heap.size() < 2 ){
            return -1;
        }
        heap.insert( *(heap.begin()) + (*(++heap.begin()) * 2) );
        heap.erase(heap.begin(), ++(++heap.begin()));
        answer++;
        // for( auto elem : heap ){
        //     cout << elem << " " ;
        // }
        // cout << endl;
    }

    // cout << "=============" << endl;
    // for( auto elem : heap ){
    //     cout << elem << " " ;
    // }
    // cout << endl;

    return answer;
    }
 */

int main(void){

    vector<int> scoville = {12,10,9,3,2,1};
    int K = 7;
    int ret;

    ret = solution(scoville, K);
    cout << ret << endl;

    return 0;
}