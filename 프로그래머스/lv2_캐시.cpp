#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

/*
    해시테이블을 사용하여 각 도시들을 캐싱한다.
    캐싱할 때, 들어온 시간 정보를 넣어 최근에 들어온 것을 확인할 수 있도록 한다.

    캐시힛인 경우, 시간 정보를 업데이트 한다.
    캐시미스인 경우, 가장 오래전에 업데이트된 데이터를 지우고, 새로운 데이터를 캐시한다.
*/

void PrintCache(unordered_map<string,int> &cache){
    // cout << endl;
    // for(auto iter = cache.begin() ; iter != cache.end(); iter ++ ){
    //     cout << iter->first << " " << iter->second << endl;
    // }
    // cout << endl;
}

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    unordered_map<string, int> cache;
    int time = 0;

    for(int i=0; i<cities.size(); i++){

        transform(cities[i].begin(), cities[i].end(), cities[i].begin(), ::toupper);

        if( cacheSize == 0){
            time += 5;
        }
        else if(cache.size() != 0 && cache.find(cities[i]) != cache.end()){
            time += 1;
            cache.find(cities[i])->second = time;
        }
        else if(cache.size() < cacheSize ){
            time += 5;
            cache.insert(make_pair(cities[i], time));

            PrintCache(cache);
        }
        else if(cache.size() == cacheSize && cache.find(cities[i]) == cache.end()){
            time += 5;

            int min = 999999;
            unordered_map<string,int>::iterator min_iter;
            for(auto iter=cache.begin(); iter != cache.end(); iter++){
                if( min >= iter->second ){
                    min = iter->second;
                    min_iter = iter;
                }
            }
            
            PrintCache(cache);
            cache.erase(min_iter);
            cache.insert(make_pair(cities[i], time));
            PrintCache(cache);
        }
    }
    
    answer = time;
    return answer;
}

int main(void){
    int cacheSize = 3;
    vector<string> cities = {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"};
    int ret;

    ret = solution( cacheSize, cities );
    cout << ret << endl;

    return 0;
}