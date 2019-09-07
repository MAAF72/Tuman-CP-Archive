#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define ll long long
typedef pair<ll,ll> pii;
typedef pair<pii,ll> piii;

ll kuadrat(ll a){
    return a*a;
}

ll dist(pii a, pii b){
    return kuadrat((a.first - b.first)) + kuadrat((a.second - b.second));
}

int main(){
    ll t;
    cin>> t;
    for(ll i = 1; i <= t; i++){
        ll v;
        cin>> v;
        pii tmp[v];
        for (ll j = 0; j < v; j++){
            ll x,y;
            cin>>x>>y;
            tmp[j] = make_pair(x,y);
        }
        ll c = ((v+1)*v)/2;
        piii e[c];
        ll y = 0;
        for(ll j = 0; j < v;j++){
            for(ll k = j+1; k < v;k++){
                e[y++] = make_pair(make_pair(j,k),dist(tmp[j],tmp[k]));
            }
        }
        auto comparator = [](piii p, piii q){
            return p.second < q.second;
        };
        
        sort(e,e +c,comparator);
        
        vector<ll> link(v);
        for(ll l =0; l <v;l++) link[l] = l;
        
        vector<ll> size(v,1);

        function <ll(ll)> find = [&link](ll x){
            while(x != link[x]) x = link[x];
            return x;
        };
        function<bool(ll,ll)> same = [&find](ll x, ll y){
            return find(x) == find(y);
        };
        function<void(ll,ll)> unite = [&find, &link, &size](ll x, ll y){
            x = find(x);
            y = find(y);
            if(size[x] > size[y]) swap(x,y);
            size[y] += size[x];
            link[x] = y;
        };

        ll ans = 0;
        for(ll j =0; j < c; j++){
            piii P = e[j];
            if(!same(P.first.first,P.first.second)){
                unite(P.first.first,P.first.second);
                ans = P.second;
            }
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
