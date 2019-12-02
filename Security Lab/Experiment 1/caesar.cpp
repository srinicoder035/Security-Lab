#include<iostream>
#include<string>
using namespace std;

/**
 * Function for encryption 
 * */
string caesarEncrypt(string text, int s) 
{ 
    string result = ""; 
    for (int i=0;i<text.length();i++) 
    { 
        if (isupper(text[i])) 
            result += char(int(text[i]+s-65)%26 +65); 
        else if (islower(text[i]))
            result += char(int(text[i]+s-97)%26 +97); 
    } 
    return result; 
} 

/**
 * Function for Decryption
 * */
string caesarDecrypt(string text, int key)
{
    for(int i = 0; i<text.length(); i++)
    {
		if (islower(text[i]))
		{
			text[i] = text[i] - key;
			if(text[i] < 'a'){
				text[i] = text[i] + 'z' - 'a' + 1;
			}
		}
		else if (isupper(text[i]))
		{
			text[i] = text[i] - key;
			if(text[i] < 'A'){
				text[i] = text[i] + 'Z' - 'A' + 1;
			}
		}
	}
	return text;
}

int main()
{
	string str;
	int k;
	cout<<"Enter the string to be encrypted"<<endl;
	cin>>str;
	cout<<"Enter the key: ";
    cin>>k;
    string encrypted_string = caesarEncrypt(str,k);
    cout<<"Encrypted string: "<<encrypted_string<<endl;
    cout<<"The string after decryption is: "<<caesarDecrypt(encrypted_string, k)<<endl; 
	return 0;
}