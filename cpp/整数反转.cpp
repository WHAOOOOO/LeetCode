#include<cmath>
#include<string>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        if(x == 0){
            return 0;
        }
        else if(x > 0){
            string str_x = to_string(x);
            string rev_x = "";
            for(int i = 0; i < str_x.size(); i++){
                rev_x = str_x[i] + rev_x;
            }
            double int_rev_x = stod(rev_x);
            if(int_rev_x > (pow(2, 31) - 1))
                return 0;
            return int_rev_x;
        }
        else{
            string str_x = to_string(x);
            string rev_x = "";
            for(int i = 1; i < str_x.size(); i++){
                rev_x = str_x[i] + rev_x;
            }
            double int_rev_x = stod(rev_x);
            if(-int_rev_x < pow(-2, 31))
                return 0;
            return -int_rev_x;
        }
    }
};