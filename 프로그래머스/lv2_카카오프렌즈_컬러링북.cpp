// 프로그래머스 컬러링북
// BFS를 이용한 제대로 된 풀이.
// picture 에서 주변에 있는 같은 색을 한번에 탐색할때 BFS 사용
#include <vector>
#include <iostream>
#include <queue>
#include <unistd.h>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    queue<pair<int,int>> q;
    int cnt=0;
    int color=0;
    int cx[4] = {0,0,1,-1};
    int cy[4] = {1,-1,0,0};
    int pos_x, pos_y;
    int size_of_one_area[10001] = {0,};

    // 미방문 픽셀은 -로 체크
    for( int i=0; i<m; i++ ){
        for( int j=0; j<n; j++){
            picture[i][j] = -picture[i][j];
        }
    }

    for( int i=0; i<m; i++ ){
        for( int j=0; j<n; j++){
            pos_x = i;
            pos_y = j;
            if( picture[i][j] < 0 ){
                cnt++;
                // cout << cnt << endl;
                q.push(make_pair(i,j));
                color = -picture[i][j];
                picture[i][j] = cnt;
                while( !q.empty() ){
                    // cout << q.front().first << " " << q.front().second << " " << endl;
                    q.pop();
                    for(int k=0; k<4; k++){
                        if( pos_x+cx[k]>=0 && pos_x+cx[k]<m && pos_y+cy[k]>=0 && pos_y+cy[k]<n ){
                            if( color == -picture[pos_x+cx[k]][pos_y+cy[k]] ){
                                q.push(make_pair(pos_x+cx[k], pos_y+cy[k])); // 상하좌우에 있는 같은 색의 좌표를 큐에 추가함
                                picture[pos_x+cx[k]][pos_y+cy[k]] = cnt;    // 방문노드를 표시
                                // cout << "check " << pos_x+cx[k] << " " << pos_y+cy[k] << endl;
                            }
                        }
                    }
                    pos_x = q.front().first;
                    pos_y = q.front().second;
                }
            }
        }
    }

    number_of_area = cnt;
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if( picture[i][j] != 0 ){
                size_of_one_area[picture[i][j]]++;
                if( max_size_of_one_area < size_of_one_area[picture[i][j]]){
                    max_size_of_one_area = size_of_one_area[picture[i][j]];
                }
            }
        }
    }

    // for(int i=0; i<m; i++){
    //     for(int j=0; j<n; j++){
    //         cout << picture[i][j];
    //     }
    //     cout << endl;
    // }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

int main(void){
    int m=7;
    int n=7;
    vector<vector<int>> picture = {{0,1,1,0,1,0,0},
                                    {0,1,1,0,1,0,1},
                                    {1,1,1,0,1,0,1},
                                    {0,0,0,0,1,1,1},
                                    {0,1,0,0,0,0,0},
                                    {0,1,1,1,1,1,0},
                                    {0,1,1,1,0,0,0}};
    
    vector<int> ret;

    ret = solution( m, n, picture);

    cout << ret[0] << " " << ret[1] << endl;

    return 0;
}