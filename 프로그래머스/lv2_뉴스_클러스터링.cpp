#include <string>
#include <iostream>
#include <vector>
#include <cctype>
#include <algorithm>
#include <unordered_map>
#include <set>

using namespace std;

int solution(string str1, string str2) {
    int answer = 0;
    vector<string> v1, v2;
    unordered_map<string, int> m1, m2;
    set<string> s1, s2;
    
    
    // 두개씩 분리 후 조건에 맞는 지 확인
    for(int i=0; i<str1.size()-1; i++){
        if( isalpha(str1[i]) && isalpha(str1[i+1]) ){
            string substring = str1.substr(i,2);
            transform(substring.begin(), substring.end(), substring.begin(), ::toupper );
            // v1.push_back( substring );
            if( m1.find(substring) == m1.end() ){
                m1.insert(make_pair(substring, 1));
            }            
            else{
                m1.find(substring)->second++;
            }
        
            s1.insert(substring);
        }
    }

    for(int i=0; i<str2.size()-1; i++){
        if( isalpha(str2[i]) && isalpha(str2[i+1]) ){
            string substring = str2.substr(i,2);
            transform(substring.begin(), substring.end(), substring.begin(), ::toupper );
            // v2.push_back( substring );
            if( m2.find(substring) == m2.end() ){
                m2.insert(make_pair(substring, 1));
            }            
            else{
                m2.find(substring)->second++;
            }
            s2.insert(substring);
        }
    }

    vector<string> intersection_s;
    vector<string> union_s;

    // 반복자 어댑터 (inserter) 사용
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(intersection_s, intersection_s.begin()));
    set_union(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(union_s, union_s.begin()));

    float union_num=0, intersection_num=0, result=0;
    for(int i=0; i<intersection_s.size(); i++){
        int num1=0, num2=0;
        if( m1.find(intersection_s[i]) != m1.end() ){
            num1 = m1.find(intersection_s[i])->second;
        }
        if( m2.find(intersection_s[i]) != m2.end() ){
            num2 = m2.find(intersection_s[i])->second;
        }

        intersection_num += min(num1, num2);
    }

    for(int i=0; i<union_s.size(); i++){
        // 합집합이기 때문에 find에서 없는 값이 나올 수 있음
        // union_num += max(m1.find(union_s[i])->second, m2.find(union_s[i])->second);

        int num1=0, num2=0;
        if( m1.find(union_s[i]) != m1.end() ){
            num1 = m1.find(union_s[i])->second;
        }
        if( m2.find(union_s[i]) != m2.end() ){
            num2 = m2.find(union_s[i])->second;
        }

        union_num += max(num1, num2);
    }

    if( union_num != 0 || intersection_num != 0){
        result = intersection_num/union_num;
    }
    else {
        result = 1;
    }
    answer = result * 65536;

    return answer;
}

int main(void){
    string str1 = "FRANCE";
    string str2 = "french";
    int ret;

    ret = solution(str1, str2);
    cout << ret << endl;

    return 0;
}