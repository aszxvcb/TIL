#include <iostream>

using namespace std;

/*
    x, y 가 0보다 큰지 작은지 확인 후,
    두자리의 비트를 이용하여 판별한다.
*/

int main(void){

    int x, y;
    int bit = 0;
    cin >> x >> y;

    if( x > 0 ){
        bit |= 2;
    }

    if( y > 0 ){
        bit |= 1;
    }

    if( bit == 0 ){
        cout << 3 << endl;
    }
    else if( bit == 1){
        cout << 2 << endl;
    }
    else if( bit == 2 ){
        cout << 4 << endl;
    }
    else if( bit == 3 ){
        cout << 1 << endl;
    }
    

    return 0;
}