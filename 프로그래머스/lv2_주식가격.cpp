#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    int time = 0;
    bool input_check;

    for(int i=0; i<prices.size(); i++){
        time = 0;
        input_check = false;
        for( int j=i; j<prices.size(); j++){
            // 조건을 확인
            if( prices[i] > prices[j] || j == prices.size()-1 ){
                // 시간은 인덱스의 차이만큼으로 계산 가능
                time = j-i;
                answer.push_back(time);
                // cout << "time : " << time << endl;
                input_check = true;
                break;
            }
        }
    }

    return answer;
}

int main(void){
    vector<int> prices = {1,2,3,2,3};
    vector<int> ret;

    ret = solution( prices );
    
    for( auto elem: ret){
        cout << elem << " " ;
    }
    cout << endl;

    return 0;
}