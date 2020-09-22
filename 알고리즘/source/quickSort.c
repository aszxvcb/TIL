///*
// quick sort
// */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void quickSort(float A[], int p, int r);
int partition(float A[], int p, int r);
float float_rand(float min, float max);
void swap(float* a, float* b);

int cnt = 0;

int main(void){
    clock_t start, end;
    int n = 20000;


    //   3.(b)
    float init_arr[20000];
    int seed = 20152408;
    srand(seed);    // rand 함수의 seed값 설정
    for( int i=0; i<8; i++){
        init_arr[i] = float_rand(-1, 1);
    }

    //  3.(a)
//    int init_arr[8] = {12,70,30,20,55,25,40,50};
//    int init_arr[8] = {8,1,7,2,6,3,4,5};

    printf("3.(c) 퀵정렬\n");
    //   3.(a,b)
//    printf("초기 배열 : ");
//    for(int i=0; i<8; i++){
////        printf("%d ",init_arr[i]);
//        printf("%.3f ",init_arr[i]);
//    }
//    printf("\n");
//    quickSort(init_arr, 0, n-1);
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
        quickSort(init_arr, 0, n-1);
        end = clock();
        printf("%d개 정렬 소요시간(msec) : %.0lf msec\n", n, ((double)end-start)/1000); // 맥 환경에서의 msec 계산
    }
}

/*
 최소값을 찾아 맨뒤로 보내는 내림차순 병합정렬
 */
void quickSort(float A[], int p, int r){
    int cnt = 0;
    int q;
    if( p <= r ){
        q = partition(A, p, r); //  분할
        if ( q<0 ) return;
        quickSort(A, p, q-1); //  왼쪽 부분 배열 정렬
        quickSort(A, q+1, r); //  오른쪽 부분 배열 정렬
    }


////     3.(a)
//    if( cnt < 5 ){
//        printf("%d번째 정렬 : ", cnt+1);
//        for(int i=0; i<8; i++){
//            printf("%d ",A[i]);
////            printf("%.3f ",A[i]);
//        }
//        printf("\n");
//        cnt++;
//    }
}

int partition(float A[], int p, int r){
    // 내림차순
    // 피봇을 기준으로 왼쪽은 큰 값, 오른쪽은 작은 값으로 정렬
        
    int pibot = r; // pibot 설정
    int i=p, j=r-1;
    
    while(i <= j){ // 엇갈릴 떄 까지 반복
        while( i < r ){            // 왼쪽에서부터 탐색 시작
            if( A[i] >= A[pibot] ){ // 피봇보다 작은 값을 찾는다.
                i++;
            }
            else
                break;
        }
        while( j > p ){            // 오른쪽에서부터 탐색 시작
            if( A[j] < A[pibot] ){ // 피봇보다 큰 값을 찾는다.
                j--;
            }
            else
                break;
        }
        
        // 좌측에서 큰 값과 우측에서 작은 값을 찾은 상태
        if( i >= j ){    // 엇갈린 상태라면
            swap( &A[i] , &A[pibot] ); // 작은값과 피봇을 swap하여 작은값이 오른쪽으로 가게끔한다.
            
//            for(int i=0; i<8; i++){
//                printf("%d ", A[i]);
//            }
//            printf("\n");
//
            return i;
        }
        else {  // 엇갈리지 않은 상태라면 작은값과 큰값의 위치를 변경한다.
            swap( &A[i], &A[j] );
            
//            for(int i=0; i<8; i++){
//                   printf("%d ", A[i]);
//               }
//               printf("\n");
        }
    }

    

//    if( cnt < 5){
//        printf("%d번째 정렬 : ", cnt+1);
//        cnt++;
//        for(int l=0; l<8; l++){
////            printf("%d ", A[l]);
//            printf("%.3f ", A[l]);
//        }
//        printf("\n");
//    }
    return -1;
}

// float random값 생성
float float_rand( float min, float max )
{
    float scale = rand() / (float) RAND_MAX; /* [0, 1.0] */
    return min + scale * ( max - min );      /* [min, max] */
}

void swap(float* a, float* b){
    float temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
