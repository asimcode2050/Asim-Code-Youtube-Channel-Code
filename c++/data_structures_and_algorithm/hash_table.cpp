#include <iostream>
#include <list>
#include <vector>
using namespace std;
template <typename K, typename V>
class HashTable
{
private:
    static const int SIZE = 10;
    vector<list<pair<K, V>>> table;

public:
    HashTable()
    {
        table.resize(SIZE);
    }
    int hash(K key)
    {
        return key % SIZE;
    }
    void insert(K key, V value)
    {
        int index = hash(key);
        for (auto &pair : table[index])
        {
            if (pair.first == key)
            {
                pair.second = value; // If found, update the value
                return;
            }
        }
        table[index].push_back(make_pair(key, value));
    }
    V get(K key)
    {
        int index = hash(key);
        for (auto &pair : table[index])
        {
            if (pair.first == key)
            {
                return pair.second; // Return the value if found
            }
        }
        throw runtime_error("Key not found");
    }
    void remove(K key)
    {
        int index = hash(key);
        for (auto it = table[index].begin(); it != table[index].end(); ++it)
        {
            if (it->first == key)
            {
                table[index].erase(it); // Erase the pair if found
                return;
            }
        }
        throw runtime_error("Key not found");
    }
    void display()
    {
        for (int i = 0; i < SIZE; i++)
        {
            cout << "Bucket " << i << ": ";
            for (auto &pair : table[i])
            {
                cout << "(" << pair.first << ", " << pair.second << ") ";
            }
            cout << endl;
        }
    }
};
int main()
{
    HashTable<int, string> ht;
    ht.insert(1, "One");
    ht.insert(2, "Two");
    ht.insert(12, "Twelve");
    ht.insert(3, "Three");
    ht.display();
    try
    {
        cout << "Value for key 2: " << ht.get(2) << endl;
        cout << "Value for key 12: " << ht.get(12) << endl;
    }
    catch (const runtime_error &e)
    {
        cout << e.what() << endl;
    }
    try
    {
        ht.remove(2);
        cout << "After removing key 2:" << endl;
        ht.display();
    }
    catch (const runtime_error &e)
    {
        cout << e.what() << endl;
    }
    return 0;
}
