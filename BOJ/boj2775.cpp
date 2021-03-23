#include <iostream>
#include <string>

using namespace std;

/*
    아파트를 초기화를 할 때, 0층의 모든 호와, 모든층의 1호를 초기화해준 후
    주어진 입력값을 하나씩 계산해서 리턴

    리턴값 = 이전 호 + 아래 층 같은 호 
*/

void print_apart(int apart[15][15]){
    for(int i=14; i >= 0; i--){
        for(int j=0; j < 15; j++){
            printf("%2d ", apart[i][j]);
        }
        cout << endl;
    }
}

int main(void){

    int num;
    cin >> num;
    
    int floor = 0;
    int room  = 1;
    int sum = 0;

    int apart[15][15] = {0,};
    for(int room=0; room<15; room++){
        apart[0][room] = room+1;
    }
    for(int floor=0; floor<15; floor++){
        apart[floor][0] = 1;
    }
    // print_apart(apart);

    for(int i=0; i<num; i++){
        cin >> floor >> room;
        int j=0, k=0;
        for(j=1; j<=floor; j++){
            for(k=1; k<room; k++){
                apart[j][k] = apart[j][k-1] + apart[j-1][k];
            }
        }
        // print_apart(apart);
        cout << apart[j-1][k-1] << endl;
    }

    return 0;
}