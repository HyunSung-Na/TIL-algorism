package com.baekjun.demo.인프런.HashMapTreeSet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class 매출액의종류 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int N = input[0];
        int K = input[1];

        int[] array = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        ArrayList<Integer> result = solution(N, K, array);

        result.forEach(it -> System.out.print(it + " "));
    }

    private static ArrayList<Integer> solution(int n, int k, int[] array) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        int rt = k - 1;

        for (int i = 0; i < rt + 1; i++) {
            hashMap.put(array[i], hashMap.getOrDefault(array[i], 0) + 1);
        }

        arrayList.add(hashMap.keySet().size());

        for (int lt = 1; lt < n - k + 1; lt++) {
            if (hashMap.get(array[lt - 1]) > 1) {
                hashMap.put(array[lt - 1], hashMap.get(array[lt - 1]) - 1);
            } else if (hashMap.get(array[lt - 1]) == 1) {
                hashMap.remove(array[lt - 1]);
            }

            rt++;
            hashMap.put(array[rt], hashMap.getOrDefault(array[rt], 0) + 1);
            arrayList.add(hashMap.keySet().size());
        }

        return arrayList;
    }
}
