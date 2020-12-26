#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

// using namespace std;

int main(void){
    int input=0;
    long long num=0;
    std::string str = "";
    char buf[256] = {0,};
    int len=0, cnt=0;

    scanf("%d", &input);
    
    for(int i=0; i<input; i++){
        while(1){
            str.clear(); // str을 초기화
            cnt = 0;
            
            num++;
            len = sprintf(buf,"%lld\n",num); // sprintf의 리턴은 buf에 쓰여진 문자열의 길이
            str.append(buf);

            if( str.find("666") != std::string::npos){
                /* string::npos (no position)으로 find값을 찾지 못할때의 리턴 값 */
                // printf("%s", str.c_str()); // str을 char* 으로 변환
                break;
            }
        }
    }

    printf("%lld\n", num);

    return 0;
}