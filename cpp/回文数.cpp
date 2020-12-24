class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0)
            return false;
        else{
            string str_x = to_string(x);
            int len = str_x.size();
            for(int i = 0; i<len; i++){
                if(str_x[i] != str_x[len-1-i]){
                    return false;
                }
            }
            return true;
        }
    }
};