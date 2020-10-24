import java.util.Scanner;
import java.util.Stack;

class Main {
  private static void solution(int numOfOrder, String[] orderArr) {
    for(String s : orderArr) {
        StringBuilder ans = new StringBuilder();
        Stack<Integer> numStack = new Stack<>();
        Stack<String> strStack = new Stack<>();

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                numStack.push(((int)(c-'0')));
                i++;
                if (s.charAt(i) != '(') {
                    int a = numStack.pop();
                    for (int k=0; k<a; k++) {
                        ans.append(s.charAt(i));
                    }
                } else{
                    strStack.push(ans.toString());
                    ans = new StringBuilder();
                }
            } else if(c == '(') {
                numStack.push(0);
                strStack.push(ans.toString());
                ans = new StringBuilder();
            } else if(c == ')') {
                int num = numStack.pop();

                if (num > 0) {
                    String tmp = ans.toString();
                    StringBuilder tmpBuilder = new StringBuilder(strStack.pop());

                    for (int k=0; k<num; k++) {
                        tmpBuilder.append(tmp);
                    }
                    ans = tmpBuilder;
                } else {
                    String tmpAns = ans.toString();
                    String top = strStack.pop();
                    StringBuilder tmpBuilder = new StringBuilder();

                    for (int k=0; k<tmpAns.length(); k++) {
                        tmpBuilder.append(top);
                        tmpBuilder.append(tmpAns.charAt(k));
                    }

                    ans = tmpBuilder;
                }
            } else {
                ans.append(c);
            }
            // System.out.println(ans);
            // System.out.println(numStack.toString());
            // System.out.println(strStack.toString());
        }
        
        
        System.out.println(ans);
    }
  }

  private static class InputData {
    int numOfOrder;
    String[] orderArr;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.numOfOrder = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

      inputData.orderArr = new String[inputData.numOfOrder];
      for (int i = 0; i < inputData.numOfOrder; i++) {
        inputData.orderArr[i] = scanner.nextLine().replaceAll("\\s+", "");
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.numOfOrder, inputData.orderArr);
  }
}

