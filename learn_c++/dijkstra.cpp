#include <iostream>
#include <vector>
#include <queue>
#include <climits> // For INT_MAX (to represent infinity)
using namespace std;
struct Edge
{
    int dest, weight;

    Edge(int d, int w) : dest(d), weight(w) {}
};

void dijkstra(int vertices, vector<vector<Edge>> &adjList, int start)
{
    vector<int> dist(vertices, INT_MAX);
    dist[start] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    while (!pq.empty())
    {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();
        if (d > dist[u])
        {
            continue;
        }

        for (const Edge &e : adjList[u])
        {
            int v = e.dest;
            int weight = e.weight;
            if (dist[u] + weight < dist[v])
            {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    cout << "Shortest distances from node " << start << ":\n";
    for (int i = 0; i < vertices; i++)
    {
        if (dist[i] == INT_MAX)
        {
            cout << "Node " << i << ": Unreachable\n";
        }
        else
        {
            cout << "Node " << i << ": " << dist[i] << endl;
        }
    }
}

int main()
{
    int vertices = 6;
    vector<vector<Edge>> adjList(vertices);
    adjList[0].push_back(Edge(1, 5));
    adjList[0].push_back(Edge(2, 10));
    adjList[1].push_back(Edge(2, 2));
    adjList[1].push_back(Edge(3, 1));
    adjList[2].push_back(Edge(4, 3));
    adjList[3].push_back(Edge(5, 4));
    adjList[4].push_back(Edge(5, 1));

    dijkstra(vertices, adjList, 0);

    return 0;
}
