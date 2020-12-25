#include <stdio.h>

int main(void){

    int row=0, col=0;
    char board[50][50] = {0,};
    char tmp;
    int r_start=0, c_start=0, count1=0, count2=0, min=999999;
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

    // for(int i=0; i<row; i++){
    //     for (int j=0; j<col; j++){
    //         printf("%c ", board[i][j]);
    //     }
    //     printf("\n");
    // }

    /* 전체 체스판에서 8*8 부분 체스판을 취함 */
    for(int i=0; i<=row-8; i++){
        for(int j=0; j<=col-8; j++){
            check = board[i][j]; // 부분 체스판의 맨왼쪽위 칸의 색
            /* 8*8 부분 체스판에서 색이 다른 부분의 갯수를 확인 */
            for(int k=0; k<8; k++){
                for (int l=0; l<8; l++){
                    if ( k%2==0 && l%2==0 ){
                        if( board[i+k][j+l] != check ){ // 맨 왼쪽위 색으로 시작한 체스판
                            // printf("[check1 %c] %c \n", check, board[i+k][j+l]);
                            count1++;
                        }
                        else{   // 반대의 경우 체스판
                            count2++;
                        }
                    }
                    else if( k%2==0 && l%2==1 ) {
                        if( board[i+k][j+l] == check ){
                            // printf("[check2 %c] %c \n", check, board[i+k][j+l]);
                            count1++;
                        }
                        else{
                            count2++;
                        }
                    }
                    else if( k%2==1 && l%2==0 ) {
                        if( board[i+k][j+l] == check ){
                            // printf("[check3 %c] %c \n", check, board[i+k][j+l]);
                            count1++;
                        }
                        else{
                            count2++;
                        }
                    }
                    else if( k%2==1 && l%2==1 ) {
                        if( board[i+k][j+l] != check ){
                            // printf("[check4 %c] %c \n", check, board[i+k][j+l]);
                            count1++;
                        }
                        else{
                            count2++;
                        }
                    }
                }
            }
            // printf("[check] %d %d\n", count1, count2);
            if( count1 <= count2 ){
                if( min > count1 ){
                    min = count1;
                }    
            }
            else{
                if( min > count2 ){
                    min = count2;
                }
            }
            count1 = 0;
            count2 = 0;
        }
    }

    printf("%d\n", min);

    return 0;
}
