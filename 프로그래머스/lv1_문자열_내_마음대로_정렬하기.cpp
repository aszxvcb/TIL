#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int global_n;

bool cmp(string a, string b){

    if (a[global_n] < b[global_n])
        return true;
    else if ( a[global_n] == b[global_n] ){
        if( a <= b ){
            return true;
        }
        else {
            return false;
        }
    }
    else{
        return false;
    }
}

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    global_n = n;

    sort(strings.begin(), strings.end(), cmp);

    answer = strings;

    return answer;
}

int main(void){

    vector<string> strings = {"abce", "abcd", "cdx"};
    int n = 1;

    vector<string> ret;
    ret = solution(strings, n);

    for( string elem : ret ){
        cout << elem << " ";
    }

    return 0;
}