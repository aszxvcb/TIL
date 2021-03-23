#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(int H, int W, int N){
    string ret = "";
    int YY, XX;
    YY = N % H;
    XX = N / H + 1;
    
    if( YY == 0 ){
        YY = H;
        XX -= 1;
    }
    ret.append(to_string(YY));
    if( XX < 10 ){
        ret.append("0");
    }
    ret.append(to_string(XX));
    return ret;
}

int main(void){
    int T, H, W, N;
    vector<string> ret;
    cin >> T;

    for(int i=0; i<T; i++){
        cin >> H >> W >> N;
        ret.push_back( solution(H, W, N) );   
    }

    for( string str : ret ){
        cout << str << endl;
    }

    return 0;
}