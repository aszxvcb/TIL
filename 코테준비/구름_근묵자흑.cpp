// 근묵자흑 문제

/*
    처음에는 최소원소가 있는 인덱스를 찾고, 그 인덱스를 이용해서 풀이를 하려했다.

    But

    맨앞에서부터 묶어가면서 횟수를 세어주면 해결되는 문제였음.
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int solution(int N, int K, vector<int> arr){
    int answer = 0;

    int i=0;
    for(i=K-1; i<N; i+=K-1){
        answer ++;
    }
    if(N-1 + K-1 != i){
        answer ++;
    }

    return answer;
}

int main(void){
    int ret;

    int N;
    int K;
    vector<int> arr;
    int tmp;

    cin >> N;
    cin >> K;
    
    for(int i=0; i<N; i++){
        cin >> tmp;
        arr.push_back(tmp);
    }

    ret = solution(N, K, arr);

    cout << ret << endl;

    return 0;
}