#include <iostream>

using namespace std;

/*
    MM 에서 45를 빼는데, 이때 45보다 낮은 수라면, HH도 함께 감소해야함
    시간이 0 에서 -1이 되면 24시로 돌아가서 -1을 해줘야함
*/

int main(void){

    int HH, MM;
    bool hour_flag = false;

    cin >> HH >> MM;
    
    if( MM >= 45 ){
        MM -= 45;
    }
    else {
        hour_flag = true;
        MM = 60 + ( MM - 45 );
    }

    if( hour_flag == true ){
        HH -= 1;
    }

    if( HH < 0 ){
        HH = 24 - ( 0 - HH );
    }

    cout << HH << " " << MM << endl;

    return 0;
}