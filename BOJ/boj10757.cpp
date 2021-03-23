#include <iostream>
#include <string>
#include <stack>

using namespace std;

/*
    문자열로 받아들인 후, 맨 끝자리부터 한자리씩 연산해준다.
    만약 10을 넘기면, 올림을 해준다.
    자릿수가 다른 경우, 한자리가 끝나면 나머지 하나만 계속 더해준다.
    스택에 넣고 역순으로 출력한다.
*/

int main(void){
    stack<int> s;
    string a, b;
    bool upper = false;

    // cout << 1;
    // for(int i=0; i<9999; i++){
    //     cout << 0;
    // }

    cin >> a >> b;

    int i=a.size()-1;
    int j=b.size()-1;
    while(1){
        int ia, ib, num;

        // 자릿수가 달라, 어느한쪽이 먼저 자릿수 탐색이 끝났다면
        if( i < 0 && j >= 0){
            num = b[j] - '0';
            if (upper == true ){
                num++;
                if(num >= 10){
                    num -= 10;
                    upper = true;
                }
                else{
                    upper = false;
                }
            }
            j--;
            s.push(num);
            continue;
        }
        else if( j < 0 && i >= 0){
            num = a[i] - '0';
            if (upper == true ){
                num++;
                if(num >= 10){
                    num -= 10;
                    upper = true;
                }
                else{
                    upper = false;
                }
            }
            i--;
            s.push(num);
            continue;
        }
        else if( i < 0 && j < 0 ){
            if( upper == true ){
                s.push(1);
            }
            break;
        }

        ia = a[i] - '0';
        ib = b[j] - '0';
        num = ia + ib;
        if( upper == true ){
            num += 1;
        }

        if( num >= 10 ){
            num -= 10;
            upper = true;
        }
        else {
            upper = false;
        }

        s.push(num);
        i--;
        j--;
    }

    for(int i=0, size=s.size(); i<size; i++){
        cout << s.top();
        s.pop();
    }

    return 0;   
}