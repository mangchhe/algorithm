#include <stdio.h>
#include <deque>

using namespace std;

deque<int> graph[101];
int visited[101];
int count;

void bfs(int n){
    while(!graph[n].empty()){
        int size = graph[n].size();
        for(int i=0; i<size; i++){
            int tmp = graph[n].front();
            if(!visited[tmp]){
                visited[tmp] = 1;
                count++;
                bfs(tmp);
            }
            graph[n].pop_front();
        }
    }
}

int main(){

    int n, m;

    scanf("%d", &n);
    scanf("%d", &m);

    for (int i=0; i<m; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    visited[1] = 1;
    bfs(1);
    printf("%d", count);

    return 0;
}