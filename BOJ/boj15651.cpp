#include <stdio.h>
#include <vector>

using namespace std;

int n,m;
int visit[10];  // 방문 노드 확인
vector<int> v;

void DFS(int cnt){
    // 출력
    if( cnt == m){
        for(int i=0; i<v.size(); i++){
            printf("%d ", v[i]);
        }
        printf("\n");
        return ;
    }
    // 재귀호출을 통한 DFS
    else{
        for(int i=1; i<=n; i++){
            // 재귀호출 시 값 설정
            visit[i] = true;
            cnt++;
            v.push_back(i);

            DFS(cnt);
            
            // 호출종료 시 값 해제
            visit[i] = false;
            cnt--;
            v.pop_back();
        }
    }
}

int main(void){
    
    int cnt = 0;
    scanf("%d %d", &n, &m);

    DFS(cnt);

    return 0;
}