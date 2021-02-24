#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool comp(int a, int b){
    return a>b;
}

int main(void){
    // 입력
    int n = 5;  // 5개의 데이터
    int m = 8;  // 8번의 덧셈
    int k = 3;  // 연속 가능한 덧셈은 3번

    vector<int> data = {2,4,5,4,6};

    // 풀이
    sort(data.begin(), data.end(), comp);

    // for ( auto elem : data){
    //     cout << elem;
    // }

    int cnt=0;
    int sum=0;
    for(int i=0; i<8; i++){
        cnt++;
        if( cnt != k){
            sum += data[0];
        }
        else{
            cnt = 0;
            sum += data[1];
        }
    }

    cout << sum;

    return 0;
}