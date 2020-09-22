/*
 bubble sort
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(float A[], int n);
void swap(float* a, float* b);
float float_rand(float min, float max);

int main(void){
    clock_t start, end;
    int n = 8;


    //   3.(b)
    float init_arr[20000];
//    int seed = 20152408;
//    srand(seed);    // rand 함수의 seed값 설정
//    for( int i=0; i<8; i++){
//        init_arr[i] = float_rand(-1, 1);
//    }

//    int init_arr[8] = {12,70,30,20,55,25,40,50};
//    int init_arr[8] = {10,9,8,7,6,5,4,3};

    printf("3.(c) 버블정렬\n");
    //   3.(a,b)
//    printf("초기 배열 : ");
//    for(int i=0; i<8; i++){
////        printf("%d ",init_arr[i]);
//        printf("%.3f ",init_arr[i]);
//    }
//    printf("\n");
//    bubbleSort(init_arr, n);
//    printf("정렬 후 배열 : ");
//        for(int i=0; i<8; i++){
////            printf("%d ",init_arr[i]);
//            printf("%.3f ",init_arr[i]);
//        }
//        printf("\n");

    // 3.(c)
    for( int n=1000; n<=20000; n+=1000 ){
        for( int i=0; i<n; i++){
            init_arr[i] = float_rand(-1, 1);
        }
        start = clock();
        bubbleSort(init_arr, n);
        end = clock();
        printf("%d개 정렬 소요시간(msec) : %.1lf msec\n", n, ((double)end-start)/1000);
    }
}

/*
 최소값을 찾아 맨뒤로 보내는 내림차순 버블정렬
 */
void bubbleSort(float A[], int n){
    int last=0;
    int cnt = 0;
    for( last=n; last>0; last-- ){  // 정렬된 값이 위치할 last 설정
        for( int j=0; j<last-1; j++ ){    // 이웃하는 원소를 비교한다.
            if( A[j] < A[j+1] ) {       // 작은 원소가 왼쪽에 있다면,
                swap(&A[j], &A[j+1]);    //   A[j]와 A[j+1]의 값을 교환
//                for(int i=0; i<8; i++){
//                    printf("%d ",A[i]);
//                }
//                printf("\n");
            }
        }
        // 3.(a)
//        if( cnt < 5 ){
//            printf("%d번째 정렬 : ", cnt+1);
//            for(int i=0; i<8; i++){
////                printf("%d ",A[i]);
//                printf("%.3f ",A[i]);
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

