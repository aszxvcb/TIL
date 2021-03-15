#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

/*
    info, query 스플릿하고
    info는 정렬하여 같은 언어들끼리 뭉쳐있도록 함
    query를 통해 info에서 찾을 때
    해당 언어가 모여있는 시작지점과 끝지점만 인덱싱하여 찾도록 함 (효율성을 위해)

    결과 : 효율성(시간초과)


    (수정) DB처럼 구축하고 이분탐색을 이용하여 범위에 해당하는 갯수 계산

    TIP : split 구현부 (current, previous 활용) , lower_bound()
*/

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    vector<int> db[3][2][2][2];
    vector<vector<int>> query_split;

    // info 의 각 인덱스에 split 적용
    int current = 0;
    int previous = 0;
    vector<int> p;
    for(string line : info ){
        p.clear();
        current = 0;
        previous = 0;
        current = line.find(" ");
        while(current != string::npos){
            string substring = line.substr(previous, current-previous);
            if( substring == "cpp" || substring == "backend" || substring == "junior" || substring == "chicken"){
                p.push_back(0);
            }
            else if( substring == "python"){
                p.push_back(2);
            }
            else {
                p.push_back(1);
            }
            previous = current + 1;
            current = line.find(" ", previous);
        }
        // cout << line.substr(previous, current) << endl;
        db[p[0]][p[1]][p[2]][p[3]].push_back(stoi(line.substr(previous, current)));
    }

    // 점수에 따라 정렬
    for(int i=0; i<3; i++){
        for(int j=0; j<2; j++){
            for(int k=0; k<2; k++){
                for(int l=0; l<2; l++){
                    for(auto elem : db[i][j][k][l] ){
                        sort(db[i][j][k][l].begin(), db[i][j][k][l].end());
                        // cout << i << " " << j << " " << k << " " << l <<  " " << elem << endl;
                    }
                }
            }
        }
    }

    // query 의 각 인덱스에 split 적용
    for(string line : query ){
        p.clear();
        current = 0;
        previous = 0;
        current = line.find(" and ");
        string substring;
        while( current != string::npos ){
            substring = line.substr(previous, current-previous);
            if( substring == "cpp" || substring == "backend" || substring == "junior" || substring == "chicken"){
                p.push_back(0);
            }
            else if( substring == "python"){
                p.push_back(2);
            }
            else if( substring == "-"){
                p.push_back(-1);
            }
            else {
                p.push_back(1);
            }
            previous = current + 5;
            current = line.find(" and ",previous);
        }
        current = line.find(" ", previous);
        substring = line.substr(previous, current-previous);
        if( substring == "chicken" ){
            p.push_back(0);
        }
        else if( substring == "pizza"){
            p.push_back(1);
        }
        else{
            p.push_back(-1);
        }
        previous = current + 1;
        substring = line.substr(previous, line.size()-previous);
        p.push_back(stoi(substring));

        query_split.push_back(p);
    }

    for(vector<int> query: query_split){
        int start_i, start_j, start_k, start_l;
        int end_i, end_j, end_k, end_l;
        
        if(query[0] == -1){ start_i = 0; end_i = 2; }
        else if(query[0] == 0){ start_i = end_i = 0; }
        else if(query[0] == 1){ start_i= end_i = 1; }
        else{ start_i = end_i = 2; }

        if(query[1] == -1){ start_j = 0; end_j = 1;}
        else if(query[1] == 0){ start_j = end_j = 0;}
        else{ start_j = end_j = 1;}

        if(query[2] == -1){ start_k = 0; end_k = 1;}
        else if( query[2] == 0){ start_k = end_k = 0;}
        else{ start_k = end_k = 1;}

        if(query[3] == -1){ start_l = 0; end_l = 1;}
        else if( query[3] == 0){ start_l = end_l = 0;}
        else { start_l = end_l = 1;}

        int n = 0;
        int score = query[4];

        for( int i=start_i; i<=end_i; i++){
            for( int j=start_j; j<=end_j; j++){
                for( int k=start_k; k<=end_k; k++){
                    for( int l=start_l; l<=end_l; l++){      
                        int size = db[i][j][k][l].size();
                        if( size == 0){ continue; }

                        int lower_idx = lower_bound(db[i][j][k][l].begin(), db[i][j][k][l].end(), score) - db[i][j][k][l].begin();

                        // for( auto elem : db[i][j][k][l]){
                        //     cout << elem << " ";
                        // }
                        // cout << lower_idx << " " << score << " " << endl;

                        n += size - lower_idx;
                    }
                }
            }
        }
        answer.push_back(n);
    }

    return answer;
}

// vector<int> solution(vector<string> info, vector<string> query) {
//     vector<int> answer;
//     vector<vector<string>> info_split;
//     vector<vector<string>> query_split;
//     vector<string> people;
//     unordered_map<string, pair<int ,int >> hashtable;

//     // info 의 각 인덱스에 split 기능 적용 
//     // 5개 컬럼의 배열에 저장
//     int current = 0;
//     int previous = 0;
//     for(string line : info){
//         people.clear();
//         current = 0;
//         previous = 0;
//         current = line.find(' ');
//         while(current != string::npos){
//             string substring = line.substr(previous, current - previous);
//             people.push_back(substring);
//             previous = current + 1;
//             current = line.find(' ', previous);
//         }
//         people.push_back(line.substr(previous, current-previous));
//         info_split.push_back(people);

//         // for(auto elem : people ){
//         //     cout << elem << " ";
//         // }
//         // cout << endl;
//     }
//     sort(info_split.begin(), info_split.end());
//     // for(auto line : info_split ){
//     //     for(auto elem : line ){
//     //         cout << elem << " ";
//     //     }
//     //     cout << endl;
//     // }
//     // cout << endl;

//     for(int i=0; i<info_split.size(); i++){
//         if( hashtable.find(info_split[i][0]) == hashtable.end() ){
//             hashtable.insert(make_pair(info_split[i][0], make_pair(i,i)));
//         }
//         else{
//             hashtable.find(info_split[i][0])->second.second++;
//         }
//     }

//     // for(auto iter = hashtable.begin(); iter != hashtable.end(); iter++){
//     //     cout << iter->first << " " << iter->second.first << " " << iter->second.second;
//     // }
//     // cout << endl;

//     // cout << "complete" << endl;

//     // query split
//     for(string line : query){
//         people.clear();
//         current = 0;
//         previous = 0;
//         current = line.find(" and ");
//         while( current != string::npos ){
//             string substring = line.substr(previous, current - previous);
//             people.push_back(substring);
//             previous = current + 5;
//             current = line.find(" and ", previous);
//         }
//         current = line.find(' ', previous);
//         people.push_back(line.substr(previous, current - previous));
//         previous = current + 1;
//         people.push_back(line.substr(previous, line.size()));
//         query_split.push_back(people);

//         // for(auto elem : people ){
//         //     cout << elem << " ";
//         // }
//         // cout << endl;
//     }

//     int start_idx;
//     int end_idx;
//     int cnt;
//     for( int i=0; i<query_split.size(); i++ ){
//         cnt = 0;

//         if( hashtable.find(query_split[i][0]) != hashtable.end() ){
//             start_idx = hashtable.find(query_split[i][0])->second.first;
//             end_idx = hashtable.find(query_split[i][0])->second.second + 1;
//         }
//         else{
//             start_idx = 0;
//             end_idx = info_split.size();
//         }
        
//         for( int j=start_idx; j<end_idx; j++){
//             if ( info_split[j][0] == query_split[i][0] || query_split[i][0] == "-"){
//                 for( int k=0; k<info_split[j].size(); k++){
//                     if( k == info_split[j].size()-1 ){
//                         if(stoi(info_split[j][k]) >= stoi(query_split[i][k]) ){
//                             cnt++;        
//                             break;
//                         }
//                     }
//                     // cout << info_split[j][k] << " " << query_split[i][k] << endl;
//                     if( info_split[j][k] != query_split[i][k] && query_split[i][k] != "-"){
//                         break;
//                     }
//                 }
//             }
//         }
//         answer.push_back(cnt);
//     }

//     return answer;
// }

int main(void){
    vector<int> ret;
    vector<string> info = {"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
    vector<string> query = {"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};
    // vector<string> query = {"go and backend and - and - 0"};

    ret = solution(info, query);

    for(auto elem : ret ){
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}