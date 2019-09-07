#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;

int main(){
    int v = 4;
    vector<pii>graph[v];
    
    graph[0].push_back(make_pair(1, 2));
    graph[0].push_back(make_pair(2, 6));
    graph[1].push_back(make_pair(2, 3));
    graph[3].push_back(make_pair(0, 7));

    function <int(vector<pii>[], int, int, int)> dijkstra = [](vector<pii>g[], int v, int start, int end){
        vector<int>dist(v, INT_MAX);
        set<pii> initial;
        initial.insert(make_pair(0, start));
        dist[start] = 0;

        while(!initial.empty()){
            pii tmp = *initial.begin();
            initial.erase(initial.begin());
            int u = tmp.second;
        
            for(auto i : g[u]){
                int z = i.first;
                int w = i.second;
                if(dist[z] > dist[u] + w){
                    if(dist[z] != INT_MAX)
                        initial.erase(initial.find(make_pair(dist[z],z)));
                    dist[z] = dist[u] + w;
                    initial.insert(make_pair(dist[z], z));
                }
            }
        }
        if(dist[end] != INT_MAX)
            return dist[end];
        return -1;
    };

    cout << dijkstra(graph, v, 0, 2) << endl;
    return 0;
}