// 근묵자흑 문제
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int solution(int N, int K, vector<int> arr){
    int answer = 0;
    int min_idx;
    int left_num=0;
    int right_num=0;

    min_idx = min_element(arr.begin(), arr.end()) - arr.begin();

    left_num = min_idx;
    right_num = arr.size() - (min_idx+1);

    cout << min_idx << " " << left_num << " " << right_num << endl;

    answer += left_num / (K-1);
    if( left_num % (K-1) != 0 ){
        answer++;
    }

    answer += right_num / (K-1);
    if( right_num % (K-1) != 0){
        answer++;
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