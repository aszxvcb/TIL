#include <iostream>
#include <vector>

using namespace std;

/*
    구현 문제
    
    자료형이 int의 범위를 벗어남. long long 사용
    ( 자료형을 수정한다고 수정해놓고 정작, solution()의 반환값을 수정안해서 삽질한 문제 )

    근데 풀이를 보니 쉽고 간단하게 해결이되더라
    answer = min( season/5, (season + coupon) / 12);
    으로 답을 구할 수 있음.
*/

long long solution(long long season, long long coupon){
    long long answer = 0;

    long long num, num2;

    answer = min( season/5, (season + coupon) / 12);
    return answer;

    // while(1){
    //     if(season >= 5){
    //         if(coupon >= 7){
    //             // 시즌+일반이 충분할 때
    //             num = season / 5;
    //             num2= coupon / 7;
    //             num = min(num, num2);

    //             coupon -= 7 * num;
    //             season -= 5 * num;
    //             answer += num;
    //         }
    //         if {
    //             if( season >= 11 * coupon && coupon < 7 && coupon > 0 ){
    //                 // 시즌이 많고, 일반이 적을 때
    //                 season -= 11 * coupon;
    //                 answer += coupon;
    //                 coupon = 0;
    //             }
    //             if( season + coupon >= 12) {
    //                 // 시즌도 적고, 일반도 적을 때
    //                 season -= (12 - coupon);
    //                 coupon = 0;
    //                 answer++;
    //             }
    //             if( season >= 12 ){
    //                 // 일반이 없을 때
    //                 num = season / 12;
    //                 season -= 12 * num;
    //                 answer += num;
    //             }
    //             else{
    //                 return answer;
    //             }
    //         }
    //     }
    //     else { return answer; };
    // }

}

int main(void){

    ios_base::sync_with_stdio(false);	
    cin.tie(NULL);
    cout.tie(NULL);

    int num;
    vector<long long> season;
    vector<long long> coupon;
    long long ret;
    long long input;

    cin >> num;

    for(int i=0; i<num; i++){
        cin >> input;
        season.push_back(input);
        cin >> input;
        coupon.push_back(input);
    }

    for(int i=0; i<num; i++){
        ret = solution(season[i], coupon[i]);
        cout << ret << endl;
    }

    return 0;
}

