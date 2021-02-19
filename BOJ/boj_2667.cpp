// boj 2667
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

vector<pair<int, vector<pair<int, int>>>> group;

bool compare(int i, int j){
    return i<j;
}

void addGroup(int x, int y, vector<vector<int>> picture){
    int color = picture[x][y];
    vector<pair<int, int>> temp;
    bool check=false;
    vector<int> check_idx;
    if( group.empty() ){
        temp.push_back(make_pair(x,y));
        group.push_back(make_pair(color, temp));
    }
    else{
        for(int i=0, group_size=group.size(); i<group_size; i++){
            pair<int, vector<pair<int, int>>>& selected_group = group[i];
            int selected_color = selected_group.first;
            vector<pair<int,int>>& arr = selected_group.second;
            if( color == selected_color ){
                for(int j=0, arr_size=arr.size(); j<arr_size; j++){
                    if( arr[j].first == x-1 && arr[j].second == y){
                        if( !check ){
                          arr.push_back(make_pair(x,y));
                        }
                        check = true;
                        check_idx.push_back(i);
                        break;
                    }
                    // else if( arr[j].first == x && arr[j].second == y+1){
                    //    if( !check ){
                    //       arr.push_back(make_pair(x,y));
                    //     }
                    //     check = true;
                    //     check_idx.push_back(i);
                    //     break;
                    // }
                    // else if( arr[j].first == x+1 && arr[j].second == y){
                    //     if( !check ){
                    //       arr.push_back(make_pair(x,y));
                    //     }
                    //     check = true;
                    //     check_idx.push_back(i);
                    //     break;
                    // }
                    else if( arr[j].first == x && arr[j].second == y-1){
                        if( !check ){
                          arr.push_back(make_pair(x,y));
                        }
                        check = true;
                        check_idx.push_back(i);
                        break;
                    }
                }
            }
        }
        // 새로운 그룹 생성
        if(!check){
          temp.push_back(make_pair(x, y));
          group.push_back(make_pair(color, temp));
        }
        // 반복문 진행방향으로 인해 그룹에 추가되지 못한 케이스 처리
        // 0101
        // 1101
        // 0111
        // 의 경우 그룹이 나눠져 있게되는데, 이를 하나의 그룹으로 합쳐준다.
        else if(check && check_idx.size()==2){
          pair<int,int> tmp_pos;
          for(int i=0, size=group[check_idx[1]].second.size(); i<size; i++){
            tmp_pos = group[check_idx[1]].second[i];
            group[check_idx[0]].second.push_back(tmp_pos);
          }
          group.erase(group.begin()+check_idx[1]);
          check_idx.clear();
        }
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    group.clear();

    for( int i=0; i<m; i++){
        for ( int j=0; j<n; j++){
            if( picture[i][j] != 0 ){
                addGroup(i, j, picture);
            }
        }
    }
    
    number_of_area = group.size();
    for(int i=0; i<group.size(); i++){
        if(max_size_of_one_area < (group[i].second).size() ){
            max_size_of_one_area = (group[i].second).size();
        }
    }

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

    cin >> m;
    n = m;
    string str;
    picture.clear();

    for(int i=0; i<m; i++){
        cin >> str;
        vector<int> tmp_v;
        for(int j=0; j<str.size(); j++){
            tmp_v.push_back(str[j]-'0');
        }
        picture.push_back(tmp_v);
    }

    ret = solution( m, n, picture);

    cout << ret[0] << endl;

    vector<int> size_ret;
    for(int i=0; i<group.size(); i++){
        size_ret.push_back(group[i].second.size());
    }
    sort(size_ret.begin(), size_ret.end(), compare);
    for(int i=0; i<size_ret.size(); i++){
        cout << size_ret[i] << endl;
    }

    // for(int i=0; i<group.size(); i++){
    //     cout << "color : " << group[i].first << endl;
    //     for( int j=0; j<(group[i].second).size(); j++){
    //         cout << "(" << (group[i].second)[j].first << " " << (group[i].second)[j].second << ") ";
    //     }
    //     cout << endl;
    // }

    return 0;
}