#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

const string b_chess[8] = {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
    };

    const string w_chess[8] = {
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
    };

int main(void){

    int row=0, col=0;
    char board[50][50] = {0,};
    char tmp;
    int r_start=0, c_start=0, count1=0, count2=0, min_result=999999;
    char check;

    scanf("%d %d\n", &row, &col);
    for(int i=0; i<row; i++){
        for( int j=0; j<col; j++){
            while(1){
                tmp = getchar();
                if (tmp != '\n'){
                    board[i][j] = tmp;
                    break;
                }
            }
        }
    }

    /* 전체 체스판에서 8*8 부분 체스판을 취함 */
    for(int i=0; i<=row-8; i++){
        for(int j=0; j<=col-8; j++){
            check = board[i][j]; // 부분 체스판의 맨왼쪽위 칸의 색
            /* 8*8 부분 체스판에서 색이 다른 부분의 갯수를 확인 */
            for(int k=0; k<8; k++){
                for (int l=0; l<8; l++){
                    if( board[i+k][j+l] != b_chess[k][l] ){ count1++; }
                    if( board[i+k][j+l] != w_chess[k][l] ){ count2++; }
                }
            }
            // printf("[check] %d %d\n", count1, count2);
            if (min_result > min(count1, count2)){
                min_result = min(count1, count2);
            }
            count1 = 0;
            count2 = 0;
        }
    }

    printf("%d\n", min_result);

    return 0;
}