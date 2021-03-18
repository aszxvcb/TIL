//Todo 빈칸 내리는 부분에 문제가 있는 것 같음

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    bool deleteCheck;
    char target;
    bool visit[30][30] = {false,};

    do{
        for(int col=0; col<m; col++ ){
            for(int row=0; row<n; row++ ){
                cout << board[col][row];
            }
            cout << endl;
        }
        cout << endl;

        deleteCheck = false;
        // 지울 수 있는 블록을 체크
        for(int row=1; row < m; row++){
            for(int col=0; col < n-1; col++){
                target = board[row][col];

                if( target == board[row][col+1] &&
                    target == board[row-1][col] &&
                    target == board[row-1][col+1] &&
                    target != ' '
                    ){
                        visit[row][col] = true;
                        visit[row-1][col] = true;
                        visit[row][col+1] = true;
                        visit[row-1][col+1] = true;
                        deleteCheck = true;
                    }
            }
        }

        // for(int col=0; col<m; col++ ){
        //     for(int row=0; row<n; row++ ){
        //         cout << visit[col][row];
        //     }
        //     cout << endl;
        // }
        // cout << endl;


        // 지워야 하는 블록 지우고, 위에서 내리기
        for(int col=m-1; col>=0; col--){
            for(int row=0; row<n; row++){
                if( visit[col][row] == true){
                    for(int cur=col; cur >= 0; cur-- ){
                        if(board[cur][row] != ' ' && visit[cur][row] == false){
                            visit[col][row] = false;
                            board[col][row] = board[cur][row];
                            board[cur][row] = ' ';
                            answer ++;
                            
                            // cout << " 1 " << endl;
                            // for(int col=0; col<m; col++ ){
                            //     for(int row=0; row<n; row++ ){
                            //         cout << board[col][row];
                            //     }
                            //     cout << endl;
                            // }
                            // cout << endl;
                            
                            break;
                        }
                        if(cur == 0){
                            visit[col][row] = false;
                            board[col][row] = ' ';
                            answer ++;

                            // cout << " 2 " << endl;
                            // for(int col=0; col<m; col++ ){
                            //     for(int row=0; row<n; row++ ){
                            //         cout << board[col][row];
                            //     }
                            //     cout << endl;
                            // }
                            // cout << endl;

                        }
                    }
                }
            }
        }

        // 사이의 빈칸 없애기
        // 밑에서부터 탐색하고 위에서 가져와야함
        for(int col=m-1; col >= 0; col-- ){
            for(int row=0; row < n; row ++){
                if( board[col][row] == ' '){
                    for(int cur=col; cur>=0; cur--){
                        // 빈칸위에 문자가 있다면
                        if( board[cur][row] != ' '){
                            board[col][row] = board[cur][row];
                            board[cur][row] = ' ';
                            break;
                        }
                    }
                }
            }
        }

        // cout << "check" << endl;
        // for(int col=0; col<m; col++ ){
        //     for(int row=0; row<n; row++ ){
        //         cout << board[col][row];
        //     }
        //     cout << endl;
        // }
        // cout << endl;
    }
    while(deleteCheck == true);

    cout << answer << endl;;
    return answer;
}

int main(void){
    int m = 7;
    int n = 2;
    int ret;

    vector<string> board = {"AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"};
    ret = solution(m, n, board);

    // cout << ret << endl;
    
    return 0;
}