#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> m;

    for( auto elem : participant ){
        m[elem]++;
    }

    for( auto elem : completion ){
        if( m.find(elem) != m.end() ){
            m[elem]--;
            if( m[elem] <= 0 ){
                m.erase(elem);
            }
        }
    }

    answer = (*(m.begin())).first;

    return answer;
}

int main(void){

    string ret;
    vector<string> participant = {"leo", "kiki", "eden", "leo"};
    vector<string> completion = {"eden", "kiki", "leo"};
    
    ret = solution(participant, completion);

    printf("%s\n", ret.c_str());

    return 0;
}