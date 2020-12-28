package me.joohyun.tutorial;

import java.util.Arrays;

/**
 * url : https://leetcode.com/problems/median-of-two-sorted-arrays/
 */

public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] concat = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, concat, 0, nums1.length);
        System.arraycopy(nums2, 0, concat, nums1.length, nums2.length);

        Arrays.sort(concat);

        if(concat.length % 2 == 0){
            int idx = concat.length / 2 - 1;
            return (double)(concat[idx] + concat[idx + 1]) / 2;
        }else{
            return concat[concat.length / 2];
        }
    }
}
