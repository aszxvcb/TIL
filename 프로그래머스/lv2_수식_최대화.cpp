#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

/*
    1. 가능한 연산자의 우선순위를 순열을 이용해서 미리 정의
    2. 식에서 정수와 연산자를 분리
    3. 우선순위에 맞게 연산자의 앞에서 부터 탐색 후
    4. 일치하는 게 있으면, 해당 연산자의 좌우와 연산 후, 결과를 해당 자리에 삽입
*/

long long solution(string expression) {
    long long answer = 0;

    // 수식에서 가능한 우선순위 결정
    // rank 에 가능한 경우의 수 저장
    vector<char> oper = {'+', '-', '*'};
    vector<vector<char>> rank;
    sort(oper.begin(), oper.end());
    do{ 
        rank.push_back(oper);
    }while(next_permutation(oper.begin(), oper.end()));

    for( auto elem : rank){
        for(auto oper : elem){
            cout << oper << " ";
        }
        cout << endl;
    }

    // 식에서 정수와 연산자를 분리
    vector<long long> num;
    vector<char> op;
    int i=0;
    do{
        if(expression[i] == '*' || expression[i] == '-' || expression[i] == '+'){
            op.push_back(expression[i]);

            num.push_back(stoi(expression.substr(0, i)));
            expression.erase(0,i+1);
            i=0;

            for( auto elem: expression){
                cout << elem << " ";
            }
            cout << endl;
        }
        i++;
    }while(i<expression.size());
    num.push_back(stoi(expression));

    for( auto elem: op){
        cout << elem << " ";
    }
    cout << endl;

    for( auto elem: num){
        cout << elem << " ";
    }
    cout << endl;

    // 식에서 우선순위를 검색하고 연산
    cout << "============" << endl;
    vector<long long> cur_num;
    vector<char> cur_op;
    vector<long long> result;
    long long cur_calc=0;
    for(int i=0; i<rank.size(); i++){
        cur_num = num;
        cur_op = op;
        for(int j=0; j<rank[i].size(); j++){
            for( int k=0; k<cur_op.size(); k++){
                if( cur_op[k] == rank[i][j] ){ // 일치하는 연산자를 발견하면
                    
                    switch(rank[i][j]){
                        case('+'):
                            cur_calc = cur_num[k] + cur_num[k+1];
                            break;
                        case('-'):
                            cur_calc = cur_num[k] - cur_num[k+1];
                            break;
                        case('*'):
                            cur_calc = cur_num[k] * cur_num[k+1];
                            break;
                    }

                    cur_op.erase(cur_op.begin()+k);
                    cur_num.erase(cur_num.begin()+(k+1));
                    cur_num.erase(cur_num.begin()+k);
                    
                    cur_num.insert(cur_num.begin()+k, cur_calc);

                    k=-1; // k를 인덱스로 되돌리기 위해

                    for( auto elem: cur_op){
                        cout << elem << " ";
                    }
                    cout << endl;

                    for( auto elem: cur_num){
                        cout << elem << " ";
                    }
                    cout << endl;

                    if( cur_num.size() == 1 ){ // 연산자가 존재하지 않을때 결과값이 잘못나오는 것을 방지
                        result.push_back(abs(cur_num[0]));
                    }
                }
            }
        }
    }

    for( auto elem : result){
        cout << elem << " ";
    }
    cout << endl;

    answer = *max_element(result.begin(), result.end());
    
    return answer;
}

int main(void){
    long long ret;
    string expression = "1+2-1";

    ret = solution(expression);
    cout << ret << endl;

    return 0;
}