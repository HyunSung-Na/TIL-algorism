package com.baekjun.demo.인프런.stackAndQueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 괄호문자제거 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] chars = br.readLine().toCharArray();
        Stack<Character> stack = new Stack<>();
        StringBuilder builder = new StringBuilder();

        for (char c : chars) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                stack.pop();
            } else {
                if (stack.isEmpty()) {
                    builder.append(c);
                }
            }
        }

        System.out.println(builder);
    }
}
