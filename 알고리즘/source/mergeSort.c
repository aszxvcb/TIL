///*
// merge sort
// */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void mergeSort(float A[], int p, int r);
void merge(float A[], int p, int q, int r);
float float_rand(float min, float max);

float sorted[20000];
int cnt = 0;

int main(void){
    clock_t start, end;
    int n = 8;


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

    printf("3.(c) 병합정렬\n");
    //   3.(a,b)
//    printf("초기 배열 : ");
//    for(int i=0; i<8; i++){
////        printf("%d ",init_arr[i]);
//        printf("%.3f ",init_arr[i]);
//    }
//    printf("\n");
//    mergeSort(init_arr, 0, n-1);
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
        mergeSort(init_arr, 0, n-1);
        end = clock();
        printf("%d개 정렬 소요시간(msec) : %.0lf msec\n", n, ((double)end-start)/1000); // 맥 환경에서의 msec 계산
    }
}

/*
 최소값을 찾아 맨뒤로 보내는 내림차순 병합정렬
 */
void mergeSort(float A[], int p, int r){
    int cnt = 0;
    int q;
    if( p < r ){
        q = floor((p+r)/2); //  절반씩 분할하여
        mergeSort(A, p, q); //  각각을 정렬
        mergeSort(A, q+1, r);
        merge(A, p, q, r);  //  정렬된 배열을 병합
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

void merge(float A[], int p, int q, int r){
    int i = p;
    int j = q+1;
    int k = p;

    // 분리되어있는 두 배열을 합칩
    while(i<=q && j<=r){  // 두 배열 중 큰 원소부터 정렬배열에 삽입
        if(A[i] >= A[j]){
            sorted[k] = A[i];
            i++;
        }
        else{
            sorted[k] = A[j];
            j++;
        }
        k++;
    }

    // 나머지 원소들을 정렬배열에 추가
    if( i<=q ){
        for( int l=i; l<=q; l++){
            sorted[k] = A[l];
            k++;
        }
    }
    else{
        for( int l=j; l<=r; l++){
            sorted[k] = A[l];
            k++;
        }
    }

    // 정렬된 배열 원소 복사
    for (int l=0; l<=r; l++){
        A[l] = sorted[l];
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
}

// float random값 생성
float float_rand( float min, float max )
{
    float scale = rand() / (float) RAND_MAX; /* [0, 1.0] */
    return min + scale * ( max - min );      /* [min, max] */
}

