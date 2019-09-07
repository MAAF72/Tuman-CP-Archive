#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
typedef pair<int,int> pii;
typedef pair<pii,int> piii;

int main(){
    int v = 4;
    int e = 4;
    piii edge[e];
    
    edge[0] = make_pair(make_pair(0, 1), 10);
    edge[1] = make_pair(make_pair(0, 2), 5);
    edge[2] = make_pair(make_pair(1, 2), 3);
    edge[3] = make_pair(make_pair(3, 0), 7);

    auto comparator = [](piii p, piii q){
        return p.second < q.second;
    };
    sort(edge,edge +e,comparator);

    vector<int> link(v);
    for(int i =0; i <v;i++) link[i] =i;

    vector <int> size(v,1);

    function <int(int)> find = [&link](int x){
        while(x != link[x]) x = link[x];
        return x;
    };
    function<bool(int,int)> same = [&find](int x, int y){
        return find(x) == find(y);
    };
    function<void(int,int)> unite = [&find, &link, &size](int x, int y){
        x = find(x);
        y = find(y);
        if(size[x] > size[y]) swap(x,y);
        size[y] += size[x];
        link[x] = y;
    };
    int ans = 0;
    for(int i =0; i < e; i++){
        piii P = edge[i];
        if(!same(P.first.first,P.first.second)){
            unite(P.first.first,P.first.second);
            ans += P.second;
        }
    }
    cout<<ans<<endl;
    return 0;
}