#include <iostream>
#include <string>

using namespace std;

/*
    손익분기점 문제
    
    판매이득이 A를 넘기게 되는 판매대수를 구하면 된다.
*/

int main(void){
    long long A, B, C;

    cin >> A >> B >> C;
    
    int num = 0;
    long long profit = 0;
    
    if ( B >= C ){
        num = -1;
    }
    else{
        // while(1){
        //     if( A + (B*num) < C*num ){
        //         break;
        //     }
        //     num ++;
        // }
        
        profit = C - B;
        num = A / profit + 1;
    }

    cout << num << endl;
}