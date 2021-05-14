package com.baekjun.demo.인프런.HashMapTreeSet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class 학급회장 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        char[] votes = br.readLine().toCharArray();

        HashMap<Character, Integer> count = new HashMap<>();

        for (char person : votes) {
            count.put(person, count.getOrDefault(person, 0) + 1);
        }

        char answer = '0';
        int maxValue = 0;

        for (char person : votes) {
            Integer result = count.get(person);
            if (result > maxValue) {
                answer = person;
                maxValue = result;
            }
        }

        System.out.println(answer);
    }
}
