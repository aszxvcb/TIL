#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";

    map<string, int> left_hand = {{"x",1},{"y",4}};
    map<string, int> right_hand = {{"x",3},{"y",4}};

    vector<int> left = {1,4,7};
    vector<int> center = {2,5,8,0};
    vector<int> right = {3,6,9};

    int idx;
    int left_distance, right_distance;
    for( int i=0; i<numbers.size(); i++){

        // cout << "hand " << left_hand.find("x")->second << " " << left_hand.find("y")->second << endl;
        // cout << "hand " << right_hand.find("x")->second << " " << right_hand.find("y")->second << endl;

        // 왼쪽 버튼일때
        if( (idx = find(left.begin() , left.end(), numbers[i]) - left.begin()) != left.size() ){
            // cout << "L" << idx+1 << endl;
            left_hand.find("y")->second = idx+1;
            left_hand.find("x")->second = 1;
            answer.append("L");
        }
        // 오른쪽 버튼일때
        else if ( (idx = find(right.begin() , right.end(), numbers[i]) - right.begin()) != right.size() ){
            // cout << "R" << idx+1 << endl;
            right_hand.find("y")->second = idx+1;
            right_hand.find("x")->second = 1;
            answer.append("R");
        }
        // 가운데 버튼일때
        else{
            idx = find(center.begin(), center.end(), numbers[i]) - center.begin() +1;
            right_distance = abs(right_hand.find("y")->second - idx) + abs(right_hand.find("x")->second - 2);
            left_distance = abs(left_hand.find("y")->second - idx) + abs(left_hand.find("x")->second - 2);
            // cout << left_distance << " " << right_distance << endl;
            if( right_distance == left_distance ){
                if( hand == "right"){
                    answer.append("R");
                }
                else{
                    answer.append("L");
                }
            }
            else if ( right_distance < left_distance){
                answer.append("R");
            }
            else {
                answer.append("L");
            }

            if( answer.back() == 'L' ){
                left_hand.find("y")->second = idx;
                left_hand.find("x")->second = 2;
            }
            else {
                right_hand.find("y")->second = idx;
                right_hand.find("x")->second = 2;
            }
        }
    }

    return answer;
}

int main(void){

    vector<int> numbers = {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2};
    string hand = "left";
    string ret;
    
    ret = solution(numbers, hand);

    cout << ret;

    return 0;
}