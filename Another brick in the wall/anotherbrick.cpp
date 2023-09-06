#include <bits/stdc++.h>
using namespace std;

int main(){
    // #ifndef TESTING
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    // #endif

    int h, w, n;
    cin >> h >> w >> n;
    bool good = true;
    int heightCount = 0;
    int wCount = 0;
    while(n--){
        int brick;
        cin >> brick;
        wCount += brick;
        if(wCount == w){
            heightCount++;
            wCount = 0;
            if(heightCount == h){
                goto end;
            }
        } else if(wCount > w){
            good = false;
            goto end;
        }
    }

    end:
    if(good && heightCount == h){
        cout << "YES";
    } else {
        cout << "NO";
    }

    return 0;   
}
