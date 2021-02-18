#include <iostream>
#include <algorithm> 
#include <vector>

using namespace std;

vector<int> network[100];
bool visit[100];
int num;

void BFS(int i){
    if( visit[i] != 1 ){
        visit[i] = 1;
        // cout << "check " << i << endl;
        num++;
        for(int j=0; j< network[i].size(); j++ ){
            BFS(network[i][j]);
        }
    }
}

int main(void){

    int N;
    int connection;
    int A, B;

    cin >> N;
    cin >> connection;    

    for( int i=0; i<connection; i++){
        cin >> A >> B;
        network[A].push_back(B);
        network[B].push_back(A);
    }

    // // 입력 확인
    // cout << endl;
    // for (int i=0; i<100; i++){
    //     if( network[i].size() != 0){
    //         cout << i << " : ";
    //         for(auto elem : network[i]){
    //             cout << elem << " ";
    //         }
    //         cout << endl;
    //     }
    // }

    BFS(1);

    cout << num-1;

    return 0;
}