import java.util.Scanner;

class Main {

  private static void printArr(int[] arr) {
      for(int a : arr) {
          System.out.print(a);
          System.out.print(' ');
      }
      System.out.println();
  }
    
  private static void solution(int day, int width, int[][] blocks) {
      int siment = 0;
      int[] arr = new int[width];

      for (int[] block : blocks) {
          for (int i=0; i<width; i++) {
              arr[i] += block[i];
          }

          int leftMax = arr[0];
          int rightMax = 0;
          int tmp = 0;

          for (int i=1; i<width-1; i++) {
              rightMax = 0;

              if (arr[i] >= leftMax) {
                  leftMax = arr[i];
                  continue;
              }

              for (int j=i+1; j<width; j++) {
                if (arr[j] >= leftMax) {
                    rightMax = arr[j];
                    break;
                }

                rightMax = Math.max(rightMax, arr[j]);
              }
              tmp = Math.min(leftMax, rightMax) - arr[i];
              siment += tmp;
              arr[i] += tmp;

              leftMax = arr[i];

            }
            
      }

      System.out.println(siment);

  }
  
  private static class InputData {
    int day;
    int width;
    int[][] blocks;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.day = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));      
      inputData.width = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      
      inputData.blocks = new int[inputData.day][inputData.width];
      for (int i = 0; i < inputData.day; i++) {
        String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
        for (int j = 0; j < inputData.width; j++) {
          inputData.blocks[i][j] = Integer.parseInt(buf[j]);
        }
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.day, inputData.width, inputData.blocks);
  }
}