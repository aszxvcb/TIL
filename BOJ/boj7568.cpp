// boj7569

#include <stdio.h> 

int main(void){

	int num;
	int kg[50] = {0,};
	int cm[50] = {0,};
	int rank = 1;

	scanf("%d", &num);
	for( int i = 0; i<num; i++ ){
		scanf("%d %d", &kg[i], &cm[i]);
	}

	// for( int i = 0; i<num; i++ ){
	// 	printf("%d %d\n", kg[i], cm[i]);
	// }	

	// 계산부
	for( int i = 0; i<num; i++ ){
		rank = 1;
		for( int j = 0; j<num; j++){
			// 몸무게와 키 둘다 큰 사람이 있으면 rank+1
			if( kg[i] < kg[j] && cm[i] < cm[j] ){
				rank++;
			}
		}
		printf("%d ", rank);
	}


	
	return 0;
}