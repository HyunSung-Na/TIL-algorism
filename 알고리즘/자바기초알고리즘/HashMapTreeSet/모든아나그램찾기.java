package com.baekjun.demo.인프런.HashMapTreeSet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class 모든아나그램찾기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] array = br.readLine().toCharArray();
        char[] matchString = br.readLine().toCharArray();

        int answer = solution(array, matchString);
        System.out.println(answer);
    }

    private static int solution(char[] array, char[] matchString) {
        int answer = 0;

        HashMap<Character, Integer> map = new HashMap<>();
        HashMap<Character, Integer> compare = new HashMap<>();

        for (char c : matchString) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        int L = matchString.length - 1;

        for (int i = 0; i < L; i++) {
            compare.put(array[i], compare.getOrDefault(array[i], 0) + 1);
        }

        int lt = 0;

        for (int rt = L; rt < array.length; rt++) {
            compare.put(array[rt], compare.getOrDefault(array[rt], 0) + 1);
            if (compare.equals(map)) answer++;

            if (compare.get(array[lt]) != 1) {
                compare.put(array[lt], compare.get(array[lt]) - 1);
            } else {
                compare.remove(array[lt]);
            }
            lt++;
        }

        return answer;
    }
}
