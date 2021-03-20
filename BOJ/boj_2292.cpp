#include <iostream>

using namespace std;

/*
    중심에서의 거리에 따른 최대값
    1->7->19->37->61->...
     +6 +12 +18 +24 ...
    한 칸씩 확장시마다 이전 변화량의 6이 더해짐
*/

int main(void){
    long long target;
    cin >> target;

    long long change = 0;
    long long num = 1;
    long long cnt = 1;

    while(1){
        num += change;
        // cout << num << " ";
        if(num >= target){
            break;
        }
        change += 6;
        cnt ++;
    }
    // cout << endl;
    cout << cnt << endl;

    return 0;
}