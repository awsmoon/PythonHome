#Module Search ordering
# 1. 동일한 디렉토리
# 2. sys.path 에서 찾음
# 3. 

import sys
for path in sys.path :
    print(path)