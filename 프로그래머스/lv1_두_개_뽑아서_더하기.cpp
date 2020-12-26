#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <set>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    set<int> result;
    vector<int> answer;
    set<int>::iterator it;
    
    for( int i=0; i<numbers.size(); i++){
        for ( int j=0; j<numbers.size(); j++){
            if( i != j ){
                result.insert(numbers[i] + numbers[j]);
            }
        }
    }

    for( it=result.begin(); it!=result.end(); it++ ){
        answer.push_back(*it);
    }

    // for ( auto v_it = answer.begin(); v_it != answer.end(); v_it++ ) {
    //     printf("%d ", *v_it);
    // }

    return answer;
}


int main(void){

    vector<int> numbers = {2,1,3,4,1};

    solution(numbers);

    return 0;
}