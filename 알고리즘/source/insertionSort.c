///*
// insertion sort
// */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertionSort(float A[], int n);
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

    //  3.(a)
//    int init_arr[8] = {12,70,30,20,55,25,40,50};
//    int init_arr[8] = {8,1,7,2,6,3,4,5};

    printf("3.(c) 삽입정렬\n");
    //   3.(a,b)
//    printf("초기 배열 : ");
//    for(int i=0; i<8; i++){
////        printf("%d ",init_arr[i]);
//        printf("%.3f ",init_arr[i]);
//    }
//    printf("\n");
//    insertionSort(init_arr, n);
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
        insertionSort(init_arr, n);
        end = clock();
        printf("%d개 정렬 소요시간(msec) : %.3lf msec\n", n, ((double)end-start)/1000);
    }
}

/*
 최소값을 찾아 맨뒤로 보내는 내림차순 삽입정렬
 */
void insertionSort(float A[], int n){
    int i=0;
    int cnt = 0;
    float key;
    for( i=1; i<n; i++ ){
        key = A[i];     // 삽입하고자 하는 값 저장
        for( int j=i; j>=0; j-- ){    // i부터 시작해서 뒤에서 앞으로 탐색
            if(A[j]<key){             // 삽입하고자 하는 값이 비교대상보다 크다면,
                A[j+1] = A[j];        // 뒤로 한칸 이동
                A[j] = key;           // 키 삽입
//                for(int i=0; i<8; i++){
//                    printf("%d ",A[i]);
//    //                printf("%.3f ",A[i]);
//                }
//                printf("\n");
            }
        }
//         3.(a)
//        if( cnt < 5 ){
//            printf("%d번째 정렬 : ", cnt+1);
//            for(int i=0; i<8; i++){
//                printf("%d ",A[i]);
////                printf("%.3f ",A[i]);
//            }
//            printf("\n");
//            cnt++;
//        }
    }


}


// float random값 생성
float float_rand( float min, float max )
{
    float scale = rand() / (float) RAND_MAX; /* [0, 1.0] */
    return min + scale * ( max - min );      /* [min, max] */
}

