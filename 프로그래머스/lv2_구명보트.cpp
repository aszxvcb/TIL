#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/*
    people을 정렬하고, 제일 큰 숫자와 작은 숫자를 더해서 
    limit 이하이면 2명을 태우고,
    limit 초과이면 1명을 태운다.
*/

int solution(vector<int> people, int limit) {
    int answer = 0;
    int cnt = 0;

    sort(people.begin(), people.end(), greater<>());

    // for(auto elem : people){
    //     cout << elem << " ";
    // }
    // cout << endl;
    
    int i = 0;
    int j = people.size()-1;
    while( i<=j ){
        if( limit < people[i] + people[j] ){
            // cout << i << " " << j << endl;
            i++;
            cnt++;
        }
        else if( limit >= people[i] + people[j] ){
            // cout << i << " " << j << endl;
            i++;
            j--;
            cnt++;
        }
    }

    answer = cnt;

    return answer;
}

int main(void){

    int ret;
    vector<int> people = {70, 50, 80, 50};
    int limit = 100;

    ret = solution(people, limit);
    cout << ret << endl;

    return 0;
}