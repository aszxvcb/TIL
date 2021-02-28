#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

/*
    조합을 만든다.
    조합을 만들기위해서 bool 벡터를 만들고, 추출하고자 하는 갯수 만큼의 true를 데이터로 입력한다.
    bool 벡터에서 순열을 뽑아내면, true를 이용한 여러개의 순열이 나온다.
    이를 이용해서 마스킹을 걸면 combination 구현 가능

    중복을 방지하기 위해서는 sort를 해놓은 상태로 unique 함수를 사용한다.
    unique 함수는 "연속"된 숫자를 판단하여 해당 숫자를 맨뒤로 보내기 때문에 sort가 필요!
    리턴값으로 뒤로 보내진 숫자들의 시작점의 iter가 리턴된다.
    이를 이용하여 erase하면 unique 벡터를 얻을 수 있다.
*/
using namespace std;

int solution(string numbers) {
    int answer = 0;
    vector<int> elem;
    vector<int> combination;
    vector<bool> masking;
    string num;


    for (int i=0; i<numbers.size(); i++){
        elem.push_back(numbers[i]-'0');
        combination.push_back(numbers[i]-'0');
    }

    for (int j=1; j<=numbers.size(); j++){
        masking.clear();
        masking.insert(masking.end(), j, true);
        masking.insert(masking.end(), numbers.size()-j, false);
        sort(masking.begin(), masking.end());
        
        do{
            num = "";
            for(int i=0; i<masking.size(); i++){
                if( masking[i] ){
                    // cout << elem[i] << " ";
                    num.push_back(char(elem[i]) + '0');
                }                
            }
            // cout << endl;
            combination.push_back(stoi(num));
        } while(next_permutation(elem.begin(), elem.end()));
    }

    sort(combination.begin(), combination.end());

    combination.erase(unique(combination.begin(), combination.end()), combination.end());

    for (auto com : combination){
        cout << com << " ";
    }
    cout << endl;

    // 소수 판별
    for (int i=0; i<combination.size(); i++){
        for( int j=2; j<=combination[i]; j++){
            if( j == combination[i] ){
                // cout << combination[i] << endl;
                answer++;
            }

            if( combination[i] % j == 0 ){
                break;
            }
        }
    }

    return answer;
}

int main(void){
    string numbers = "222";
    int ret;

    ret = solution(numbers);
    cout << ret << endl; 

    return 0;
}