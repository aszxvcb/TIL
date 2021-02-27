#include <string>
#include <vector>
#include <iostream>

using namespace std;

int cnt;
bool visit[20];

/* 더 좋은 풀이
#include <string>
#include <vector>

using namespace std;

int total;

void DFS(vector<int> &numbers, int &target,int sum,int n) {
    if(n >= numbers.size()){
        if(sum == target) total++;
        return;
    }

    DFS(numbers, target, sum + numbers[n], n+1);
    DFS(numbers, target, sum - numbers[n], n+1);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;

    DFS(numbers, target, numbers[0] , 1);
    DFS(numbers, target, -numbers[0], 1);

    answer = total;

    return answer;
}
*/

void DFS(vector<int>& numbers, int target, int idx, int num){
    
    for( ; idx<numbers.size(); idx++){
        if( idx < numbers.size() && visit[idx] == false ){
            num += numbers[idx];
            if( idx == numbers.size()-1 && num == target){
                cnt++;
            }
            
            DFS( numbers, target, idx+1, num );

            num -= 2 * numbers[idx]; // DFS함수 전 더해준 것을 빼줘야하기 때문에 *2 연산
            if( idx == numbers.size()-1 && num == target){
                cnt++;
            }
        }
    }
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    int num = 0;

    DFS(numbers, target, 0, num);

    answer = cnt;

    return answer;
}

int main(void){

    vector<int> numbers = {1,1,1,1,1};
    int target = 3;
    int ret;
    int num=0;

    ret = solution(numbers, target);

    cout << ret << endl;

    return 0;
}