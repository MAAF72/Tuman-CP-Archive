#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int c;
        cin >> c;
        int total = 0;
        int maks = 0;
        for (int j = 0; j < c; j++){
            int tmp;
            cin >> tmp;
            total += tmp;
            maks = max(maks,tmp);
        }
        int res = total - (maks*2);
        if(res >= 0){
            cout << "true" << endl;
        }else{
            cout << "false" << endl;
        }
    }
}