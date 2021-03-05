#include <string>
#include <vector>
#include <iostream>

using namespace std;

/*
    전체 타일크기를 만족할 순서쌍 (가로크기, 세로크기)를 찾은 후
    조건에 맞는 지 확인해보기.
*/

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int total = brown + yellow;
    int num;
    int side;
    vector<pair<int,int>> possible;

    for(int i=total; i>0; i-- ){
        if( total % i == 0){
            num = total / i;
            if( i>=num ){
                possible.push_back(make_pair(i, num));
            }
        }
    }

    // for(auto elem : possible){
    //     cout << elem.first << " " << elem.second << endl;
    // }

    for(int i=0; i<possible.size(); i++ ){
        side = ((possible[i].first + possible[i].second) - 1 ) * 2 - 2;
        if( side == brown ){
            answer.push_back(possible[i].first);
            answer.push_back(possible[i].second);
            return answer;
        }
    }

    return answer;
}

int main(void){

    vector<int> ret;

    ret = solution(24, 24);
    
    for(int i=0; i<ret.size(); i++){
        cout << ret[i] << " ";
    }
    cout << endl;

    return 0;
}