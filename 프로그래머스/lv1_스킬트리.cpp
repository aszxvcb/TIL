#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

/*
    python 풀이 참고
*/

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;

    for( string skill_tree : skill_trees ){
        queue<char> q;
        bool check = true;
        for(int i=0; i<skill.size(); i++ ){
            q.push(skill[i]);
        }

        for(int i=0; i<skill_tree.size(); i++ ){
            if( find(skill.begin(), skill.end(), skill_tree[i]) != skill.end() ){
                if( skill_tree[i] != q.front() ){
                    check = false;
                    break;
                }
                else {
                    q.pop();
                }
            }
        }

        if( check == true ){
            answer ++;
        }
        
    }

    return answer;
}

int main(void){

    string skill = "CBD";
    vector<string> skill_trees = {"BACDE", "CBADF", "AECB", "BDA"};
    int ret;

    ret = solution(skill, skill_trees);
    cout << ret << endl;


    return 0;
}