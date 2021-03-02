#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

/*
    처음에는 글자의 길이 수만큼 정렬을 한 후, 짧은 수부터 선택해놓고 모든 배열을 탐색하여
    답을 찾는 방식을 택함.
    하지만 시간초과 발생. 이후 해시맵을 이용하여 문제해결 -> 수행 시간이 줄어들었나

    이후 답안을 보니, 그냥 사전순으로 정렬하고 인접한 문자열을 비교하는 방법으로 풀이가 가능함
    스트링을 대상으로 한 sort는 자동으로 사전순으로 정렬된다는 것을 기억하자.
*/

bool size_comp(string str1, string str2){
    if( str1.size() <= str2.size() ){
        return true;
    }
    return false;
}

bool solution(vector<string> phone_book) {
    bool answer = true;
    string str;
    string split_temp;

    unordered_map<string, int> hash_map;

    // sort(phone_book.begin(), phone_book.end(), size_comp);

    for(int i=0; i<phone_book.size(); i++){
        hash_map.insert(make_pair(phone_book[i], phone_book[i].size()));
    }

    // for( auto elem : m ){
    //     cout << elem.first << " " << elem.second << endl;
    // }

    for(auto i=hash_map.begin(); i!=hash_map.end(); i++){
        for(auto j=hash_map.begin(); j!=hash_map.end(); j++){
            if( i != j ){
                str = i->first;
                split_temp = j->first.substr(0,str.size());

                if( str == split_temp ){
                    return false;
                }

                // cout << str << " " << split_temp << endl;
            }
        }
    }   

    return answer;
}

int main(void){
    vector<string> phone_book = {"00","11"};
    bool ret;

    ret = solution(phone_book);
    cout << ret << endl;

    return 0;
}
