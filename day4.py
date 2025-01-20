# What is the time, space complexity of following code :

int a = 0, b = 0; 

int i, j, k;
for (i = 0; i < N; i++) { 
    for (j = 0; j < N; j++) { 
        a = a + j; 
    } 
} 
for (k = 0; k < N; k++) { 
    b = b + k; 
}


# ans: Time Complexity: 0(N*N)time, O(1) space
