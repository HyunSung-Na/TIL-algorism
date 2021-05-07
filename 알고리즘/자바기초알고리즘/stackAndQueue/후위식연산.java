package com.baekjun.demo.인프런.stackAndQueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 후위식연산 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] inputs = br.readLine().toCharArray();
        Stack<Integer> stack = new Stack<>();

        for (char s : inputs) {
            if (checkOperator(s)) {
                int p2 = stack.pop();
                int p1 = stack.pop();
                int result = calculator(p1, p2, s);
                stack.push(result);
            } else {
                stack.push(s - '0');
            }
        }

        int answer = stack.pop();

        System.out.println(answer);
    }

    private static int calculator(int p1, int p2, char s) {
        if (s == '+')
            return p1 + p2;

        if (s == '-')
            return p1 - p2;

        if (s == '*')
            return p1 * p2;

        if (s == '/')
            return p1 / p2;

        return 0;
    }

    private static boolean checkOperator(char s) {
        if (s == '+')
            return true;
        if (s == '-')
            return true;

        if (s == '*')
            return true;

        if (s == '/')
            return true;


        return false;
    }
}
