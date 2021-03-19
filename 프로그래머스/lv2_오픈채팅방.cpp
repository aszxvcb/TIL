#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <sstream>

using namespace std;

/*
    1. record를 접근하기 편하게 split하여 파싱
    2. Enter, Change일 경우 hashtable을 사용하여, uid에 따른 닉네임 수정 반영
    3. 전체 데이터를 순회하면서 필요한 데이터 출력.

    c++ 에는 string split()이 없음
    공백단위 구분은 stringstream을 이용하면 간결하게 구현 가능

    getline과 함께 이용하면 'token' 분리도 가능

    참고 : https://psychoria.tistory.com/666
*/

vector<string> solution(vector<string> record) {
    vector<string> answer;
    string str;
    vector<string> split;
    vector<vector<string>> vec_record;
    unordered_map<string, string> name_hash;
    string text;

    // record 파싱
    for(int i=0; i<record.size(); i++){
        split.clear();
        str.clear();

        // // 공백 단위로 분리 (처음 시도 방법)
        // for(int j=0; j<record[i].size(); j++ ){
        //     if(record[i][j] != ' '){
        //         str.push_back(record[i][j]);
        //     }
            
        //     if(record[i][j] == ' ' || j == record[i].size()-1 ){
        //         split.push_back(str);
        //         str.clear();
        //     }
        // }

        // stringstream 을 이용한 분리 (수정된 방법)
        stringstream ss(record[i]);
        while( ss >> str ){
            split.push_back(str);
        }

        vec_record.push_back(split);        
    }

    // for(int i=0; i<vec_record.size(); i++){
    //     for(int j=0; j<vec_record[i].size(); j++){
    //         cout << vec_record[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    for( int i=0; i<vec_record.size(); i++){
        if (vec_record[i][0] == "Enter"){
            name_hash[vec_record[i][1]] = vec_record[i][2];
        }
        else if( vec_record[i][0] == "Change" ){
            name_hash.find(vec_record[i][1])->second = vec_record[i][2];
        }
    }

    for( int i=0; i<vec_record.size(); i++){
        if ( vec_record[i][0] == "Enter"){
            text.clear();
            text.append(name_hash.find(vec_record[i][1])->second);
            text.append("님이 들어왔습니다.");
            answer.push_back(text);
        }
        else if (vec_record[i][0] == "Leave"){
            text.clear();
            text.append(name_hash.find(vec_record[i][1])->second);
            text.append("님이 나갔습니다.");
            answer.push_back(text);
        }
    }

    return answer;
}

int main(void){
    vector<string> record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
    vector<string> ret;

    ret = solution(record);
    
    for(string str : ret ){
        cout << str << endl;
    }

    return 0;
}

