#include <vector>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums){
            vector<int> ans;

            vector<int> prefixArray;
            int runningProduct = 1;
            for (int num: nums){
                runningProduct *= num;
                prefixArray.push_back(runningProduct);
            }

            vector<int> suffixArray;
            runningProduct = 1;
            for (int num: nums){
                runningProduct *= num;
                suffixArray.push_back(runningProduct);
            }

            for (int i = 0; i < nums.size(); i++){
                int suffixProduct;
                int prefixProduct;
                if (i - 1 < 0){
                    prefixProduct = 1; 
                } else if (i + 1 == nums.size()){
                    suffixProduct = 1; 
                } else {
                    prefixProduct = prefixArray[i];
                    suffixProduct = suffixArray[i]; 
                }
                ans.push_back(prefixProduct * suffixProduct);
            }

            return ans;
        }
};

int main() {
    cout << "Input: " << endl;
    
    string strInput; 
    
    vector<int> input;
    for (string line; std::getline(cin, strInput, ',');){
        input.push_back(stoi(line));  
    }
    
    for (int i: input) cout << i;
    cout << endl;

}

