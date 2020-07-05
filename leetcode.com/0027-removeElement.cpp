class Solution {
    
    

    
public:
    int m_val;
    vector<int>::iterator  Current_pos;
  
    
    int removeElement(vector<int>& nums, int val) {
        vector<int> nums2 = nums;
        
        
        m_val = val;
        int length = 0; 
        
       

        
        Current_pos = nums.begin();
     
        
        while(Current_pos < nums.end())
        {
        
            if(*Current_pos == val)
            {
                
                nums.erase(Current_pos);
                Current_pos--;
                
            }
            
            else
            {
                length++;
               

            }
            Current_pos++;
        }
        
        return length;
        
        

        
    }
};