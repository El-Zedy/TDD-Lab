# TDD-Lab
## unit testing lab using 'unittest' in python 

### Create Tests using unittest framework
- test one act as ex1.py
- test two act as ex2.py

#### Using the test techniques => write test cases to test the following function with respect to following rules :
- Mentioned used techniques 
- Create 2 Test suites 
- In each test suite create at least 2 test cases
- Use the following methods 
-- afterAll
-- beforeAll
#### Ex #1 :Test function to evaluate Car speed
--------------------------------------------
  Req # 1 : Input to the function is the car speed and output shall be speed level
  Req# 2 : Function shall calculate output to be:
  
      - If          Speed < 0    Level shall be Invalid 
      - If     0 <= Speed < 40  Level shall be Low
      - If    40 <= Speed < 120 Level shall be Normal
      - If   120 <= Speed < 200 Level shall be High
      - If   200 <= Speed < 220 Level shall be V.High 
      - If   220 <  Speed       Level shall be Invalid

#### Ex #2 :Test function to evaluate students Scores
--------------------------------------------------
  Req # 1 : Input to the function is student Scores and output student Level
  Req# 2 : Function shall calculate output to be:
  
      - If         Score < 0    Level shall be Invalid 
      - If    0 <= Score < 50   Level shall be Failed 
      - If   50 <= Score < 65   Level shall be Passed
      - If   65 <= Score < 75   Level shall be Good
      - If   75 <= Score < 85   Level shall be V.Good
      - If   85 <= Score < 100  Level shall be Excellent 
      - If  100 <  Score        Level shall be In
