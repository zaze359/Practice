class Solution {
    public static void main(String[] args) {
        int[] intArray = new int[] { 4, 5, 6, 7, 0, 1, 2 };
        int target = 1;
        intArray = new int[] { 1 };
        target = 1;
        // intArray = new int[] { 4, 5, 6, 7, 8, 1, 2, 3 };
        // target = 5;
        // intArray = new int[] { 5, 1, 2, 3, 4 }; // 1
        // target = 1;
        // intArray = new int[] { 3, 1 }; // 1
        // target = 1;
        // intArray = new int[] { 8, 9, 2, 3, 4 }; // 9
        // target = 9;
        // intArray = new int[] { 9, 8 }; // 8
        // target = 8;
        // mid < a1
        int index = new Solution().search(intArray, target);
        System.out.println("index: " + index);
    }

    public int search(int[] nums, int target) {
        int n = nums.length;
        if (n == 0) {
            return -1;
        }
        int low = 0;
        int high = n - 1;
        //
        int left;
        int right;
        while (low <= high) {
            // 获取左右边的值，来判断新区间中的数据是否有序
            left = nums[low];
            right = nums[high];
            // 相同直接返回
            // if (left == target) {
            // return low;
            // }
            // 获取中间值
            int mid = (low + high) >> 1;
            int midValue = nums[mid];
            System.out.println(" mid: " + mid + "; midValue: " + midValue);
            // 相同直接返回
            if (midValue == target) {
                return mid;
            }
            // 查找的值小于中间值场景,
            if (target < midValue) {
                if (target >= left) { // 往回找
                    // 查找的值 在 [left, mid] 区间内
                    high = mid - 1;
                } else { // 需要往后找
                    // 值在[mid, right] 区间内
                    low = mid + 1;
                }
                continue;
            }
            // 查找的值大于中间值场景
            if (left < midValue || target <= right) {
                // 直接跳到 mid之后
                // 1. left -> mid 是有序的,
                // 2. 查找的值小于等于最右边的数，
                low = mid + 1;
            } else { // 查找的大于最后一个值，此时需要往回找
                high = mid - 1;
            }
        }
        return -1;
    }
}