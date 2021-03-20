#include <iostream>

using namespace std;

/*
    달팽이는 올라가고 싶다 문제

    1) 정상에 올라가면 미끄러지지 않는다.
     : 최종목적지를 C-A로 설정하면, 미끄러지면서 가야하는 최종지를 설정할 수 있음
    
    2) 미끄러지면서 C-A까지 가는 횟수를 구함
*/

int main(void){
    long long A, B, C;
    long long answer = 0;
    cin >> A >> B >> C;

    C -= A;
    answer = C / (A-B);
    if( C % (A-B) != 0 ){
        answer ++;
    }
    answer ++; 
    cout << answer << endl;

    return 0;
}