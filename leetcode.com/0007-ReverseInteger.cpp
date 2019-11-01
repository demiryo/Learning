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

/*
Failing test case : Line 7: Char 15: runtime error: 
    negation of -2147483648 cannot be represented in type 'int'; 
    cast to an unsigned type to negate this value to itself (solution.cpp)
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
        long result = std::stol(str_val);
        if (std::numeric_limits<int32_t>::max() < result
            || std::numeric_limits<int32_t>::min() > result)
        {
            return 0;
        }
        return result;
    }
};
