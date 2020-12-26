// boj2231

#include <stdio.h>

int main(void){
	 int input = 0; // 입력 받은 값
	 int size = 0; // 자릿수를 구하기 위한 변수
	 int sum = 0 ;
	 int part = 0;
	 
	 scanf("%d", &input);

	 for( int i=0; i <= input; i++ ){ // 0~input까지 모든 경우 확인
	 	sum = 0;	// 반복문 시작마다 초기화
	 	// printf("--- i = %d ---\n", i);
	 	part = i;
	 	while( part != 0 ){
	 		size++;
	 		sum += part % 10;	// 자리수를 구하면서 합을 계산
	 		part = part / 10;	
	 		// printf("%d->", sum);
	 	}
	 	// printf("i\n");
	 	sum += i;
	 	// printf("=>%d\n", sum);

	 	if( input == sum ){	// 합이 input과 같다면 결과 출력
	 		// printf("check : %d\n", i);
	 		printf("%d", i);
	 		return 0;
	 	}
	 }
	 printf("0");
	 return 0;
}