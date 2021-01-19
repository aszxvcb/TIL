#include <string>
#include <regex>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    vector<int> score;
    vector<char> bonus;
    vector<char> option;

    regex re("(\\d*)([SDT]{1})([*#]?)");
    smatch match;

    /* 문자열 전체가 패턴에 만족하는지 체크 */
    // cout << dartResult << ": " << boolalpha << regex_match(dartResult, re) << endl;
    /* 문자열에 패턴에 일치하는 부분이 있는지 체크 */
    // cout << dartResult << ": " << boolalpha << regex_search(dartResult, match, re) << endl;

    /* 반복문을 이용한 패턴 검색 */
    // while( regex_search(dartResult, match, re) ){
    //     cout << match.str() << endl;
    //     dartResult = match.suffix();
    // }
    // cout << match[0] << endl;

    /* 이터레이터를 이용한 패턴 검색 */
    auto start = sregex_iterator(dartResult.begin(), dartResult.end(), re);
    auto end = sregex_iterator();   // 인자를 넣지 않으면 끝을 가리키는 이터레이터 리턴

    while( start !=  end){
        // cout << start->str() << endl;
        // cout << (*start)[1] << endl;
        // cout << (*start)[2] << endl;
        // cout << (*start)[3] << endl;

        score.push_back( atoi( (*start)[1].str().c_str() ));
        bonus.push_back((*start)[2].str()[0]);
        option.push_back((*start)[3].str()[0]);

        ++start;
    }

    for( int i=0; i<bonus.size(); i++ ){
        if( bonus[i] == 'D' ){
            score[i] = (int)pow(score[i],2);
        }
        else if( bonus[i] == 'T' ){
            score[i] = (int)pow(score[i],3);
        }
    }

    for( int i=0; i<option.size(); i++){
        if( option[i] == '*' ){
            score[i-1] = score[i-1] * 2;
            score[i] = score[i] * 2;
        }
        else if( option[i] == '#' ){
            score[i] = score[i] * -1;
        }
    }

    for( int i=0; i<score.size(); i++ ){
        answer += score[i];
    }
    
    printf("[check]");

    return answer;
}

int main(void){

    string dartResult = "1S2D*3T";
    int answer;

    answer = solution(dartResult);
    
    printf("%d", answer);

    return 0;
}