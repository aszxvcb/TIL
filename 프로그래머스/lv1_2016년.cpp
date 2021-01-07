#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    string answer = "";
    string day[7] = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
    int dd = 5;

    if( a != 1 ){
        for(int i=1; i<a; i++){
            if( i == 2 ){
            dd += 29;
            }
            else if( i==1 || i==3 || i==5 || i==7 || i==8 || i==10 || i==12 ){
                dd += 31;
            }
            else {
                dd += 30;
            }
        }
    }
    dd += b-1;
    dd %= 7;
    answer = day[dd];

    return answer;
}

int main(void){
    int a = 2;
    int b = 29;
    string ret = "";

    ret = solution(a,b);

    printf("%s", ret.c_str());
}