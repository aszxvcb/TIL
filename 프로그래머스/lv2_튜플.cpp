#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

/*
    주어진 문자열을 split해서 vector 자료형으로 파싱
    vector 자료형을 각 항목의 사이즈를 기준으로 해서 정렬
    set을 이용해서 이전에 없던 항목을 찾고 answer에 추가

    나는 split을 이용했지만
    앞에서 부터 하나씩 탐색해서 { } 안의 숫자들을 벡터에 넣는 방법도 가능
*/

bool comp(vector<int> a, vector<int> b){
    return a.size() < b.size();
}

vector<int> solution(string s) {
    vector<int> answer;
    vector<int> temp;
    vector<vector<int>> tuple;

    // s split 해서 vector 에 넣기
    int current=0;
    int previous=0;
    int sub_cur=0;
    int sub_pre=0;

    string substring;
    string elem;

    s.erase(s.begin());
    s.erase(s.begin());
    s.erase(s.end()-1);
    s.erase(s.end()-1);
    
    current = s.find("},{");
    while( current != string::npos ){
        substring = s.substr(previous, current-previous);
        
        sub_cur=0;
        sub_pre=0;
        temp.clear();
        sub_cur = substring.find(",");
        while( sub_cur != string::npos ){
            elem = substring.substr(sub_pre, sub_cur-sub_pre);
            temp.push_back(stoi(elem));
            sub_pre = sub_cur + 1;
            sub_cur = substring.find(",", sub_pre);
        }
        temp.push_back(stoi(substring.substr(sub_pre, substring.size()-sub_pre)));
        tuple.push_back(temp);

        previous = current + 3;
        current = s.find("},{", previous);
    }
    substring = s.substr(previous, s.size()-current);
    sub_cur = substring.find(",");
    sub_pre = 0;
    temp.clear();
    while( sub_cur != string::npos ){
        elem = substring.substr(sub_pre, sub_cur - sub_pre );
        temp.push_back(stoi(elem));
        sub_pre = sub_cur + 1;
        sub_cur = substring.find(",", sub_pre);
    }
    temp.push_back(stoi(substring.substr(sub_pre, substring.size()-sub_pre)));
    tuple.push_back(temp);

    // for(vector<int> t : tuple ){
    //     for(int elem : t){
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }


    // vector 정렬
    sort(tuple.begin(), tuple.end(), comp);

    // for(vector<int> t : tuple ){
    //     for(int elem : t){
    //         cout << elem << " ";
    //     }
    //     cout << endl;
    // }

    // vector의 각 원소에 set 적용
    set<int> num_set;
    for(int i=0; i<tuple.size(); i++){
        for(int j=0; j<tuple[i].size(); j++){
            if(num_set.find(tuple[i][j]) == num_set.end()){
                answer.push_back(tuple[i][j]);
                num_set.insert(tuple[i][j]);
            }
        }
    }

    return answer;
}

int main(void){
    string s = "{{20,111},{111}}";
    vector<int> ret = solution(s);
    for(auto elem : ret ) {
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}