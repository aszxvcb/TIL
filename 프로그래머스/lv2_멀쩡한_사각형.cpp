#include <stdio.h>

using namespace std;

long long gcd(long long a, long long  b);

long long solution(int w, int h) {
    // 문제의 매개변수 조건이 1억 이하의 자연수 임 -> 연산시 longlong으로 캐스팅
    long long answer = 1;
    long long gcd_num = 0;

    gcd_num = gcd(w,h);

    answer = (long long)w * (long long)h; // 전체 사각형 계산, 캐스팅
    answer -= (w+h-gcd(w,h)); // 지워질 사각형 계산
    return answer;
}

/* 최소공약수 구하는 함수 */
long long gcd(long long a, long long b){
    long long ret;
    long long div;

    if( a >= b ){
        ret = a%b;
        div = b;
    }
    else {
        ret = b%a;
        div = a;
    }

    if( ret == 0 ){
        return div;
    }
    else {
        return gcd(div, ret);
    }
}

int main(void){
    long long answer;

    answer = solution(3,5);

    printf("%lld\n", answer);



    return 0;
}