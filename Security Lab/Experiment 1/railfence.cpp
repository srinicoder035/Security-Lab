#include <bits/stdc++.h>
using namespace std;

string railfenceEncrypt(string s, int key)
{
    char railfence[key][s.length()];
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            railfence[i][j] = '#';
        }
    }

    bool move_down = false;
    int row = 0, col = 0;

    for (int i = 0; i < s.length(); i++)
    {
        if (row == 0 || row == key - 1)
        {
            move_down = !move_down;
        }

        railfence[row][col++] = s[i];

        if (move_down)
            row++;
        else
            row--;
    }

    cout << "Encryption RailFence is: " << endl;
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            cout << railfence[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    string encrypted_text;
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            if (railfence[i][j] != '#')
            {
                encrypted_text.push_back(railfence[i][j]);
            }
        }
    }
    return encrypted_text;
}

string railfenceDecrypt(string s, int key)
{
    char railfence[key][s.length()];
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            railfence[i][j] = '#';
        }
    }

    bool move_down;
    int row = 0, col = 0;

    for (int i = 0; i < s.length(); i++)
    {
        if (row == 0)
            move_down = true;
        if (row == key - 1)
        {
            move_down = false;
        }
        railfence[row][col++] = '*';
        if (move_down)
            row++;
        else
            row--;
    }

    int ind = 0;
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            if (railfence[i][j] == '*' && ind < s.length())
            {
                railfence[i][j] = s[ind++];
            }
        }
    }

    cout << "Decryption RailFence is: " << endl;
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < s.length(); j++)
        {
            cout << railfence[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    string original_text;
    row = 0, col = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (row == 0)
            move_down = true;
        if (row == key - 1)
            move_down = false;

        if (railfence[row][col] != '#')
        {
            original_text.push_back(railfence[row][col++]);
        }

        if (move_down)
            row++;
        else
            row--;
    }

    return original_text;
}

int main()
{
    cout << "Enter the string to be encrypted: ";
    string s;
    cin >> s;
    cout << "Enter the key: ";
    int key;
    cin >> key;
    string encrypted_text = railfenceEncrypt(s, key);
    cout << "Encrypted Text: " << encrypted_text << endl
         << endl;
    string decrypted_text = railfenceDecrypt(encrypted_text, key);
    cout << "Decrypted Text: " << decrypted_text << endl
         << endl;
    return 0;
}