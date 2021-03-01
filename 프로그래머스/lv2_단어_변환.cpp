#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool visit[50];
int min_cnt;
int cnt;

void DFS(string& begin, string& target, vector<string>& words){
    int diff_cnt=0;

    if( begin == target ){
        // cout << "being == target!" << endl;
        if( min_cnt > cnt ){
            // cout << "cnt 갱신" << min_cnt << "->" << cnt << endl;
            min_cnt = cnt;
            return;
        }
    }
    
    for( int idx=0; idx<words.size(); idx++){
        if( visit[idx] == false ){
            diff_cnt = 0;
            
            // 문장 내 다른 글자 수 확인
            for( int i=0; i<words[idx].size(); i++ ){
                if( words[idx][i] != begin[i] ){
                    diff_cnt++;
                }
            }

            // 글자가 하나만 다르다면
            if( diff_cnt == 1 ){
                // cout << begin << "---" << words[idx] << "   " << target << endl;
                visit[idx] = true;
                cnt++;
                DFS( words[idx], target, words );
                cnt--;
                visit[idx] = false;
            }
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    min_cnt = 999;

    DFS(begin, target, words);

    answer = min_cnt;
    if(answer == 999){
        answer = 0;
    }
    return answer;
}


int main(void){

    min_cnt = 999;
    string begin = "hit";
    string target = "cog";
    int ret;

    vector<string> words = {"hot", "dot", "dog", "lot", "log", "cog"};

    ret = solution(begin, target, words);

    cout << ret << endl;

    return 0;
}