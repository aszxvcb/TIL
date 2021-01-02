#include <stdio.h>
#include <vector>

using namespace std;

int n,m;
vector<int> v;

void DFS(int cnt, int max){
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
            // 비내림차순 체크
            if(i >= max){
                // 재귀호출 시 값 설정
                cnt++;
                v.push_back(i);
                max = i;

                DFS(cnt, max);
                
                // 호출종료 시 값 해제
                cnt--;
                v.pop_back();
            }
        }
    }
}

int main(void){
    
    int cnt = 0;
    int max = 0;
    scanf("%d %d", &n, &m);

    DFS(cnt, max);

    return 0;
}