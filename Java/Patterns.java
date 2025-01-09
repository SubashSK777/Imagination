public class Patterns {
  public static void Triangle (int n) {
                    for (int i = 0; i <= n; i++){
                      for (int j = 0; j <= i; j++){
                        System.out.print(" * ");
                      } System.out.println();
                    }
  }

  public static void UpArrow(int n, char c){
                    for (int i = 0; i <= n; i++) {
                      for (int j = 0; j <= n; j++) {
                        if (j == n/2 || i + j == n/2 || i + j == 2*i+(n/2)) {
                          System.out.print(" " + c + " ");
                        } else {
                          System.out.print("   ");
                        }
                      }System.out.println();
                    }
  }

  public static void HourGlass (int n) {
    for (int i = 0; i < n; i++){
      for (int j = 0; j < 2*i+1; j++) {
        System.out.print(" ");
      } 
      for (int k = 0; k < n - i - 1; k++) {
        System.out.print("* ");
      }
      System.out.println();
    }
  }
    public static void main(String[] args) {
    // Triangle(7);
    // UpArrow(12, '#');
    HourGlass(7);
  }
}
