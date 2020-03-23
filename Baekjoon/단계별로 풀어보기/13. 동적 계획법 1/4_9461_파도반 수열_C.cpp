#include <stdio.h>

long long respo[101] = {0, };


long long wave(int N)
{
	if(respo[N] == 0)
	{
		respo[N] = wave(N-2) + wave(N-3);
	}
	return respo[N];
}

int main()
{
	respo[0] = 1;
	respo[1] = 1;
	respo[2] = 1;
	
	int num = 0;
	int num2 = 0;
	
	scanf("%d",&num);
	
	for(int i=0;i<num;i++){
			
		scanf("%d",&num2);
		printf("%lld\n", wave(num2-1));
	}
	
}


