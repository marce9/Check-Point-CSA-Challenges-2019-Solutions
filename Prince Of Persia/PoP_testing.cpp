#include <iostream>
#include <array>
#include <cstring>
#include <cstdlib>
#include <numeric>
#include <vector>

using namespace std;

#define N1 256



void swap(unsigned char *a, unsigned char *b) {
	unsigned char tmp = *a;
	*a = *b;
	*b = tmp;
}

int PRGA(unsigned char *S, char *plaintext, unsigned char *ciphertext) {
	int i = 0;
	int j = 0;
	for (size_t n = 0, len = strlen(plaintext); n < len; n++) {
		i = (i + 1) % N1;
		j = (j + S[i]) % N1;
		swap(&S[i], &S[j]);
		int rnd = S[(S[i] + S[j]) % N1];
		ciphertext[n] = rnd ^ plaintext[n];
	}
	return 0;
}

int KSA(char *key, unsigned char *S) {
	int len = 15;
	int j = 0;
	for (int i = 0; i < N1; i++)
		S[i] = i;
	for (int i = 0; i < N1; i++) {
		j = (j + S[i] + key[i % len]) % N1;
		swap(&S[i], &S[j]);
	}
	return 0;
}

int RC(char *key, char *plaintext, unsigned char *ciphertext) {

	unsigned char S[N1];
	KSA(key, S);

	PRGA(S, plaintext, ciphertext);

	return 0;
}


void cartesian( vector<vector<int> >& v ) {
  auto product = []( long long a, vector<int>& b ) { return a*b.size(); };
  const long long N = accumulate( v.begin(), v.end(), 1LL, product );
  vector<int> u(v.size());
  for( long long n=0 ; n<N ; ++n ) {
    lldiv_t q { n, 0 };
    for( long long i=v.size()-1 ; 0<=i ; --i ) {
      q = div( q.quot, v[i].size() );
      u[i] = v[i][q.rem];
    }
    // Do what you want here with u.
    for( int x : u ) cout << x << ' ';
    cout << '\n';
  }
}


int main()
{

    int block1[] = {214, 85, 173,9, 13, 217,126, 133, 241,98, 37, 11,50, 52, 8,18, 230, 22,122, 125, 160,86, 8, 226,17, 235, 234,154, 238, 250,210, 123, 171,178, 43, 98,237, 136, 68,184, 17, 74,113, 74, 138};
    char strrc[100] = { 0 };
    char decrypt[57] = { 0 };
	char finalstr[100] = { 0 };
    char decryptstr[100] = { 0 };
	char str[57] = {0};
	char rooms[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 20, 0};

    // printf("current_level: %d\n", current_level);
    // printf("win_room: %d\n", drawn_room);
    for (int i = 0, j = 0; i < 15 * 4; i++) {
        if (i % 4 != 3) {
            str[j*3 + i % 4] = block1[i-j];
        }
        else {
            j++;
        }
    }
    // for (const char* p = str; *p; ++p)
    // {
    //     printf("%d\n", *p);
    // }
    // printf("\n");
    // for (const char* p = str; *p; ++p)
    // {
    //     printf("%02x", *p);
    // }
    // printf("\n");
    for (int i = 0; i < 1; i++){
        // rooms[13] = i;
        RC(rooms, str, (unsigned char*)strrc);
        // sprintf(finalstr,"%s %s", "Great:", strrc);
        sprintf(finalstr,"%s", strrc);
        if (finalstr[7] == 'C' && finalstr[8] == 'S' && finalstr[9] == 'A'){
            printf("%s\n", finalstr);
        }
        printf("%s\n", finalstr);
        // char decrypt[57] = { 0 };
        // RC(rooms, strrc, (unsigned char*)decrypt);
        // sprintf(decryptstr,"%s", decrypt);
        // printf("%s\n", decryptstr);

    }

    // vector<vector<int> > v { { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24},
    //                        { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24} };
    // cartesian(v);
   
    return 0;
}