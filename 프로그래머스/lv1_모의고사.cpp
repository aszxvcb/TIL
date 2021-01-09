#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> std1 = {1,2,3,4,5};
    vector<int> std2 = {2,1,2,3,2,4,2,5};
    vector<int> std3 = {3,3,1,1,2,2,4,4,5,5};

    vector<int> score(3);
    int max = 0;

    for( int i=0; i<answers.size(); i++ ){
        /* std의 원소 갯수를 생각해서 % 연산 */
        if(answers[i] == std1[i%5]){score[0]++;}
        if(answers[i] == std2[i%8]){score[1]++;}
        if(answers[i] == std3[i%10]){score[2]++;}
    }

    if( score.empty() != true ){
        /* score 벡터에서 가장 높은 점수를 취득 */
        max = *max_element(score.begin(), score.end());
        
        /* 가장 높은 점수를 가진 사람 확인 */
        for ( int i=0; i<score.size(); i++ ){
            if( max == score[i] ){
                answer.push_back(i+1);
            }
        }
    }

    return answer;
}

int main(void){
    
    vector<int> answers = {1,3,2,4,2};
    vector<int> ret;

    ret = solution(answers);

    for( auto elem : ret ){
        cout << elem << endl;
    }

    return 0;
}