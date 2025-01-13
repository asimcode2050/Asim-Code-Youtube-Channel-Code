#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

class Graph {
public:
    unordered_map<int, vector<int>> adjList;
    unordered_map<int, bool> visited;
    stack<int> topologicalOrder;
    void addEdge(int u, int v) {
        adjList[u].push_back(v);  // 'u' -> 'v' edge
    }

    void dfs(int node) {
        visited[node] = true;
        cout << "Visiting node " << node << endl;
        for (int neighbor : adjList[node]) {
            if (!visited[neighbor]) {
                cout << "Neighbor " << neighbor << " of node " << node << " is unvisited, doing DFS!" << endl;
                dfs(neighbor);  
            }
        }

        topologicalOrder.push(node);
        cout << "Adding node " << node << " to topological order (stack)" << endl;
    }

    void topologicalSort() {
        for (auto& entry : adjList) {
            if (!visited[entry.first]) {
                cout << "Starting DFS from node " << entry.first << endl;
                dfs(entry.first);  // Start DFS from this node
            }
        }

        cout << "Topological Sort Order: ";
        while (!topologicalOrder.empty()) {
            cout << topologicalOrder.top() << " ";
            topologicalOrder.pop(); 
        }
        cout << endl;
    }
};

int main() {
    Graph g;

    g.addEdge(5, 2);  // 5 -> 2
    g.addEdge(5, 0);  // 5 -> 0
    g.addEdge(4, 0);  // 4 -> 0
    g.addEdge(4, 1);  // 4 -> 1
    g.addEdge(2, 3);  // 2 -> 3
    g.addEdge(3, 1);  // 3 -> 1
    g.topologicalSort();

    return 0;
}
