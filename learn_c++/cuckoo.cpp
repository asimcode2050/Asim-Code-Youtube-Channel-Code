#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

class CuckooHashTable
{ // Definition of the CuckooHashTable class
private:
    vector<int> table1;
    vector<int> table2;
    int size1, size2;
    static const int NUM_HASH_FUNCTIONS = 2;

public:
    CuckooHashTable(int table1_size, int table2_size)
    {
        size1 = table1_size;
        size2 = table2_size;

        table1.resize(size1, -1);
        table2.resize(size2, -1);
    }

    int hash1(int key)
    {
        return key % size1; 
    }

    int hash2(int key)
    {
        return key % size2;
    }

    void insert(int key)
    {
        int current_key = key;
        int current_table = 1;
        for (int i = 0; i < size1 + size2; i++)
        {
            if (current_table == 1)
            {
                int index = hash1(current_key);
                if (table1[index] == -1)
                {
                    table1[index] = current_key;
                    cout << "Inserted " << current_key << " into table1 at index " << index << endl;
                    return;
                }
                else
                { // If there is a collision (slot already occupied)
                    cout << "Collision in table1 at index " << index << ". Kicking out " << table1[index] << endl;
                    current_key = table1[index];
                    table1[index] = current_key;
                    current_table = 2;
                }
            }
            else
            {
                int index = hash2(current_key); 
                if (table2[index] == -1)
                {
                    table2[index] = current_key;
                    cout << "Inserted " << current_key << " into table2 at index " << index << endl;
                    return;
                }
                else
                {
                    cout << "Collision in table2 at index " << index << ". Kicking out " << table2[index] << endl;
                    current_key = table2[index];
                    table2[index] = current_key;
                    current_table = 1;
                }
            }
        }
        throw runtime_error("Too many collisions. Consider resizing the hash tables.");
    }

    bool search(int key)
    {
        int index1 = hash1(key); 
        if (table1[index1] == key)
        {
            cout << "Found " << key << " in table1 at index " << index1 << endl;
            return true;
        }

        int index2 = hash2(key); 
        if (table2[index2] == key)
        {
            cout << "Found " << key << " in table2 at index " << index2 << endl;
            return true; 
        }

        cout << key << " not found." << endl;
        return false;
    }

    void print()
    {
        cout << "Table1: ";
        for (int i = 0; i < size1; i++)
        {
            if (table1[i] == -1)
                cout << "[] "; // Empty slot is represented by []
            else
                cout << "[" << table1[i] << "] "; 
        }
        cout << endl;

        cout << "Table2: ";
        for (int i = 0; i < size2; i++)
        {
            if (table2[i] == -1)
                cout << "[] "; 
            else
                cout << "[" << table2[i] << "] "; 
        }
        cout << endl;
    }
};

int main()
{
    CuckooHashTable ht(5, 5);

    ht.insert(10);
    ht.insert(20);
    ht.insert(30);
    ht.insert(40);
    ht.insert(50);

    ht.print();
    ht.search(20);
    ht.search(100);

    return 0;
}
