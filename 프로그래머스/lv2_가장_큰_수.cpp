#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

/*
    처음 시도는 가능한 모든 순열을 만든 후, 만들어진 순열 중 최대값을 찾아내어 리턴하는 방식
    하지만, 답안제출시 시간초과 에러 발생
    많은 입력값이 들어왔을 떄, 시간복잡도가 크기 때문으로 보임

    sort()를 이용해서 str끼리의 크기 비교를 하면, 가장 큰 수를 만들 수 있는 numbers 를 얻을 수 있음.
    { 0, 0, 0, 0 } 이 들어올 떄의 예외를 처리해줌
*/

/*
string solution(vector<int> numbers) {
    string answer = "";
    vector<string> combination;
    string str;
    string max = "0";
    
    sort(numbers.begin(), numbers.end());

    do{
        str = "";
        for(int i=0; i<numbers.size(); i++ ){
            str.append(to_string(numbers[i]));
        }
        
        combination.push_back(str);
        cout << str << endl;

        if( max < str ){
            max = str;
        }

    }while ( next_permutation(numbers.begin(), numbers.end()) );

    while( max[0] == '0' && max.size() > 1){
        // cout << max[0] << " " << max.size() << endl;
        max.erase(0,1);
    }

    answer = max;

    return answer;
}
*/

bool comp(int str1, int str2){
    if( to_string(str1)+to_string(str2) > to_string(str2)+to_string(str1) ){
        return true;
    }
    else{
        return false;
    }
}

string solution(vector<int> numbers){
    string answer = "";

    sort(numbers.begin(), numbers.end(), comp);

    if ( numbers[0] == 0 ){
        return "0";
    }

    for (auto elem : numbers ){
        answer.append(to_string(elem));
    }

    return answer;
}

int main(void){
    vector<int> numbers = {0,0,0,0};
    string ret;

    ret = solution(numbers);

    cout << ret;
    return 0;
}