import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.lang.NumberFormatException;

class ExceptionCost {
  private static final String STR = "abc";
  private static final String REGEX = "\\A[-]?[0-9]+\\z";
  private static final Pattern PATTERN = Pattern.compile(REGEX);
  public static void main(String args[]) throws Exception {

    if (args.length < 2) {
      System.err.println("usage : java ExceptionCost [type: plus or buffer] [count]");
      System.exit(1);
    }
    int count = Integer.parseInt(args[1]);

    long before = System.currentTimeMillis();
    if ("ex".equals(args[0])) {

      for (int i = 0; i < count; i++) {
        isNumberParse(STR);
      }

    } else if ("regex".equals(args[0])) {

      for (int i = 0; i < count; i++) {
        isNumberRegex(STR);
      }
    }
 
    System.out.println(String.format("%d ms", System.currentTimeMillis() - before));
    System.exit(0);
  }

  private static boolean isNumberParse(String val) {
    try {
      Integer.parseInt(val);
      return true;
    } catch (NumberFormatException nfex) {
      return false;
    }
  }

  private static boolean isNumberRegex(String val) {
    Matcher m1 = PATTERN.matcher(val);
    return m1.find();
  }
}