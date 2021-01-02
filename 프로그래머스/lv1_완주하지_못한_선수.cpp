#include <string>
#include <vector>
#include <set>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";

    multiset<string> mset;

    for ( auto iter = participant.begin(); iter != participant.end(); iter++ ){
        mset.insert(*iter);
    }

    for ( auto iter = completion.begin(); iter != completion.end(); iter++){
        mset.erase(mset.find(*iter));
    }

    answer = *(mset.begin());

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