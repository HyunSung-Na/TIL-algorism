package com.baekjun.demo.인프런.stackAndQueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 쇠막대기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();

        System.out.println(solution(input));
    }

    private static int solution(String input) {
        int answer = 0;
        Stack<Character> stack = new Stack<>();
        char[] array = input.toCharArray();

        for (int i = 0; i < array.length; i++) {
            if (array[i] == '(') {
                stack.push(array[i]);
            } else {
                if (array[i - 1] == '(') {
                    stack.pop();
                    answer += stack.size();
                } else {
                    stack.pop();
                    answer += 1;
                }
            }
        }

        return answer;
    }
}
