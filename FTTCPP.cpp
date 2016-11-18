#include <bits/stdc++.h>

using namespace std;

//typedef complex<double> base;

// this is the recursive FFT
/*void fft(vector<base> & a, bool invert) {
	int n = (int) a.size();
	if (n == 1)
		return;
	vector<base> a0(n / 2), a1(n / 2);
	for (int i = 0, j = 0; i < n; i += 2, j++) {
		a0[j] = a[i];
		a1[j] = a[i + 1];
	}
	fft(a0, invert);
	fft(a1, invert);
	double ang = 2 * M_PI / n * (invert ? -1 : 1);
	base w(1), wn(cos(ang), sin(ang));
	for (int i = 0; i < n / 2; i++) {
		a[i] =  a0[i] + w * a1[i];
		a[i + n / 2] =  a0[i] - w * a1[i];
		if (invert)
			a[i] /= 2, a[i + n / 2] /= 2;
		w *= wn;
	}
}*/


// This is the first optimisation with reversing the bits.
/*int rev(int num, int lg_n) {
	int res = 0;
	for (int i = 0; i < lg_n; i++)
		if (num & (1 << i))
			res |= 1 << (lg_n - 1 - i);
	return res;
}

void fft(vector<base> & a, bool invert) {
	int n = (int) a.size();
	int lg_n = 0;
	while ((1 << lg_n) < n)
		++lg_n;
	for (int i = 0; i < n; i++) {
		int j = rev(i, lg_n);
		if (i < j)
			swap(a[i], a[j]);
	}
	for (int len = 2; len <= n; len <<= 1) {
		double ang = 2 * M_PI / len * (invert ? -1 : 1);
		base wlen(cos(ang), sin(ang));
		for (int i = 0; i < n; i += len) {
			base w(1);
			for (int j = 0; j < len / 2; j++) {
				base u = a[i + j], v = a[i + j + len / 2] * w;
				a[i + j] = u + v;
				a[i + j + len / 2] = u - v;
				w *= wlen;
			}
		}
	}
	if (invert)
		for (int i = 0; i < n; i++)
			a[i] /= n;
}*/

// The second optimisation with the reversing trick.
/*void fft(vector<base> & a, bool invert) {
	int n = (int) a.size();
	for (int i = 1, j = 0; i < n; i++) {
		int bit = n >> 1;
		for (; j >= bit; bit >>= 1)
			j -= bit;
		j += bit;
		if (i < j)
			swap(a[i], a[j]);
	}
	for (int len = 2; len <= n; len <<= 1) {
		double ang = 2 * M_PI / len * (invert ? -1 : 1);
		base wlen(cos(ang), sin(ang));
		for (int i = 0; i < n; i += len) {
			base w(1);
			for (int j = 0; j < len / 2; j++) {
				base u = a[i + j], v = a[i + j + len / 2] * w;
				a[i + j] = u + v;
				a[i + j + len / 2] = u - v;
				w *= wlen;
			}
		}
	}
	if (invert)
		for (int i = 0; i < n; i++)
			a[i] /= n;
}*/

long long mod = 12289;
long long root = 3;
long long root_1 = 8193;
long long root_pw = 512;
long long sqrtOfPrimitiveRoot = 1321;

/* This function calculates (a^b)%MOD */
long long pow(long long a, long long b, long long MOD) {
	long long x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
            if(x>MOD) x%=MOD;
        }
        y = (y*y);
        if(y>MOD) y%=MOD;
        b /= 2;
    }
    return x;
}
 
long long modInverse(long long a, long long m) {
    return pow(a,m-2,m);
}

void ntt(vector<long long> & a, bool invert) {
	int n = (int) a.size();
	for (int i = 1, j = 0; i < n; i++) {
		int bit = n >> 1;
		for (; j >= bit; bit >>= 1)
			j -= bit;
		j += bit;
		if (i < j)
			swap(a[i], a[j]);
	}
	for (int len = 2; len <= n; len <<= 1) {
		int wlen = invert ? root_1 : root;
		for (int i = len; i < root_pw; i <<= 1)
			wlen = (int) (wlen * 1ll * wlen % mod);
		for (int i = 0; i < n; i += len) {
			int w = 1;
			for (int j = 0; j < len / 2; j++) {
				int u = a[i + j], v = (int) (a[i + j + len / 2] * 1ll * w % mod);
				a[i + j] = u + v < mod ? u + v : u + v - mod;
				a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + mod;
				w = (int) (w * 1ll * wlen % mod);
			}
		}
	}
	if (invert) {
		long long nrev = modInverse(n, mod);
		for (int i = 0; i < n; i++)
			a[i] = (int) (a[i] * 1ll * nrev % mod);
	}
}
/*const int mod = 7340033;
const int root = 5;
const int root_1 = 4404020;
const int root_pw = 1<<20;
 
void fft (vector<int> & a, bool invert) {
	int n = (int) a.size();

	for (int i=1, j=0; i<n; ++i) {
		int bit = n >> 1;
		for (; j>=bit; bit>>=1)
			j -= bit;
		j += bit;
		if (i < j)
			swap (a[i], a[j]);
	}

	for (int len=2; len<=n; len<<=1) {
		int wlen = invert ? root_1 : root;
		for (int i=len; i<root_pw; i<<=1)
			wlen = int (wlen * 1ll * wlen % mod);
		for (int i=0; i<n; i+=len) {
			int w = 1;
			for (int j=0; j<len/2; ++j) {
				int u = a[i+j], v = int (a[i+j+len/2] * 1ll * w % mod);
				a[i+j] = u+v < mod ? u+v : u+v-mod;
				a[i+j+len/2] = u-v >= 0 ? u-v : u-v+mod;
				w = int (w * 1ll * wlen % mod);
			}
		}
	}
	if (invert) {
		int nrev = modInverse (n, mod);
		for (int i=0; i<n; ++i)
			a[i] = int (a[i] * 1ll * nrev % mod);
	}
}*/

int nearestPowerOfTwoGreaterThanOrEqual(int x) {
	int n = 1;
	while (n < x)
		n <<= 1;
	return n;
}

/*void multiplyfft(vector<long long> & a, vector<long long> & b, vector<long long> & res) {
	vector<base> fa(a.begin(), a.end()), fb(b.begin(), b.end());
	int n = nearestPowerOfTwoGreaterThanOrEqual(max(a.size(), b.size()));
	n <<= 1;
	fa.resize(n); fb.resize(n);
	fft(fa, false); fft(fb, false);
	for (int i = 0; i < n; i++)
		fa[i] *= fb[i];
	fft(fa, true);
	res.resize(n);
	for (int i = 0; i < n; i++)
		res[i] = (long long) (fa[i].real() + 0.5);
}

void multiplyntt(vector<long long> & a, vector<long long> & b, vector<long long> & res) {
	vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
	int n = nearestPowerOfTwoGreaterThanOrEqual(max(a.size(), b.size()));
	n <<= 1;
	fa.resize(n); fb.resize(n);
	ntt(fa, false); ntt(fb, false);
	for (int i = 0; i < n; i++)
		fa[i] *= fb[i];
	ntt(fa, true);
	res.resize(n);
	for (int i = 0; i < n; i++)
		res[i] = (long long) (fa[i]);
}*/

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0); cin.tie();
	int n, m;
	vector<long long> a, b, res, resntt;
	/*cin >> n;
	for (int i = 0; i < n; i++) {
		long long x; cin >> x;
		a.push_back(x);
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		long long x; cin >> x;
		b.push_back(x);
	}*/
	a.push_back(5);
	a.push_back(2);
	a.push_back(4);
	a.push_back(3);
	n = nearestPowerOfTwoGreaterThanOrEqual(512);
	a.resize(n);
	b.resize(n);
	for (int i = 0; i < a.size(); i++) {
		a[i] *= pow(sqrtOfPrimitiveRoot, i, mod);
		a[i] %= mod;
	}
	/*for (int i = 0; i < b.size(); i++) {
		b[i] *= pow(sqrtOfPrimitiveRoot, i, mod);
		b[i] %= mod;
	}*/
	ntt(a, false);
	cout << "[";
	for (int i = 0; i < a.size(); i++)
		cout << a[i] << ", ";
	cout << "]" << endl;
	/*ntt(b, false);
	cout << "[";
	for (int i = 0; i < b.size(); i++)
		cout << b[i] << ", ";
	cout << "]" << endl;
	res.resize(n);
	for (int i = 0; i < res.size(); i++)
		res[i] = (a[i] * b[i]) % mod;
	cout << "[";
	for (int i = 0; i < res.size(); i++)
		cout << res[i] << ", ";
	cout << "]" << endl;
	ntt(res, true);
	for (int i = 0; i < res.size(); i++) {
		res[i] *= modInverse(pow(sqrtOfPrimitiveRoot, i, mod), mod);
		res[i] %= mod;
	}
	cout << "[";
	for (int i = 0; i < res.size(); i++)
		cout << res[i] << ", ";
	cout << "]" << endl;*/
	return 0;
}