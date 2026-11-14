#!/bin/bash
# sed -E '/#B Seq/d' |\
#     sed -E  '/#E Seq/d' |\
#     sed -E  '/#B Pred/d' |\
#     sed -E  '/#E Pred/d' |\
#     sed -E  '/#B Br/d' |\
#     sed -E  '/#E Br/d'

sed -E '/#B /d' | sed -E '/#E /d'
