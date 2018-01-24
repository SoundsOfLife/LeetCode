#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <deque>
#include <map>

using namespace std;

class Solution {
public:
    bool isNum(string str){
      for(int i = 0;i < str.size();i++){
        if(str[i] > '9' || str[i] < 'a'){
          return false;
        }
      }
      return true;
    }

    multiset<string> order(string str){
      multiset<string> mss;
      int flag = 0;
      for(auto i = 0;i < str.size();i++){
          if(str[i] == '*'){
            mss.insert(str.substr(flag,i  - flag));
            flag = i + 1;
          }
      }
      mss.insert(str.substr(flag));
      return mss;
    }

/*
    string subtraction(const map<string,int> a,const map<string,int> b){
      string[] values =
    }

    string addition(const map<string,int> a,const map<string,int> b){
      return a + " " + b;
    }

    string multiplication(const map<string,int> a,const map<string,int> b){

    }
*/
    vector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {
        string temp = "";
        for(int i = 0;i < expression.size();i++){
            string t = "~";
            t[0] = expression[i];
            if(expression[i] == '('){
                temp += t;
                temp += " ";
            }else if(expression[i] == ')'){
                temp += " ";
                temp += t;
            }else{
                temp += t;
            }
        }
        expression = temp;
        vector<string> ret;
        map<string,int> msi;
        for(auto i = 0;i < evalints.size();i++){
            msi.insert(pair<string,int>(evalvars[i],evalints[i]));
        }
        stack<string> s1,s2;
        s1.push("#");
        int begin = 0;
        for(int i = 0;i < expression.size();i++){
            string str = "~";
            str[0] = expression[i];
            if(expression[i] == ' '){
                string value = expression.substr(begin, i - begin);
                if(value != ""){
                    s2.push(value);
                }
                begin = i + 1;
            }else if(expression[i] == '('){
                s1.push(str);
                begin = i + 1;
            }else if(expression[i] == ')'){
                while(s1.top() != "("){
                    string val = s1.top();
                    s2.push(val);
                    s1.pop();
                }
                s1.pop();
                begin = i + 1;
            }else if(expression[i] == '*'){
                while(s1.top() == "*" ){
                    string val = s1.top();
                    s2.push(val);
                    s1.pop();
                }
                s1.push(str);
                begin = i + 1;
            }else if (expression[i] == '+' || expression[i] == '-'){
                while(s1.top() == "*" || s1.top() == "-" || s1.top() == "+"){
                    string val = s1.top();
                    s2.push(val);
                    s1.pop();
                }
                s1.push(str);
                begin = i + 1;
            }
        }
        stack<string> s;
        while(!s2.empty()){
            s.push(s2.top());
            s2.pop();
        }

        return ret;
    }
};

int main(int argc, char const *argv[]) {
    /* code */
    string expression = "((ac - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))";
    // string expression = "3 + 4";
    vector<string> evalvars;
    vector<int> evalints;
    Solution solution;
    auto anw = solution.basicCalculatorIV(expression, evalvars, evalints);
    auto test = solution.order("-2*a*bbb*a*b*abc");
    for(auto it = test.begin();it != test.end();it++){
      cout  << *it << endl;
    }
    // cout << anw.size() << endl;
    return 0;
}
