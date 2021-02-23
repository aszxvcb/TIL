// 거스름돈 문제
// 그리디

#include <iostream>
#include <vector>

using namespace std;

int main(void){

    // 거스름돈 문제
    int n = 1260;
    int ret = 0;
    int tmp = 0;

    vector<int> coin = {500, 100, 50, 10};

    for(int i=0; i<coin.size(); i++){
        if( n >= coin[i] ){
            tmp = n / coin[i];
            ret += tmp;
            n = n - coin[i] * tmp;
        }
    }

    cout << ret;

}