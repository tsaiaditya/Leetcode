/*
Q - You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
*/
#include<iostream>
#include<vector>
#include<algorithm>
#include <string> 
#include <unordered_set> 
using namespace std;
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        vector<string> q{"0000"};
        unordered_set<string> lookup{"0000"};
        int depth = 0;
        while(!q.empty()){
            vector<string> next_q;
            for(const auto& node:q){
                if(node == target)
                    return depth;
                if(dead.count(node))
                    continue;
                for(int i = 0; i<4; i++){
                    auto n = node[i] - '0';
                    for(const auto& d:{-1,1}){
                        auto nn = (n+d+10)%10;
                        auto neighbour = node;
                        neighbour[i] = '0' + nn;
                        if(!lookup.count(neighbour)){
                            lookup.emplace(neighbour);
                            next_q.emplace_back(neighbour);
                        }
                    }
                }
            }
            swap(q,next_q);
            ++depth;
        }
        return -1;
    }
};

int main(int argc, char const *argv[])
{
    int n;
    cout<<"Enter the number of deadends: ";
    cin>>n;
    vector<string> dead(n);
    string temp;
    cout<<"Enter the deadends: ";
    for(int i = 0; i<n; i++){
        cin>>temp;
        dead.push_back(temp);
    }
    Solution s;
    string target;
    cout<<"Enter the target: ";
    cin>>target;
    int res = s.openLock(dead,target);
    if(res != -1)
        cout<<"Number of moves to reach to target from 0000 is: "<<res;
    else
        cout<<"We can't reach the target without getting stuck.";
    return 0;
}
