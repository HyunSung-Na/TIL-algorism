package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 에라토스테네스체 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int input = Integer.parseInt(br.readLine());

        System.out.println(solution(input));
    }

    private static int solution(int input) {
        int answer = 0;
        int[] ch = new int[input + 1];

        for (int i = 2; i < input; i++) {
            if (ch[i] == 0) {
                answer++;
                for (int j = i; j < input; j= j + i) {
                    ch[j] = 1;
                }
            }
        }

        return answer;
    }
}
