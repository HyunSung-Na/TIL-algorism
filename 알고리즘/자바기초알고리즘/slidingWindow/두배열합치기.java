package com.baekjun.demo.인프런.slidingWindow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 두배열합치기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] firstArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int M = Integer.parseInt(br.readLine());

        int[] secondArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        ArrayList<Integer> arrayCombine = combinedArrays(firstArray, secondArray, N, M);

        arrayCombine.forEach(it -> System.out.print(it + " "));
    }

    private static ArrayList<Integer> combinedArrays(int[] firstArray, int[] secondArray, int N, int M) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        int lt = 0;
        int rt = 0;

        while (lt < N && rt < M) {
            if (firstArray[lt] < secondArray[rt]) {
                arrayList.add(firstArray[lt]);
                lt++;
            } else {
                arrayList.add(secondArray[rt]);
                rt++;
            }
        }

        while (lt < N) arrayList.add(firstArray[lt++]);

        while (rt < M) arrayList.add(secondArray[rt++]);

        return arrayList;
    }
}
