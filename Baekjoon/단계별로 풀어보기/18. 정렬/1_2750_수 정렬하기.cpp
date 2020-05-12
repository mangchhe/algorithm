#include <stdio.h>

void selectSort(int *arr, int n){
	
	for(int i=0;i<n-1;i++){
		
		int min = arr[i];
		int idx = i;
		
		for(int j=i;j<n;j++){
			
			if(min > arr[j]){
				idx = j;
				min = arr[j];
			}
		}
		
		int tmp = arr[i];
		arr[i] = min;
		arr[idx] = tmp;
	}
	
}

int main(){
	
	int N;
	
	scanf("%d", &N);
	
	int NList[N];
	
	for(int i=0;i<N;i++){
		
		scanf("%d", &NList[i]);
	}
	
	selectSort(NList, N);
	
	for(int i=0;i<N;i++){
		
		printf("%d\n", NList[i]);
	}
	
	return 0;
}
