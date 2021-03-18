#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/*
    가능한 순열을 찾고
    해당 순열에서 가능한 조건들을 하나씩 확인한다.
    모든 조건을 충족하면 answer++ 을 한다.
*/

int solution(int n, vector<string> data) {
    int answer = 0;
    int left, right;
    int distance;
    int cnt = 0;

    vector<char> friends = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    sort(friends.begin(), friends.end());

    do{
        cnt = 0;
        for(int i=0; i<n; i++ ){
            left = find(friends.begin(), friends.end(), data[i][0]) - friends.begin() + 1;
            right = find(friends.begin(), friends.end(), data[i][2]) - friends.begin() + 1;
            distance = abs( left - right ) - 1;

            if( data[i][3] == '='){
                if( distance == (data[i][4]-'0') ){
                    cnt++;
                }
            }
            else if( data[i][3] == '<'){
                if( distance < (data[i][4]-'0') ){
                    cnt++;
                }
            }
            else if( data[i][3] == '>'){
                if( distance > (data[i][4]-'0') ){
                    cnt++;
                }
            }

            if( cnt == n ){
                answer++;
            }
        }
    }
    while( next_permutation(friends.begin(), friends.end()) );

    // cout << answer << endl;

    return answer;
}

int main(void){
    int n = 2;
    vector<string> data = {"N~F=0", "R~T>2"};
    int ret;

    ret = solution(n, data);

    cout << ret << endl;

    return 0;
}