package com.baekjun.demo.인프런.HashMapTreeSet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 아나그램 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String answer = "YES";
        char[] first = br.readLine().toCharArray();
        Arrays.sort(first);

        char[] second = br.readLine().toCharArray();
        Arrays.sort(second);

        for (int i = 0; i < first.length; i++) {
            if (first[i] != second[i]) {
                answer = "NO";
            }
        }

        System.out.println(answer);
    }
}
