#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string number, int k) {
    string answer = "";

    int max_num = 0;
    int max_idx = -1;
    int min_num = 99;
    int min_idx = number.size()-1;
    string temp = "";

    // k 만큼 앞에서 탐색하면서 가장 큰 수를 찾고, 그 앞의 숫자를 지움
    for ( int i=0; i<=k ; i++){
        if( max_num < (int)number[i]-48 ) {
            max_num = (int)number[i]-48;
            max_idx = i;
        }
    }
    number.erase(0, max_idx);
    // cout << number << endl;

    // 남은 문자 중 작은 뒤에 문자보다 작은 문자 제거
    for( int j=0; j<k-max_idx; j++){
        min_num = 99;
        min_idx = number.size()-1;
        for (int i=0; i<=number.size()-2; i++){
            if( ((number[i]-48) < (number[i+1]-48)) && (min_num > number[i]-48) ){
                min_num = number[i] - 48;
                min_idx = i;
                break;
            }
        }
        number.erase(min_idx, 1);
    }

    // cout << number << endl;
    
    answer = number;

    return answer;
}

int main(void){
    string number = "12398785652387";
    // string number = "";
    int k = 6;
    string ret = "";

    ret = solution(number, k);

    cout << ret << endl;
    return 0;
}