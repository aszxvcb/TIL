#include <string>
#include <vector>
#include <bitset>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<int> temp;
    vector<string> v_bitset;
    string bits;

    /* 비트연산 */
    for( int i=0; i<n; i++ ){
        temp.push_back(arr1[i] | arr2[i]);
    }

    /* bitset 이용하여 만들어진 16자리수를 n개로 저장 */
    for( int i=0; i<n; i++ ){
        bits = bitset<16>(temp[i]).to_string();
        v_bitset.push_back("");
        for(int j=16-n; j<16; j++){
            v_bitset[i].push_back(bits[j]);
        }
    }

    /* 비트 값을 확인하여 결과 도출 */
    for( int i=0; i<n; i++ ){
        answer.push_back("");
        for( int j=0; j<n; j++ ){
            if ( v_bitset[i][j] == '1' ){
                answer[i].push_back('#');
            }
            else{
                answer[i].push_back(' ');
            }
        }
    }

    return answer;
}

int main(void){
    int n = 5;
    vector<int> arr1 = {9,20,28,18,11};
    vector<int> arr2 = {30,1,21,17,28};
    vector<string> ret;

    ret = solution(n,arr1,arr2);

    return 0;
}