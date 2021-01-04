#include <stdio.h>
#include <vector>
#include <stdlib.h>

using namespace std; 

int n;
int cnt;
vector<int> v_col; // 놓여진 Q를 저장, v_col[row-1]로 row에 놓여진 Q의 col 리턴

bool promising(int row, int col){
    for( int v_row=0; v_row<v_col.size(); v_row++ ){
        // printf("[compare] (%d,%d) (%d,%d)\n", i+1, v_col[i], row, col);
        /* 같은 열 또는 대각선 위에 있는 지 확인 */
        if(v_col[v_row] == col || abs(v_col[v_row]-col) == abs((v_row+1)-row)){
            // printf("[false] %d\n", col);
            return false;
        }
    }
    // printf("[true] %d\n", col);
    return true;
}

/* row에서 가능한 Q의 col을 찾는 함수 */
void nqueen(int row){
    if( row > n ){
        cnt++;
        return ;
    }
    
    for(int col=1; col<=n; col++){
        if(promising(row, col)){
            // printf("[check] row %d col %d\n", row, col);
            v_col.push_back(col);
            nqueen(row+1);
            v_col.pop_back();
        }
    }
    return ;
}

int main(void){

    scanf("%d", &n);

    nqueen(1);

    printf("%d\n", cnt);

    return 0;
}