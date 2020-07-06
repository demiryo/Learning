class Solution {
    
    

    
public:
    int m_val;
    vector<int>::iterator  Current_pos;
  
    
    int removeElement(vector<int>& nums, int val) {
       
        auto m_end = nums.end();
         
        for( auto m_start = nums.begin(); m_start != m_end; m_start++)
        {
            if(*m_start == val)
            {
                m_start = nums.erase(m_start) - 1;
                
                m_end = nums.end();
            }
        }
        return nums.size();

        
    }
};