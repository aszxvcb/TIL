// BOJ2798

#include <stdio.h>

int main(void){

	int num = 0;
	int max = 0;
	int input_arr[100] = {0,};
	int sum_val = 0;
	int ret = 0;

	scanf("%d %d", &num, &max);

	for ( int i=0; i<num; i++ ){
		scanf("%d", &input_arr[i]);
	}

	// for ( int i=0; i<num; i++ ){
	// 	printf("%d ", input_arr[i]);
	// }


	// 계산부
	for ( int i=0; i<num; i++ ){
		for( int j=0; j<num; j++){
			for( int k=0; k<num; k++){
				// 같은 카드를 다시 사용하지 않도록 예외처리
				if( input_arr[i] == input_arr[j] || input_arr[i] == input_arr[k] || input_arr[j] == input_arr[k])
					continue;
				sum_val = input_arr[i] + input_arr[j] + input_arr[k];
				// printf("%d\n", sum_val);
				if( sum_val <= max && ret < sum_val ){
					// printf(" check %d %d %d %d %d\n", ret, sum_val, input_arr[i], input_arr[j], input_arr[k]);
					ret = sum_val;
				}
			}
		}
	}

	printf( "%d\n" , ret );

	return 0;

}