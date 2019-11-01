/*

https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

*/

class Solution {
public:
    int reverse(int x) {
        bool is_negative = x < 0;
        if (is_negative)
        {
            x = -x;
        }
        std::string str_val = std::to_string(x);
        std::reverse(str_val.begin(), str_val.end());
        
        if (is_negative)
        {
            str_val = "-" + str_val;
        }
        return std::stoi(str_val);
    }
};
