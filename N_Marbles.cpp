#include<iostream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
/*Ques. A craftsman has N marbles, each colored Red (0), White (1), 
or Blue (2). The marbles are arranged in a line, but they are unordered. 
Your task is to sort the marbles in-place such that all Red (0) 
marbles come first, followed by White (1), and then Blue (2).  

Input Format (String): "N C1 C2 C3 ... CN"Where:N is the number 
of marbles.Ci represents the color of the i-th 
marble (0, 1, or 2).*/

void sortMarbles(vector<int>& marbles){
int low=0;
int mid=0;
int high=marbles.size()-1;
while(mid<=high){
    if(marbles[mid]==0){
        swap(marbles[low],marbles[mid]);
        low++;
        mid++;
    }
    else if(marbles[mid]==1){
        mid++;
    } else{
        swap(marbles[mid],marbles[high]);
        high--;
    }
  }
}

int main(){
string inputline;
getline(cin,inputline);
stringstream ss(inputline);
int N;
if(!(ss>>N))
return 0;
vector<int>marbles(N);
for(int i=0;i<N;++i){
ss>>marbles[i];
}
sortMarbles(marbles);
for (int i = 0; i < N; ++i) {
    cout << marbles[i] << (i == N - 1 ? "" : " ");
    }
    cout << endl;
return 0;
}