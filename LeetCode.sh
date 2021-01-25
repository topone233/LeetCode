#!/bin/sh

set -eux

LANGUAGE="zh-CN"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

curl \
  -H "Accept-Language: $LANGUAGE" \
  -H "User-Agent: $UA" \
  -h "Content-Type: application/json"
  -X POST
  -d "{
    "operationName": "questionOfToday",
    "variables": {},
    "query": "query questionOfToday { todayRecord {   question {     questionFrontendId     questionTitleSlug     __typename   }   lastSubmission {     id     __typename   }   date   userStatus   __typename }}"
}"
  -o result.html \
  https://leetcode-cn.com/graphql
