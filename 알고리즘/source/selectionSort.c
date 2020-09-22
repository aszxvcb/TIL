/*
 selection sort
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void selectionSort(float A[], float n);
void swap(float* a, float* b);
float float_rand(float min, float max);

int main(void){
    clock_t start, end;
    int n = 8;
    float init_arr[20000];
    int seed = 20152408;
    srand(seed);    // rand 함수의 seed값 설정

//    for( int i=0; i<8; i++){
//        init_arr[i] = float_rand(-1, 1);
//    }

//    int init_arr[8] = {12,70,30,20,55,25,40,50};
//    int init_arr[8] = {10,9,8,7,6,5,4,3};

//    printf("3.(c) 선택정렬\n");
//    printf("초기 배열 : ");
//    for(int i=0; i<8; i++){
//        printf("%.3f ",init_arr[i]);
//    }
//    printf("\n");
//    selectionSort(init_arr, n);
//    printf("정렬 후 배열 : ");
//    for(int i=0; i<8; i++){
//        printf("%.3f ",init_arr[i]);
//    }
//    printf("\n");


    // 3.(c)
    for( int n=1000; n<=20000; n+=1000 ){
        for( int i=0; i<n; i++){
            init_arr[i] = float_rand(-1, 1);    // 난수 생성
        }
        start = clock();    // 시간 측정
        selectionSort(init_arr, n); //   선택정렬
        end = clock();
        printf("%d개 정렬 소요시간(msec) : %.3lf msec\n", n, ((double)end-start)/1000);
    }
}

/*
 최소값을 찾아 맨뒤로 보내는 내림차순 선택정렬
 */
void selectionSort(float A[], float n){
    int last=0;
    int k=0;
    float min=0;
    int cnt = 0;
    for( last=n; last>0; last-- ){  // 정렬된 값이 위치할 last 설정
        min = 999999999;
        for( int j=0; j<last; j++ ){    // A[0...last-1] 중 가장 작은 A[k]를 찾는다.
            if( A[j] < min ) {  //  작은 값이 나타나면 해당 위치를 기억한다.
                min = A[j];
                k = j;
            }
        }
        swap(&A[last-1], &A[k]);    //   A[k]와 A[last-1]의 값을 교환

//        if( cnt < 5 ){
//            printf("%d번째 정렬 : ", cnt+1);
//            for(int i=0; i<8; i++){
//                printf("%d ",A[i]);
//            }
//            printf("\n");
//            cnt++;
//        }
    }
}

void swap(float* a, float* b){
    float temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

// float random값 생성
float float_rand( float min, float max )
{
    float scale = rand() / (float) RAND_MAX; /* [0, 1.0] */
    return min + scale * ( max - min );      /* [min, max] */
}

