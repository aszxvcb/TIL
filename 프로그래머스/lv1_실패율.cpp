#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    multimap<float,int,greater<float>> m;
    int user_num = stages.size();
    int num1=0, num2=0;

    for(int i=1; i<=N; i++) {
        num1=0;
        num2=0;
        for(int j=0; j<stages.size(); j++){
            if( stages[j] >= i && stages[j] == i){
                num1++;
            }
            if( stages[j] >= i){
                num2++;
            }
        }

        m.insert( make_pair( (float(num1)/float(num2)), i) );
    }

    for( auto elem : m ){
        answer.push_back(elem.second);
    }

    return answer;
}

int main(void){
    int N = 5;
    vector<int> stages = {2,1,2,6,2,4,3,3};
    vector<int> ret;

    ret = solution(N, stages);

    return 0;
}