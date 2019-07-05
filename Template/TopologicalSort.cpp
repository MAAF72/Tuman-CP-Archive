#include <bits/stdc++.h>
using namespace std;
int main(){
    int v = 4;
    int e = 4;
    vector<int> graph[v];
    graph[0].push_back(1);
    graph[0].push_back(2);
    graph[1].push_back(2);
    graph[3].push_back(0);
    function <void(vector<int>[], int, int)>topologicalSort = [](vector<int>g[], int v, int e){
        vector<int> inDegree(v,0);
        for(int i = 0; i < v; i++)
            for(auto x : g[i])
                inDegree[x]++;
        queue<int> initial;
        for(int i = 0; i < v; i++)
            if(inDegree[i] == 0)
                initial.push(i);
        vector<int> ans;
        while(!initial.empty()){
            int tmp = initial.front();
            initial.pop();
            ans.push_back(tmp);
            for(auto x : g[tmp])
                if(--inDegree[x] == 0)
                    initial.push(x);
        }
        if(ans.size() == v)
            for(auto x : ans)
                cout << x << " ";
        cout << endl;
    };
    topologicalSort(graph,v,e);
    return 0;
}