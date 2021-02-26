#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool visit[200];
int cnt;

void DFS(vector<vector<int>>& computers, int n){

    if( visit[n] == false ){
        visit[n] = true;
        
        // 연결된 네트워크 탐색
        for ( int i=0; i<computers[n].size(); i++){
            if( computers[n][i] == 1 && i != n ){
                DFS(computers, i);
            }
        }
    }

}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for(int i=0; i<n; i++){
        if( visit[i] == false ){
            cnt++; // 새로운 네트워크를 탐색할때마다, cnt 상승
            DFS(computers, i);
        }
    }

    answer = cnt;
    
    return answer;
}

int main(void){
    int n = 3;
    vector<vector<int>> computers = {{1,1,0}, {1,1,0}, {0,0,1}};
    int ret;

    ret = solution(n, computers);

    cout << ret;

    return 0;
}