#include <string>
#include <vector>
#include <stack>

using namespace std;

int choose(vector<vector<int>>& board, int move); // 뽑기기계에서 인형을 뽑는 함수 

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int cur = 0;
    int pop_cnt = 0;

    stack<int> s;

    for( int i=0; i<moves.size(); i++){
        cur = choose(board, moves[i]-1); // moves의 값이 1부터 시작하기 때문에 -1 필요
        // printf("[check] %d", cur);

        if( cur == 0 ) continue;
        
        if(s.empty()){
            s.push(cur);
        }
        else{
            if( s.top() != cur ){
                s.push(cur);
            }
            else{ // 스택의 맨 위 인형과 현재 들어올 인형이 같다면, 스택에 푸쉬하지 않는다.
                s.pop();
                pop_cnt++;
            }
        }
    }

    answer = pop_cnt*2;
    // printf("\n%d\n", answer);

    return answer;
}

int choose(vector<vector<int>>& board, int move){
    /* c++에서는 참조자를 사용할 수 있음. 될 수 있으면 포인터 대신 참조자를 사용한다. */
    int ret=0;

    for ( int i=0; i<(board)[move].size(); i++ ){
        if( (board)[i][move] != 0 ){
            ret = (board)[i][move];
            (board)[i][move] = 0;
            return ret;
        }
    }
    return 0;
}

int main(void){

    vector<vector<int>> board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
    vector<int> moves = {1,5,3,5,1,2,1,4};

    solution(board,moves);

    return 0;
}


