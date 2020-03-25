#include <stdio.h>

int main()
{
	int N = 0, change=0,  changeCount = 0, tmp = 0;
	
	scanf("%d %d",&N, &change);
	
	int changeList[N] = {0, };
	
	for(int i=0;i<sizeof(changeList)/sizeof(int);i++){
		
		scanf("%d",&tmp);
		if(tmp > change){
			N -= 1;
		}
		else{
			changeList[i] = tmp;
		}
	}
	
	for(int i=N-1;i>-1;i--){
		tmp = change / changeList[i];
		changeCount += tmp;
		change -= changeList[i] * tmp;
	}
	
	printf("%d", changeCount);
	
};
