#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

int main(void){
    
    int cnt = 0;
    string str;
    stringstream ss;

    getline(cin, str);
    ss.clear();
    ss << str;
    while(ss >> str){
        cnt++;
        // cout << str << endl;
    }

    cout << cnt << endl;
}