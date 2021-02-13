#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int findIdx(vector<char>& arr, char a){
    int ret = 0;
    for (int i=0; i<arr.size(); i++){
        if( arr[i] == a){
            ret = i;
        }
    }
    return ret;
}

int solution(string name) {
    /*
        케이스   
            1) A 뭉치가 여러개인 경우     ex) BBAABBBBAAAB
            2) A 뭉치가 연결되어 있는 경우 ex) AAABBAAAAA , AAAAABBAAA
            3) A 가 마지막에 있는 경우 ex) BBAAAABBAAA
    */

    int answer = 0;

    vector<char> arr        = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    vector<char> revers_arr = {'A','Z','Y','X','W','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B'};
    
    // 1 step : 문자열 중 A가 연속인 뭉치 중, 가장 긴 뭉치 찾기
    
    int A_num=0, max_A_num=0;
    int startIdx=-1, max_startIdx=-1;
    int endIdx=-1, max_endIdx=-1;

    for (int idx=0; idx<name.length(); idx++){
        if( name[idx] == 'A' ){
            A_num++;
            if( startIdx == -1 && endIdx == -1){
                startIdx = idx;
            }
            else if( startIdx != -1 && endIdx != -1){
                startIdx = idx;
            }
        }
        if( name[idx+1] != 'A' ){
            if( startIdx != -1 && endIdx == -1){
                endIdx = idx;
                if( max_A_num < A_num ){
                    max_A_num = A_num;
                    max_startIdx = startIdx;
                    max_endIdx = endIdx;
                }
                A_num = 0;
                startIdx = -1;
                endIdx = -1;
            }
        }
    }

    // 2 step : 시작점에서 A까지 정방향으로 가는 거리와 정방향으로 가다 역방향으로 가는 거리 중 가까운 거리 찾기

    int distance = name.length();
    int tail_A_size = 0;
    if( name[name.length()-1] == 'A'){
        for( int i=name.length()-1; i>=0; i--){
            if( name[i] == 'A' ){
                tail_A_size++;
            }
            else{
                break;
            }
        }
    }

    if( max_A_num != 0){
        answer = min(name.length()-1-tail_A_size , ((max_startIdx-1) * 2) + (name.length()-1)-(max_endIdx) );
    }
    else {
        answer = name.length()-1;
    }
    
    // 4 step : 위/아래 횟수 계산
    for (int i=0; i<name.length(); i++){
        if( name[i] != 'A'){
            answer += min(findIdx(arr, name[i]), findIdx(revers_arr, name[i]));
        }
    }

    return answer;
}

int main(void){

    string name = "CANAAAAANAN";
    int ret;

    ret = solution(name);
    cout << ret << endl ;

    return 0;
}