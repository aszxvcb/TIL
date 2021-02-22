#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int num=0;
    int size = progresses.size();

    while( !progresses.empty() ){
        for(int i=progresses.size()-1; i>=0; i--){
            progresses[i] += speeds[i];

            // 맨앞 원소가 100보다 커지면, 앞에서부터 차례로 100이상인 수를 체크함
            if( progresses.front() >= 100 ){
                num=0;
                while( !progresses.empty() && progresses.front() >= 100 ){
                    num++;
                    progresses.erase(progresses.begin());
                    speeds.erase(speeds.begin());
                }
                answer.push_back(num);
            }
        }
    }
 
    return answer;
}

int main(void){
    vector<int> progresses = {95, 90, 99, 99, 80, 99};
    vector<int> speeds = {1, 1, 1, 1, 1, 1};   
    vector<int> ret;

    ret = solution(progresses, speeds);

    for(int i=0; i<ret.size(); i++){
        cout << ret[i] << " " ;
    }
    cout << endl;

    return 0;
}