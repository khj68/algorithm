import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class Main {
  private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames, int[] numOfMovesPerGame){
    Set<Character> quickSet = new HashSet<>();
    int[] counter = new int[26];
    char[] players = new char[numOfAllPlayers-1];

    counter[0] += 1;
    char cur = 'A';

    for (char quickPlayer : namesOfQuickPlayers) {
        quickSet.add(quickPlayer);
    }
    for(int i=0; i<players.length; i++) {
        players[i] = (char)((int)'A' + i+1);
    }

    int idx = 0;
    for (int move : numOfMovesPerGame) {
        while (move > 0) {
            idx++;
            move--;

            if (idx == players.length) idx = 0;
        }
        while (move < 0) {
            idx--;
            move++;

            if (idx == -1) idx = players.length-1;
        }

        if (idx >= players.length) idx %= players.length;
        if (quickSet.contains(players[idx])) {
            counter[cur - (int)'A']++;
        } else {
            char tmp = cur;
            cur = players[idx];
            players[idx] = tmp;
            counter[cur - (int)'A']++;
        }
    }

    for (int i=0; i<players.length; i++) {
        System.out.println(String.format("%c %d", players[i], counter[players[i]-(int)'A']));
    }
    System.out.println(String.format("%c %d", cur, counter[cur-(int)'A']));

  }

  private static class InputData {
    int numOfAllPlayers;
    int numOfQuickPlayers;
    char[] namesOfQuickPlayers;
    int numOfGames;
    int[] numOfMovesPerGame;
  }

  private static InputData processStdin() {
    InputData inputData = new InputData();

    try (Scanner scanner = new Scanner(System.in)) {
      inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

      inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
      System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0, inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

      inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
      inputData.numOfMovesPerGame = new int[inputData.numOfGames];
      String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
      for(int i = 0; i < inputData.numOfGames ; i++){
        inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
      }
    } catch (Exception e) {
      throw e;
    }

    return inputData;
  }

  public static void main(String[] args) throws Exception {
    InputData inputData = processStdin();

    solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  }
}