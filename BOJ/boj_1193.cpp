#include <iostream>

using namespace std;

int main(void){
    long long X;
    cin >> X;

    long long row = 1;
    long long col = 1;
    long long target = 1;
    long long num =0 ;

    for(num=1; ;num++){
        target += num;
        // cout << target << endl;
        if( target > X){
            target -= num;
            break;
        }
    }

    // 몇번째 대각선에 있는지 구함
    // cout << num << endl;

    if( num % 2 == 0){  // 짝수번째 대각선
        row = 1;
        col = num;
    }
    else {
        row = num;
        col = 1;
    }
    // cout << row << " " << col << " " << target << endl;

    // 해당 대각선에서 정해진 방향으로 탐색하며 타겟을 찾음
    while( target != X ){
        target++;
        if( num % 2 == 0 ){
            col--;
            row++;
        }
        else {
            col++;
            row--;
        }
    }
    // cout << row << " " << col << " " << target << endl;

    cout << row << "/" << col << endl;

    return 0;
}