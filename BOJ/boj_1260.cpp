#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<int> graph[1000];
bool dfs_visit[1000];
bool bfs_visit[1000];
queue<int> q;

void DFS(int vertex){
    cout << vertex << " ";
    dfs_visit[vertex] = true;
    for( int i=0; i<graph[vertex].size(); i++ ){
        // cout << "[check] " << graph[vertex][i] << " " << endl;
        if( dfs_visit[ graph[vertex][i] ] == false ){
            DFS(graph[vertex][i]);
        }
    }
}

void BFS(int vertex){
    int idx;
    q.push(vertex);
    bfs_visit[vertex] = true;
    
    while( !q.empty() ){
        idx = q.front();
        cout << idx << " ";
        q.pop();
        for(int i=0; i<graph[idx].size(); i++){
            if( bfs_visit[ graph[idx][i] ] == false ){
                q.push( graph[idx][i] );
                bfs_visit[graph[idx][i]] = true;
            }
        }
    }
}

int main(void){
    int N, M, V;
    int v, e;

    cin >> N >> M >> V;

    for (int i=0; i<M; i++){
        cin >> v >> e;
        graph[v].push_back(e);
        graph[e].push_back(v);
    }

    for (int i=1; i<N; i++){
        sort(graph[i].begin(), graph[i].end());
    }

    DFS(V);
    
    cout << endl;
   
    BFS(V);

    return 0;
}