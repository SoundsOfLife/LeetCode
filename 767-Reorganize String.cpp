#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <iterator>

using namespace std;

class Solution {
  public:
    struct {
        bool operator()(pair<int,char> a, pair<int,char> b) const {
            return a.first < b.first;
        }
    } cmp;
    string reorganizeString(string S) {
        auto length = S.size();
        map<char, int> mci;
        vector<pair<int, char>> vic;
        for(auto i = 0;i < length;i++){
          if(mci.count(S[i]) != 0){
            mci.find(S[i])->second = mci[S[i]] + 1;
          }else{
            mci.insert(pair<char, int>(S[i], 1));
          }
        }
        for(auto iter = mci.begin();iter != mci.end();iter++){
          vic.push_back(pair<int,char>(iter->second, iter->first));
        }
        sort(vic.begin(),  vic.end(), cmp);
        if(vic.rbegin()->first * 2 - 1 > length){
          return "";
        }else{
          string temp = string(vic.rbegin()->first,vic.rbegin()->second);
          string t = "";
          for(auto it = vic.rbegin() + 1; it != vic.rend();it++){
              t.insert(t.size(), it->first, it->second);
          }
          string anw = "";
          if(t.size() + 1 == temp.size()){
            for(auto i = 0;i < t.size();i++){
              anw += temp[i];
              anw += t[i];
            }
            anw += temp[0];
          }else{
            int len = t.size() / temp.size();
            for(auto j = 0;j < temp.size();j++){
                anw += temp[j];
                for(auto i = 0;i < len;i++){
                  anw += t[i * temp.size() + j];
                }
            }
            if(t.size() % temp.size() != 0){
              int loc = 0;
              for(auto j = len * temp.size();j < t.size();j++){
                  anw.insert(anw.begin()+loc,t[j]);
                  loc += 2;
              }
            }
          }
          return anw;
        }
    }
};

int main(){
  // string str = "gpneqthatplqrofqgwwfmhzxjddhyupnluzkkysofgqawjyrwhfgdpkhiqgkpupgdeonipvptkfqluytogoljiaexrnxckeofqojltdjuujcnjdjohqbrzzzznymyrbbcjjmacdqyhpwtcmmlpjbqictcvjgswqyqcjcribfmyajsodsqicwallszoqkxjsoskxxstdeavavnqnrjelsxxlermaxmlgqaaeuvneovumneazaegtlztlxhihpqbajjwjujyorhldxxbdocklrklgvnoubegjrfrscigsemporrjkiyncugkksedfpuiqzbmwdaagqlxivxawccavcrtelscbewrqaxvhknxpyzdzjuhvoizxkcxuxllbkyyygtqdngpffvdvtivnbnlsurzroxyxcevsojbhjhujqxenhlvlgzcsibcxwomfpyevumljanfpjpyhsqxxnaewknpnuhpeffdvtyjqvvyzjeoctivqwann";
  string str = "bfrbs";
  Solution solution;
  auto anw = solution.reorganizeString(str);
  cout << anw << endl;
}
