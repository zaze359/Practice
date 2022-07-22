class Solution {
    public static void main(String[] args) {
        int[] intArray = new int[] { 0, 1, 0, 3, 12 };
        new Solution().moveZeroes(intArray);
    }

    public void moveZeroes(int[] nums) {
        int size = nums.length;
        int position = 0;
        for (int num : nums) {
            if (num == 0) {
                // ignore
            } else {
                nums[position] = num;
                position++;
            }
        }

        while (position < size) {
            nums[position] = 0;
            position++;
        }
        for (int i : nums) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}