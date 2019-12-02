#include<bits/stdc++.h>
using namespace std;

/**
 * Function to genenrate matrix
 * */
void getKeyMatrix(string key, int keyMatrix[][100], int n) 
{ 
    int k = 0; 
    for (int i = 0; i < n; i++)  
    { 
        for (int j = 0; j < n; j++)  
        { 
            keyMatrix[i][j] = (key[k]) % 65; 
            k++; 
        } 
    } 
} 
  
/**
 * Function to perform encryption
 * */
void encrypt(int cipherMatrix[][1], int keyMatrix[][100], int messageVector[][1], int n) 
{ 
    int x, i, j; 
    for (i = 0; i < n; i++)  
    { 
        for (j = 0; j < 1; j++) 
        { 
            cipherMatrix[i][j] = 0; 
            for (x = 0; x < n; x++) 
            { 
                cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j]; 
            } 
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26; 
        } 
    } 
} 

/**
 * Function to generate co factor matrix
 * */
void getCofactor(int A[][100], int temp[][100], int p, int q, int n) 
{ 
    int i = 0, j = 0; 
    for (int row = 0; row < n; row++) 
    { 
        for (int col = 0; col < n; col++) 
        { 
            if (row != p && col != q) 
            { 
                temp[i][j++] = A[row][col]; 
  
                if (j == n - 1) 
                { 
                    j = 0; 
                    i++; 
                } 
            } 
        } 
    } 
} 
  
/**
 * Function to determine the determinant
 * */
int determinant(int A[][100], int n) 
{ 
    int D = 0; 
    if (n == 1) 
        return A[0][0]; 
  
    int temp[100][100];  
  
    int sign = 1;  
    
    for (int f = 0; f < n; f++) 
    { 
        getCofactor(A, temp, 0, f, n); 
        D += sign * A[0][f] * determinant(temp, n - 1); 
  
        sign = -sign; 
    } 
  
    return D; 
} 
  
/**
 * Function to calculate adjoint matrix
 * */
void adjoint(int A[][100],int adj[][100], int n) 
{ 
    int sign = 1, temp[100][100]; 
  
    for (int i=0; i<n; i++) 
    { 
        for (int j=0; j<n; j++) 
        { 
            getCofactor(A, temp, i, j, n); 
  
            sign = ((i+j)%2==0)? 1: -1; 
  
            adj[j][i] = (sign)*(determinant(temp, n-1)); 
        } 
    } 
} 

/**
 * Function to calculate the inverse of a matrix
 * */
bool inverse(int A[][100], float inverse[][100], int n) 
{ 
    int det = determinant(A, n); 
    if (det == 0) 
    { 
        cout << "Singular matrix, can't find its inverse"; 
        return false; 
    } 
  
    int adj[100][100]; 
    adjoint(A, adj, n); 
  
    for (int i=0; i<n; i++) 
        for (int j=0; j<n; j++) 
            inverse[i][j] = adj[i][j]/float(det); 
    
    cout<<"\n\nInverse Matrix is:\n";
	for(int i = 0; i < 3; i++) {
		for(int j = 0; j < 3; j++)
			cout<<inverse[i][j]<<" ";
		
		cout<<"\n";
	}
  
    return true; 
}

/**
 * Function to calculate decyption 
 * */
void decrypt(int cipherMatrix[][1], int keyMatrix[][100], int messageVector[][1], int n) 
{
    int i, j, k;
    float inverseMatrix[100][100];
	
	inverse(keyMatrix, inverseMatrix, n);

    cout<<endl;
	
	for(i = 0; i < n; i++)
    {
        for(j = 0; j < 1; j++)
        {
            messageVector[i][j] = 0;
            for(k = 0; k < n; k++)
				messageVector[i][j] += inverseMatrix[i][k] * cipherMatrix[k][j];
        }
        messageVector[i][j] %= 26;
    }
}
  
/**
 * Function to perform the encryption of Hill Cipher
 * */
void HillCipher(string message, string key) 
{ 
    int n = message.length();
    int keyMatrix[100][100]; 
    getKeyMatrix(key, keyMatrix, n); 
  
    int messageVector[100][1]; 
  
    for (int i = 0; i < n; i++) 
        messageVector[i][0] = (message[i]) % 65; 
  
    int cipherMatrix[100][1]; 
  
    encrypt(cipherMatrix, keyMatrix, messageVector, n); 
  
    string CipherText; 
  
    for (int i = 0; i < n; i++) 
        CipherText += cipherMatrix[i][0] + 65; 
    
    for(int i=0;i<n;i++)
    {
        cipherMatrix[i][0] = (CipherText[i]) %65;
    }
  
    cout << "Ciphertext: " << CipherText<<endl;

    cout<<endl;

    int messageMatrix[100][1];
    decrypt(cipherMatrix, keyMatrix, messageMatrix, n); 

    string messageText;
	for(int i = 0; i < n; i++)
		messageText += (messageVector[i][0] + 65);
	
	cout<<"Decrypted text: "<<messageText<<endl;

} 
  
int main() 
{ 
    string message, key;
    cout<<"Enter the string to be encrypted"<<endl;
    cin>>message;
    cout<<"Enter the key: ";
    cin>>key; 
    HillCipher(message, key); 
    return 0; 
} 