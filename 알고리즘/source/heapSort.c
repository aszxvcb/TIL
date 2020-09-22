///*
// heap sort
// */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void heapSort(float A[], int n);
float float_rand(float min, float max);
void swap(float* a, float* b);
void buildHeap(float A[], int n);
void heapify(float A[], int p, int q);

int cnt = 0;

int main(void){
    clock_t start, end;
    int n = 8;


//       3.(b)
    float init_arr[20000];
//    int seed = 20152408;
//    srand(seed);    // rand 함수의 seed값 설정
//    for( int i=0; i<8; i++){
//        init_arr[i] = float_rand(-1, 1);
//    }

    //  3.(a)
//    int init_arr[8] = {12,70,30,20,55,25,40,50};
//    int init_arr[8] = {8,1,7,2,6,3,4,5};

    printf("3.(c) 힙정렬\n");
//       3.(a,b)
//    printf("초기 배열 : ");
//    for(int i=0; i<8; i++){
////        printf("%d ",init_arr[i]);
//        printf("%.3f ",init_arr[i]);
//    }
//    printf("\n");
//    heapSort(init_arr, n-1);
//    printf("정렬 후 배열 : ");
//        for(int i=0; i<8; i++){
////            printf("%d ",init_arr[i]);
//            printf("%.3f ",init_arr[i]);
//        }
//        printf("\n");

    // 3.(c)
    for( int n=1000; n<=20000; n+=1000 ){
        for( int i=0; i<n; i++){
            init_arr[i] = float_rand(-1, 1); // 난수 생성
        }
        start = clock();    // 시간 측정
        heapSort(init_arr, n-1);
        end = clock();
        printf("%d개 정렬 소요시간(msec) : %.0lf msec\n", n, ((double)end-start)/1000); // 맥 환경에서의 msec 계산
    }
}

/*
 최소값을 찾아 맨뒤로 보내는 내림차순 힙정렬
 */
void heapSort(float A[], int n){
    
    buildHeap(A, n);    // 주어진 배열을 이용하여 힙을 생성
//    printf("정렬 후 힙 : ");
//    for(int i=0; i<8; i++){
////        printf("%d ",A[i]);
//            printf("%.3f ", A[i]);
//    }
//    printf("\n");
    
    for(int i=n; i>0; i--){
        swap(&A[0] , &A[i]);    // 첫 요소와 끝 요소를 스왑한다.
                                // 첫 요소는 정렬이 보장되어 있기 때문
        
        //     3.(a)
//            if( cnt < 5 ){
//                printf("%d번째 정렬(swap) : ", cnt+1);
//                for(int i=0; i<8; i++){
////                    printf("%d ",A[i]);
//                    printf("%.3f ",A[i]);
//                }
//                printf("\n");
//                cnt++;
//            }
        
        heapify(A, 0, i-1); // 스왑된 배열이 힙의 특성을 만족하도록 한다.
    }
}

void buildHeap(float A[], int n){
    // 최소힙 - 부모노드가 작은 것
    for(int i=1; i<=n; i++){
        int c = i;
        do{
            int root = (c-1) / 2; // 현재 노드의 루트(부모) 인덱스 계산
            if(A[root] > A[c]){   // 부모노드가 크다면, 자식노드와 스왑한다.
                swap( &A[root], &A[c] ); // 작은 노드가 위로 올라올 수 있도록
            }
            c = root;
        } while(c != 0);
    }
}

void heapify(float A[], int p, int q){
    int root = 0;
    int c = 1;
    do {
        c=2 * root + 1;
        // 좌,우 자식 중 더 작은 값을 찾기
        if(c < q && A[c] > A[c+1]){
            c++;
        }
        // 루트보다 자식이 크다면 교환
        if( c < q && A[root] > A[c]){
            swap(&A[root], &A[c]);
        }
        root = c;
        
//        for( int i=0; i<8; i++){
//            printf("%d ", A[i]);
//        }
//        printf("\n");
    }while(c<q);
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
