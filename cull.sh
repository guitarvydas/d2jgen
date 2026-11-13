#!/bin/bash
sed -E '/# begin Seq/d' |\
    sed -E  '/# end Seq/d' |\
    sed -E  '/# begin Pred/d' |\
    sed -E  '/# end Pred/d' |\
    sed -E  '/# begin Br/d' |\
    sed -E  '/# end Br/d'
    
