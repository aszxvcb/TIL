#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    // 대문자로 변환 
    for(char c : new_id){
        c = tolower(c);
        // 특정문자만 선택 
        if( ('a' <= c && c <= 'z') || ('0' <= c && c <= '9') || c == '-' || c == '_' || c == '.' ){
            // 마침표가 2번 이상 연속이라면 삭제
            if ( !(answer.back() == '.' && c == '.') ){
                answer.push_back(c);
            }
        }
    }

    // 마침표가 처음이나 끝에 위치한다면 제거
    if ( answer.front() == '.' ){
        answer.erase(answer.begin());
    }
    if ( answer.back() == '.'){
        answer.erase(answer.end()-1);
    }
    // 빈문자열이라면 a 추가
    if ( answer.empty() ){
        answer.push_back('a');
    }

    // 길이가 16자 이상이면, 처음 15개의 문자를 제외한 나머지 문자열을 제거
    if ( answer.size() >= 16 ){
        answer.erase(answer.begin()+15, answer.end());
        // 제거한 문자열의 마지막이 . 이라면 제거
        if ( answer.back() == '.' ){
            answer.erase(answer.end()-1);
        }
    }
    
    // 문자열의 길이가 2보다 작다면, 길이가 3이 될때까지 뒤에 추가
    while (answer.size() <= 2){
        answer.push_back( answer.back() );
    }

    return answer;
}

int main(void){

    string new_id = "...!@BaT#*..y.abcdefghijklm";
    string ret;

    ret = solution(new_id);

    cout << ret << endl;
}