#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;

int image[64][64];
vector<char> result;

void DFS(int min_x, int min_y, int max_x, int max_y){
    // check
    // cout << min_x << " " << min_y << " " << max_x << " " << max_y << " " << endl;

    int num=image[min_x][min_y];
    bool same_check = true;

    /* 주어진 영역이 같은 색으로 채워져 있음을 체크 */
    for( int i=min_x; i<=max_x; i++){
        for( int j=min_y; j<=max_y; j++){
            if( num != image[i][j] ){
                same_check = false;
            }    
        }
    }

    /* 최소 크기 일 떄, 각각의 글자를 압축 */
    if( (abs(max_x - min_x) == 1 && abs(max_y - min_y) == 1) ){
        if( same_check == false ){
            result.push_back('(');

            if( image[min_x][min_y] == 1 ){
                result.push_back('1');
            }else { result.push_back('0');}

            if( image[min_x][max_y] == 1){
                result.push_back('1');
            }else { result.push_back('0');}

            if( image[max_x][min_y] == 1){
                result.push_back('1');
            }else { result.push_back('0');}

            if( image[max_x][max_y] == 1){
                result.push_back('1');
            }else { result.push_back('0');}

            result.push_back(')');
        }
        else{
            result.push_back(num+'0');
        }
    }
    /* 부분적으로 더 쪼개야 한다면, 재귀호출을 통해 영역 재지정 */
    else{
        if( same_check == false ){
            result.push_back('(');
            DFS( min_x, min_y, (min_x+max_x)/2 , (min_y+max_y)/2 );
            DFS( min_x, (min_y+max_y)/2+1, (min_x+max_x)/2, max_y );
            DFS( (min_x+max_x)/2+1, min_y, max_x, (min_y+max_y)/2);
            DFS( (min_x+max_x)/2+1, (min_y+max_y)/2+1, max_x, max_y);
            result.push_back(')');
        }
        else {
            result.push_back( num + '0' );
        }
    }
}

int main(void){

    int N;
    string str;
    cin >> N;

    for(int i=1; i<=N; i++){
        cin >> str;
        for(int j=1; j<=N; j++){
            image[i][j] = str[j-1]-'0';
        }
    }

    // cout << endl;

    // for(int i=1; i<=N; i++){
    //     for(int j=1; j<=N; j++){
    //         cout << image[i][j];
    //     }
    //     cout << endl;
    // }

    DFS(1,1,N,N);

    for( int i=0; i<result.size(); i++){
        cout << result[i];
    }

    return 0;
}