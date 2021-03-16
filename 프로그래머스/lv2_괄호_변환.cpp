#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

/*
    stack을 이용하여 ( ) 의 짝을 맞춰주는 문제
    재귀를 이용하여 주어진 순서에 맞게 문제를 해결한다.
 */

bool CollectCheck(string p){
    stack<char> check;
    for(int i=0; i<p.size(); i++ ){
        if( check.size() >= 1){
            if( check.top() == '(' && p[i] == ')' ){
                check.pop();
                continue;
            }
            // else if( check.top() == ')' && p[i] == '('){
            //     check.pop();
            //     continue;
            // }
        }
        check.push(p[i]);
    }

    // cout << check.size() << endl;

    if( check.size() == 0 ){
        return true;
    }
    else { return false; }
}

// 균형잡힌 문자열 리턴
vector<string> FindCollect(string p){
    int l_num=0;
    int r_num=0;
    string balance = "";
    string remain = "";
    vector<string> ret;
    
    for( int i=0; i<p.size(); i++){
        if( p[i] == '(' ){
            l_num++;
        }
        else if( p[i] == ')' ){
            r_num++;
        }

        if( l_num == r_num ){
            int i=0;
            for(i=0 ; i<l_num+r_num; i++){
                balance.push_back(p[i]);
            }
            for(; i<p.size(); i++){
                remain.push_back(p[i]);
            }
            break;
        }
    }

    ret.push_back(balance);
    ret.push_back(remain);

    // cout << balance << endl;
    // cout << remain << endl;

    return ret;
}

string recursive(string p){
    bool check;
    vector<string> split;
    string u, v;

    // 올바른 문자열인지 검사 stack 활용
    check = CollectCheck(p);
    if( check == true ){
        return p;
    }
    
    // 빈 문자열이면 반환
    if( p == "" ){
        return p;
    }

    // 균형잡힌 괄호문자열로 분리
    split = FindCollect(p);
    u = split[0];
    v = split[1];

    // cout << u << " " << v << endl;

    if( CollectCheck(u) ){ // u가 올바른 괄호문자열이라면
        u.append(recursive(v));
        return u;
    }
    else {
        string temp;
        temp.append("(");
        temp.append(recursive(v));
        temp.append(")");
        
        u.erase(u.begin());
        u.erase(u.end()-1);
        // cout << "temp " << temp << endl;
        // cout << "reverse u " << u << endl;
        for(int i=0; i<u.size(); i++){
            if( u[i] == '(' ){
                temp.push_back(')');
            }
            else{
                temp.push_back('(');
            }
        }
        return temp;
    }
}

string solution(string p) {
    string answer = "";
    
    answer = recursive(p);
    // cout << answer << endl;

    return answer;
}

int main(void){
    string ret;
    string p = "(()())()";
    ret = solution(p);
    cout << ret << endl;

    return 0;
}