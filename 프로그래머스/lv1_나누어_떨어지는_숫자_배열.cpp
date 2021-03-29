#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    
    for(int elem : arr){
        if( elem % divisor == 0){
            answer.push_back(elem);
        }
    }
    
    sort(answer.begin(), answer.end());
    
    if ( answer.empty() ){
        answer.push_back(-1);
    }
    return answer;
}