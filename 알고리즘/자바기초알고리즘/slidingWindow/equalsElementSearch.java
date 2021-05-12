package com.baekjun.demo.인프런.slidingWindow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class equalsElementSearch {

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

        Arrays.sort(firstArray);
        Arrays.sort(secondArray);

        ArrayList<Integer> arrayList = equalsElement(N, M, firstArray, secondArray);
        arrayList.forEach(it -> System.out.print(it + " "));
    }

    private static ArrayList<Integer> equalsElement(int n, int m, int[] firstArray, int[] secondArray) {
        ArrayList<Integer> integerArrayList = new ArrayList<>();

        int p1 = 0;
        int p2 = 0;

        while (p1 < n && p2 < m) {
            if (firstArray[p1] == secondArray[p2]) {
                integerArrayList.add(firstArray[p1]);
                p1++;
                p2++;
            } else if (firstArray[p1] < secondArray[p2]) {
                p1++;
            } else {
                p2++;
            }
        }

        return integerArrayList;
    }
}
