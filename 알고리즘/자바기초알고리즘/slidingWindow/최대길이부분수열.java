package com.baekjun.demo.인프런.slidingWindow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 최대길이부분수열 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] array = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int answer = solution(inputs[0], inputs[1], array);

        System.out.println(answer);
    }

    private static int solution(int N, int K, int[] array) {
        int answer = 0;
        int cnt = 0;
        int lt = 0;

        for (int rt = 0; rt < N; rt++) {
            if (array[rt] == 0) cnt++;
            while (cnt > K) {
                if (array[lt] == 0) cnt--;
                lt++;
            }
            answer = Math.max(answer, rt - lt + 1);
        }

        return answer;
    }
}
