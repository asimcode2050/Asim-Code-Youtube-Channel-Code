#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTICES 10
typedef struct
{
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} Graph;

/* In the adjacency matrix, each element `adjMatrix[i][j]` represents an edge between vertex `i` and vertex `j`.
- If `adjMatrix[i][j] = 1`, it means there is an edge between vertices `i` and `j`.
- If `adjMatrix[i][j] = 0`, it means there is no edge between them.
*/

void initGraph(Graph *g)
{
  for (int i = 0; i < MAX_VERTICES; i++)
  {
    for (int j = 0; j < MAX_VERTICES; j++)
    {
        g->adjMatrix[i][j] = 0;
    }
  }
  g->numVertices = 0;
  printf("Graph initialized. No vertices or edges yet.\n");
}

void addVertex(Graph *g)
{
  if (g->numVertices < MAX_VERTICES)
  {
      g->numVertices++;
      printf("Vertex %d added to the graph.\n", g->numVertices - 1);
  }
  else
  {
      printf("Maximum number of vertices reached. Cannot add more.\n");
  }
}

void addEdge(Graph *g, int u, int v)
{
  if (u >= 0 && u < g->numVertices && v >= 0 && v < g->numVertices)
  {
      g->adjMatrix[u][v] = 1;
      g->adjMatrix[v][u] = 1;
      printf("Edge added between Vertex %d and Vertex %d.\n", u, v);
  }
  else
  {
      printf("Invalid vertices. Edge not added.\n");
  }
}

/*  
We then set `adjMatrix[u][v] = 1` to indicate an edge from `u` to `v`, and similarly set `adjMatrix[v][u] = 1` for the reverse edge (since it's undirected).
- If either vertex is invalid, we display an error message.
*/


void displayGraph(Graph *g)
{
    printf("\nGraph Adjacency Matrix:\n");
  for (int i = 0; i < g->numVertices; i++)
  {
    for (int j = 0; j < g->numVertices; j++)
    {
        printf("%d ", g->adjMatrix[i][j]);
    }
    printf("\n");
  }
}


void DFS(Graph *g, int vertex, int visited[])
{
    visited[vertex] = 1;
    printf("Visited Vertex: %d\n", vertex);

  for (int i = 0; i < g->numVertices; i++)
  {
    if (g->adjMatrix[vertex][i] == 1 && !visited[i])
    {
        DFS(g, i, visited);
    }
  }
}


void startDFS(Graph *g, int startVertex)
{
    int visited[MAX_VERTICES] = {0};
    printf("\nStarting DFS from Vertex %d:\n", startVertex);
    DFS(g, startVertex, visited); 
}



int main()
{
    Graph g;
    initGraph(&g);

    addVertex(&g);
    addVertex(&g);
    addVertex(&g);

    addEdge(&g, 0, 1);
    addEdge(&g, 1, 2);

    displayGraph(&g);
    startDFS(&g, 0);

    return 0;
}
