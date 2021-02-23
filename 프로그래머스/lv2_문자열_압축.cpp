#include <string>
#include <vector>
#include <iostream>
#include <string.h>

using namespace std;

//todo 다시 풀어보기!

int solution(string s) {
    int answer = 0;
    int pos = 0;
    int loop_cnt = 0;
    vector<string> str_split;
    string cmp;
    string temp;
    vector<string> answer_tmp;
    int min_len=1000;
    
    if( s.length() == 1 ){
        return 1;
    }

    for( int i=1; i<s.length()/2+1; i++ ){
        while( pos < s.length() ){
            str_split.push_back(s.substr(pos,i));
            pos += i;
        }

        // for( auto elem : str_split){
        //     cout << elem << " " ;
        // }
        // cout << endl;
        
        for(int j=0; j<str_split.size(); j++){
            if( j == 0 ){
                cmp = str_split[j];
                loop_cnt = 0;
            }

            // cout << "[check] " << loop_cnt << " " << cmp << endl;

            if( str_split[j] != cmp ){
                if(loop_cnt != 1){
                   temp.append(to_string(loop_cnt));
                }
                temp.append(cmp);
                if( j == str_split.size()-1 ){
                    temp.append(str_split[j]);
                }
                cmp.clear();
                cmp = str_split[j];
                loop_cnt = 1;
            }
            else {
                loop_cnt++;
                if ( j == str_split.size()-1 ){
                    if(loop_cnt != 1){
                        temp.append(to_string(loop_cnt));
                    }
                    temp.append(cmp);
                }
            }
        }

        answer_tmp.push_back(temp);
        temp.clear();
        cmp.clear();
        pos = 0;
        while(!str_split.empty()){
            str_split.pop_back();
        }
    }

    for( auto elem : answer_tmp ){
        // cout << elem << endl;
        if( min_len > elem.length() ){
            min_len = elem.size();
        }
    }
    answer = min_len;
    return answer;
}

int main(void){
    string s = "a";
    int ret;

    ret = solution(s);
    cout << ret;

    return 0;
}