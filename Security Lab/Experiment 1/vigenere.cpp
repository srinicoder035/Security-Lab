#include<bits/stdc++.h> 
using namespace std; 
  
string generateKey(string str, string key) 
{ 
    int x = str.size(); 
  
    for (int i = 0; ; i++) 
    { 
        if (x == i) 
            i = 0; 
        if (key.size() == str.size()) 
            break; 
        key.push_back(key[i]); 
    } 
    return key; 
} 
  
string cipherText(string str, string key) 
{ 
    string cipher_text; 
  
    for (int i = 0; i < str.size(); i++) 
    { 
        int x = (str[i] + key[i]) %26; 
  
        x += 'A'; 
  
        cipher_text.push_back(x); 
    } 
    return cipher_text; 
} 
  
string originalText(string cipher_text, string key) 
{ 
    string orig_text; 
  
    for (int i = 0 ; i < cipher_text.size(); i++) 
    { 
        int x = (cipher_text[i] - key[i] + 26) %26; 
  
        x += 'A'; 
        orig_text.push_back(x); 
    } 
    return orig_text; 
} 
  
int main() 
{ 
    cout << "Enter the string to be encrypted: ";
    string s;
    cin >> s;
    cout << "Enter the keyword: ";
    string keyword;
    cin >> keyword;
    string key = generateKey(s, keyword); 
    cout<< endl <<"Generated Key is: "<<key<<endl;
    string cipher_text = cipherText(s, key); 
  
    cout << endl << "Encryptedtext : "<< cipher_text << endl; 
  
    cout << endl << "Original/Decrypted Text : "<< originalText(cipher_text, key) <<endl;
    return 0;
}