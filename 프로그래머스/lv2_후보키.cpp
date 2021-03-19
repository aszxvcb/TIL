#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

/*
    1. 가능한 조합 모두 찾기
    2. 슈퍼키 찾기 / 유일성 만족하는 키 조합 찾기
    3. 후보키 찾기 / 유일성, 최소성 만족하는 키 조합 찾기

    next_permutation을 이용한 순열, 조합 방법과
    비트연산을 이용한 방법이 있음.

    비트연산을 이용하면 쉽게 풀리는 문제가 몇몇 있다. 연습해서 대비하자

    팁 : includes() 를 이용하면 최소성을 판단할 수 있음
    https://medium.com/newworld-kim/c-std-includes-%EB%BD%80%EA%B0%9C%EA%B8%B0-fef4a34edc5e
*/

bool cmp(vector<int> a, vector<int> b){
    if( a.size() < b.size()){ return true; }
    else if( a.size() == b.size() ){
        for(int i=0; i<a.size(); i++){
            if( a[i] < b[i] ){
                return true;
            }
            else if( a[i] > b[i] ){
                return false;
            }
            else {
                continue;
            }
        }
        return true;
    }
    else {
        return false;
    }
}

int solution(vector<vector<string>> relation) {
    int answer = 0;
    int rowsize = relation.size();
    int colsize = relation[0].size();
    set<string> s;
    
    vector<int> temp;
    vector<vector<int>> combination;
    vector<vector<int>> superkey;
    vector<vector<int>> candidatekey;

    // 가능한 조합
    for(int bit=1, size=1<<colsize; bit < size; bit++){
        // 0000, 0001, 0010, 0011, 0100 ...
        temp.clear();
        int num = 1 << (colsize-1);
        for(int cnt=0; cnt<colsize; cnt++){
            if( bit & (num >> cnt)){
                // cout << cnt << " ";
                temp.push_back(cnt);
            }
        }
        // cout << endl;
        combination.push_back(temp);
    }

    sort(combination.begin(), combination.end(), cmp);
    
    cout << "가능한 조합의 키" << endl;
    for( auto iter : combination){
        for( auto elem : iter ){
            cout << elem << " ";
        }
        cout << endl;
    }

    // 유일성 체크
    for(int i=0; i<combination.size(); i++){
        bool check = true;
        string str;
        s.clear();
        
        for(int row=0; row<rowsize; row++){
            str = "";
            for(int j=0; j<combination[i].size(); j++){
                str.append(relation[row][combination[i][j]]);
            }
            // cout << str << endl;
            auto ret = s.insert(str);
            if( ret.second == false ){
                check = false;
                break;
            }
        }

        if( check == true ){
            superkey.push_back(combination[i]);
        }
    }

    // cout << "슈퍼키" << endl;
    // for(auto iter : superkey){
    //     for(auto elem : iter ){
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }

    // 최소성 체크
    for(int i=0; i<superkey.size(); i++){
        bool check = true;
        for(int j=0; j<candidatekey.size(); j++){
            if ( includes(superkey[i].begin(), superkey[i].end(), candidatekey[j].begin(), candidatekey[j].end()) ){
                check = false;    
            }
        }
        if( check == true ){
            candidatekey.push_back(superkey[i]);
        }
    }

    // cout << "후보키" << endl;
    // for(auto iter : candidatekey){
    //     for(auto elem : iter ){
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }

    return answer = candidatekey.size();
}

int main(void){
    int ret;
    vector<vector<string>> relation = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","4"},{"500","muzi","music","3"},{"600","apeach","music","2"}};
    // vector<vector<string>> relation = {{"a","b","c"}, {"1","b","c"}, {"a","b","4"}, {"a","5","c"}};

    ret = solution(relation);
    cout << ret << endl;

    return 0;
}