
void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int q = 0;
    for (int i = m ; i < m + n; i++) {
        nums1[i] = nums2[q];
        q += 1;
    }

     for (int i = 0; i < nums1Size; i++) {
        for (int q = 0; q < nums1Size; q++) {
            if (nums1[q] > nums1[i]) {
                int aux = nums1[q];
                nums1[q] = nums1[i];
                nums1[i] = aux;
            }
        }
    }
}
