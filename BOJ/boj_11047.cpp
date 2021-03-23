#include <vector>
#include <iostream>

using namespace std;

int solution(int target, vector<int> &coin){
    int answer = 0;
    int money = target;
    int num = 0;

    for( int idx=coin.size()-1; idx >= 0; idx-- ){
        if( money >= coin[idx] ){
            num = money / coin[idx];
            money -= coin[idx] * num;
            answer += num;
            // cout << "check " << coin[idx] << " " << money << endl;
        }

        if( money == 0 ){
            break;
        }
    }

    return answer;
}

int main(void){

    int n, target;
    int input;
    int ret;
    vector<int> coin;
    cin >> n >> target;

    for(int i=0; i<n; i++){
        cin >> input;
        coin.push_back(input);
    }

    ret = solution(target, coin);
    cout << ret << endl;

    return 0;
}