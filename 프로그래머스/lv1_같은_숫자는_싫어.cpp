#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for(int i=0; i<arr.size(); i++){
        if( i==0 ){
            answer.push_back(arr[i]);
        }
        else if(answer[answer.size()-1] != arr[i]){
            answer.push_back(arr[i]);
        }
    }

    return answer;
}

int main(void){
    vector<int> arr = {4,4,4,3,3};
    vector<int> answer;

    answer = solution(arr);
    
    for( auto elem : answer){
        cout << elem;
    }

    return 0;
}