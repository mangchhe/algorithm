#include <stdio.h>

long long solve(long long A, long long B);


int main(){

    long long A, B, C;

    scanf("%lld %lld %lld", &A, &B, &C);

    printf("%lld", solve(B, A) % C);

    return 0;

}

long long solve(long long A, long long B){

    if(A == 0)
        return 1;
    else{
        long long tmp = solve(A / 2, B);

        if(A % 2 == 0){
            return tmp * tmp;
        }
        else
            return tmp * tmp * B;
    }
}