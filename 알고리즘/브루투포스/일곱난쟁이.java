package com.baekjun.demo.브루트포스;

import java.util.Arrays;
import java.util.Scanner;

public class 일곱난쟁이 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 9;
        int[] arr = new int[n];
        int sum = 0;

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i];
        }

        Arrays.sort(arr);

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (sum - arr[i] - arr[j] == 100) {
                    for (int k = 0; k < n; k++) {
                        if (i == k || j == k) {
                            continue;
                        }
                        System.out.println(arr[k]);
                    }
                    System.exit(0);
                }
            }
        }
    }

}
