/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

//BFS Solution
class Solution {
public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> v;
        if (node==NULL)
            return node;
        queue<Node*> q;
        q.push(node);
        Node* n1 = new Node(node->val, {});
        v[node] = n1;
        while(!q.empty())
        {
            Node* n = q.front();
            q.pop();
            
            Node* new_node = v[n];
            
            for (auto nbr: n->neighbors)
            {
                if(v[nbr])
                {
                    new_node->neighbors.push_back(v[nbr]);
                }
                else
                {
                    Node* new_nbr = new Node(nbr->val, {});
                    q.push(nbr);
                    v[nbr] = new_nbr;
                    new_node->neighbors.push_back(new_nbr);
                }
            }
        }
        
        return v[node];
    }
};