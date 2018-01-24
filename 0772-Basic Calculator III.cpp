#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <deque>
#include <map>
#include <cstdlib>
#include <cstdio>

using namespace std;

class Solution {
  public:
      vector<string> analyzeExpression(string expression){
        vector<string> ret;
        string s = "@";
        for(auto i = 0,begin = 0;i < expression.size();i++){
            s[0] = expression[i];
            if(expression[i] == ' '){
              if(begin != i){
                string val = expression.substr(begin,i - begin);
                ret.push_back(val);
              }
              begin = i + 1;
            }else if(expression[i] == '(' || expression[i] == ')' ||  expression[i] == '+' ||  expression[i] == '-' ||  expression[i] == '*' ||  expression[i] == '/'){
              if(begin != i){
                string val = expression.substr(begin,i - begin);
                ret.push_back(val);
              }
              ret.push_back(s);
              begin = i + 1;
            }else if(i == expression.size() - 1){
                string val = expression.substr(begin);
                ret.push_back(val);
            }
        }
        return ret;
      }

      int calculate(string s) {
        vector<string> elements = analyzeExpression(s);
        stack<string> s1,s2;
        s1.push("#");
        for(auto it = elements.begin();it != elements.end();it++){
          if(*it == "("){
            s1.push(*it);
          }else if(*it == ")"){
            while(s1.top() != "("){
              s2.push(s1.top());
              s1.pop();
            }
            s1.pop();
          }else if(*it == "*" || *it == "/"){
            while(s1.top() == "*" || s1.top() == "/"){
              s2.push(s1.top());
              s1.pop();
            }
            s1.push(*it);
          }else if(*it == "+" || *it == "-"){
            while(s1.top() != "(" && s1.top() != "#"){
              s2.push(s1.top());
              s1.pop();
            }
            s1.push(*it);
          }else{
            s2.push(*it);
          }
        }
        while(s1.top() != "#"){
          s2.push(s1.top());
          s1.pop();
        }
        stack<string> ss;
        while(!s2.empty()){
          ss.push(s2.top());
          s2.pop();
        }
        stack<long long> value;
        while(!ss.empty()){
          if(ss.top() == "+" || ss.top() == "-" || ss.top() == "*" || ss.top() == "/"){
            long long a = value.top();
            value.pop();
            long long b = value.top();
            value.pop();
            if(ss.top() == "+"){
              value.push(b + a);
            }else if(ss.top() == "-"){
              value.push(b - a);
            }else if(ss.top() == "*"){
              value.push(b * a);
            }else{
              value.push(b / a);
            }
          }else{
            value.push(stoll(ss.top()));
          }
          ss.pop();
        }
        return value.top();
      }
};

int main(int argc, char const *argv[]) {
  /* code */
  string s = "((   ( (   (34   /   (( (  (   67*(43+ 64 )  ) + ((  35 /  52  )-   (1-   15   )   )   )  -   63)*  ( ( 56   +  (  47 /86   )   )+  (   24  /   (   (93   -   20  )  * (   49 +   78   )   )  )  ) ) )   +   ( (  (16+(((90   +96) - (95- 19) )  -   ( (   77   * 33 )+ (   98 +   81 )  )   ) )  +19 ) *   (  ( (   (   (  23 +   54  )*( 64 -   97 )   )  *   (   (64+ 34   )*  (37  *  85   )  )  ) - ( ( (33   +  18   ) *60   )   +  24   )   )*( (  (  (60  *   38   )+( 27 / 32)  ) +   (   (  30  - 94   )   + (   81 + 74)))*   ( (   (  19+  25   )   +  (77  / 12   )   )  +   ( 60+   ( 66-100))))  ) ))  *   81)   + (   ( (86 -( ( (  (  (98   -   56   ) +   (   88   +  62 ))   -(  (   66 *  58) *(3  + 64   ) ))+(100   +  ( ( 5   /86  )  - (   85* 13 ) )  )   )   +(  (  72   +   (  ( 63+98)+  ( 16  + 72  )))   /  ((   ( 11  + 81)   / (  32   *7   ) )  +(   (   3   +  4   ) +  (81  *47   )  )) ))   )- ( ((  ((  (  53  +  26)   - (   97  /42 )   )   / (   (  30  +   37   )   *  ( 28 +69)  ) )   +  ( ( 47  *   (  55  * 36   )   )*  76))   -   ((( 49/   ( 95  *3  )   )+(  (20  + 87  )*  61  ) )+  (( ( 94 *   41   )   + (78  +12   )  )-(( 34+ 52  )  +(  84 /   33 )  )   ) )  )   *90  )   ) + (   (  ( (  (   ( (59 * 24  )   +  (   85   *  15   )   )+   (  (   92  +   58)   -(   97  -   57  ) )  )   /(   (  (   90/37)+( 74   + 34  ))  *  (  91+  (   58 /  73   ) )   ))   +( ( ( (19 -  66   ) -   (42 *75   ) ) - (  (  20- 10 )   +(  72-97)   )  )   *  (( 93  + (91   - 65 )   )+   (  ( 63 *   7 ) +   (1+14)  )   )  )  )  -((  (   (  (  95/39)   +72 )*  ( ( 86   - 31) +  ( 23/  88)   )   ) / (   (   (   97  - 55  )  +(24  -  49))+ (   (  84   +   64   )   +  44 ) )  )   +  (   67  + (   ( (   45   -   3  )+ (16   +   64  )   ) +  (   (15 -78 )*(3  + 57 )   )   ))))*   ( (  ( (( ( 83 -61  )  +  ( 55+  63   ) )  *   (  ( 93  +2   )   /  ( 76  +  25)   ) )* (   ( ( 75  /   50 )   +  (   99  + 19))- (  (  99+ 63 )   +( 63  *40 ) ))  ) -  ( 1   +( (   (  17 *  5)+ (8 + 40   )   )*  ( (   48  -66  )   - (   85   +   2 )   )) )   )  -  (  ((  (  (  37   +   16 )  *  59   )+   (   (   32 *   36   )-  (  53+  39))   )- (   (  69-34 )-  ((  79 *  66 )   -( 3 *   9  ) )   ))  /   ( (  (  (   75   +   81 )  / (   38  -   30)   )  *   (  (   99   * 93   )   + ( 100 +  88  )  )  )   *((  46   / ( 33  +18   ) )   +   ( (100   * 8 )   - (63+   92   )   ))) )  ))   ) )   /  (   ( (   ((   (  (  ( ( 56  + 94)   +   (   23  -23 )  ) -(  (63  +   26 )+  (  59   + 51 ) )  ) +  ( ( (45 +   71  ) +( 51  / 24)   ) -   15  ) )*   ( (  ((55+   61 )/  4 )   *  (   22   -  (  47-  78 )  )   ) /   (( (19   *69)  + (  18+  81)  )   +   (  ( 59  / 3  )   +   (  54   *1)   ) )   ) ) *   32)   * (   89  -( ( (   (   (  40/   51  ) +(  61 / 16  )  )/( (89 *  20   )  -   ( 88   -  41   ))   ) + 19   )  /( (((  48   + 19 )  -(71   *  58   )) *(   (   73 /   48 )  / (  8  +  33  ) )  )+( (   (92 +47  )   +( 12 * 56 )   )+  ( (   12*  68   )  +  36   ))  ))  )   ) +   (   (  ( ((   (   (72+   4   ) - (   97 /  33   ) )+( (   30  - 2)  /  (   99 +  87)   )) *(  (( 51 +  25)  *  (47  +   87  ))  *  (( 48  *  78   )  -  ( 79 +   68  )   ) ) )  - (   ((  (  41   +55   )-   (   68+20   ) ) +  ( (   85  /18)   + (  9   - 74 )))+  30 )  )   -(  (   55*(   ((81 /26 )  +  (45+  39) )   *(   (53*93)   + (40  +54)   ) ))   - (  ( (  (53   + 44 ) -  (28  -  29  )   ) +(   (36  /  4  )*  (   33  - 24))  )  +   (  (  ( 88   -   62)+ (   93  *   77 )  ) +  (  (   23   +  34 )   *( 1 /   94) ))) )  )  +   (15 *(   ( ((  ( 22+82  )   +  (77   +   84)   )*  (  (   30  -   34)- (   66 -   29  )   ) )   + (  (  70-(   62 -14  )  )+(   (22  /  70   ) + ( 22   - 39)   )) )  -( (   (  ( 18  + 31 )   + (7  * 92  ))+  (96 + (  10 +37   ))  )   -   (  ( ( 97*  14  ) +43)   *  (   (   100 *25 ) /  (95 +93  )   )  )   )   ))  )  ) *( ( (  (  (   (   ((  14  *54  ) *  (5   +  80  ))+  (  (  14+ 46   )*(  55*  36   ) )   )   -  98   ) +   (   (  ( (  97 *  97  )   +(62   /20  )) +  (   (54- 40   )  +(   24+45 )  )   )  - (  ( (  15 + 4 )   - ( 52  +77  ))   +( (94   - 92   ) +(  96   *24 ) ) )  )  )  + (   ((((  91  *65   )- (   66  *62   ) )  /(   4 + (   86+ 58   )   )   )  *(  87 - (  (  40   -   82)  +  (   61 +  87))) )  *   (   61 -  23   )   ))  - ((  ((   ((  41  - 43 )   +(74  /   7 )  ) - ( (   25   -  12   )   +  (28*74))   )+( 88  +  22 ))  *70)- 83)   )  -( ((   98 / 11   )   *   (  (  (  ( (   66+43 )*(  58 -  40  ) )+(  (   18+27)   +  (   91  -   59) ))-   ((  (  49   +29 ) - 84 )   +(  (  10   /15  ) +( 44*   89 )   )  ))+  (  (  92* (   3  +  (92   + 62)   ) )  -(   99   /   ( (   73  + 34   )   +(  78   -  35 )  )   )) )  ) /   57 ))  )   )";
  Solution solution;
  auto anw = solution.calculate(s);
  cout << anw << endl;
  return 0;
}
