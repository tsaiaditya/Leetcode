#include<iostream>
using namespace std;
int h;
int w;

void markNeigbors(char grid[1000][1000], int x, int y) {
    if (x < 0 || x >= h || y < 0 || y >= w || grid[x][y] != '1')
        return;
    grid[x][y] = '2';
    markNeigbors(grid, x + 1, y);
    markNeigbors(grid, x - 1, y);
    markNeigbors(grid, x, y + 1);
    markNeigbors(grid, x, y - 1);
}

int numIslands(char grid[1000][1000]) {
    
    if (h == 0)
        return 0;
    int islandCount = 0;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (grid[i][j] == '1') {
                markNeigbors(grid, i, j);
                ++islandCount;
            }
        }
    }
    return islandCount;
}

int main(int argc, char const *argv[])
{
    int m,n;
    cout<<"Enter the rows and columns required: ";
    cin>>m>>n;
    h=m;
    w=n;
    char grid[1000][1000];
    cout<<"Enter the grid: "<<endl;
    for(int i = 0; i<m; i++)
        for(int j = 0; j<n; j++)
            cin>>grid[i][j];
    cout<<"Number of islands: "<<numIslands(grid);
    return 0;
}
