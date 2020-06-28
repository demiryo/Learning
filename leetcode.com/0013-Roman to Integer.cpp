class Solution {
    private:
        const string *m_s;
        // I rather use const_forward iterator
        string::const_iterator m_pos; // store current position
        string::const_iterator m_end_pos; // store end position
        int m_val;

    // Increment the current position by inc
        void inc_value(int inc)
        {
            m_val+= inc;
        }
    
        bool inc_pos(size_t inc)
        {

         if(m_end_pos - m_pos  < inc)
            {
                return false;
            }
           m_pos += inc;    
            return true;

         }

    bool Is_III(){

        if( m_end_pos - m_pos < 3)
        {
            return false;
        }

        if( *m_pos == 'I' && *(m_pos+1) == 'I' && *(m_pos+2) == 'I' )
        {
            inc_pos(3);
            inc_value(3);
            return true;
        }
        
        return false;
    }

    bool Is_II(){

        if( m_end_pos - m_pos  < 2)
        {
            return false;
        }


         if(*m_pos == 'I' && *(m_pos+1) == 'I')
        {
            inc_pos(2);
            inc_value(2);
             return true;
        }
        return false;
    }
    bool Is_I(){

        if( m_end_pos - m_pos  < 1)
        {
            return false;
        }


         if(*m_pos == 'I')
        {
            inc_pos(1);
            inc_value(1);
             return true;
        }
        return false;
    }
    
    bool Is_V(){

        if( m_end_pos - m_pos  < 1)
        {
            return false;
        }


         if(*m_pos == 'V')
        {
            inc_pos(1);
            inc_value(5);
             return true;
        }
        return false;
    }
    
    

    bool Is_IV(){

        if(m_end_pos - m_pos < 2)
        {
            return false;
        }

      

         if(*m_pos == 'I' &&  *(m_pos+1) == 'V')
        {
            inc_pos(2);
            inc_value(4);
             return true;
        }
        return false;
    }
    bool Is_IX(){

        if(m_end_pos - m_pos < 2)
        {
            return false;
        }

      

         if(*m_pos == 'I' &&  *(m_pos+1) == 'X')
        {
            inc_pos(2);
            inc_value(9);
             return true;
        }
        return false;
    }
    
    bool Is_X(){

        if( m_end_pos - m_pos  < 1)
        {
            return false;
        }


         if(*m_pos == 'X')
        {
            inc_pos(1);
            inc_value(10);
             return true;
        }
        return false;
    }
    
    bool Is_XL(){

        if(m_end_pos - m_pos < 2)
        {
            return false;
        }


         if(*m_pos == 'X' &&  *(m_pos+1) == 'L')
        {
            inc_pos(2);
            inc_value(40);
             return true;
             
        }
        return false;
    }
    
     bool Is_XC(){

        if(m_end_pos - m_pos < 2)
        {
            return false;
        }


         if(*m_pos == 'X' &&  *(m_pos+1) == 'C')
        {
            inc_pos(2);
            inc_value(90);
             return true;
             
        }
        return false;
    }
    
     bool Is_L(){

        if( m_end_pos - m_pos  < 1)
        {
            return false;
        }


         if(*m_pos == 'L')
        {
            inc_pos(1);
            inc_value(50);
             return true;
        }
        return false;
    }
    
     bool Is_C(){

        if( m_end_pos - m_pos  < 1)
        {
            return false;
        }


         if(*m_pos == 'C')
        {
            inc_pos(1);
            inc_value(100);
             return true;
        }
        return false;
    }
     bool Is_CD(){

        if(m_end_pos - m_pos < 2)
        {
            return false;
        }


         if(*m_pos == 'C' &&  *(m_pos+1) == 'D')
        {
            inc_pos(2);
            inc_value(400);
             return true;
             
        }
        return false;
    }
     bool Is_CM(){

        if(m_end_pos - m_pos < 2)
        {
            return false;
        }


         if(*m_pos == 'C' &&  *(m_pos+1) == 'M')
        {
            inc_pos(2);
            inc_value(900);
             return true;
             
        }
        return false;
    }
    
     bool Is_D(){

        if( m_end_pos - m_pos  < 1)
        {
            return false;
        }


         if(*m_pos == 'D')
        {
            inc_pos(1);
            inc_value(500);
             return true;
        }
        return false;
    }
    
     bool Is_M(){

        if( m_end_pos - m_pos  < 1)
        {
            return false;
        }


         if(*m_pos == 'M')
        {
            inc_pos(1);
            inc_value(1000);
             return true;
        }
        return false;
    }
    
    void initialize(const string& s)
    {
            m_s = &s;
            m_pos = m_s->cbegin();
            m_end_pos = m_s->cend();
            m_val = 0;        
    }

    public:
        int romanToInt(string s) {

            initialize(s);
            
            while(m_pos != m_end_pos)
           {
                                // cout << "{ pos=" << (m_end_pos-m_pos) << "/ size=" << m_s.size() << ";*pos=" << *m_pos << " }\n";


                if(Is_CM())
                {

                }
                if(Is_CD())
                {

                }

                if(Is_XL())
                {

                }
                if(Is_XC())
                {

                }


                if(Is_V())
                {

                }
                
                if(Is_IX())
                {

                }

                if(Is_X())
                {

                }

                if(Is_L())
                {

                }

                if(Is_C())
                {

                }



                if(Is_D())
                {

                }

                if(Is_M())
                {

                }
                
                if(Is_IX() )
                {
// i want a way to make this block faster    //
                }                           //                
                else if(Is_IV() )          //
                {                         /////
                                            //
                }                          //
                else if(Is_III())         //
                {                        //

                }
                else if(Is_II())
                {

                }
                else if(Is_I())
                {

                }
                
                
                            
               // inc_pos(1);
            
           }

            return m_val;
            }

        };  
