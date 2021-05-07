package com.baekjun.demo.인프런.stackAndQueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 올바른괄호 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] inputs = br.readLine().toCharArray();
        Stack<Character> stack = new Stack<>();

        for (char s : inputs) {
            if (s == '(') {
                stack.push(s);
            } else {
                if (!stack.empty())
                    stack.pop();
                else {
                    System.out.println("NO");
                    System.exit(0);
                }
            }
        }

        if (!stack.empty()) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }
}
