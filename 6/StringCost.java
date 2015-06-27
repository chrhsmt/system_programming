class StringCost {

  public static void main(String[] args) {

    if (args.length < 2) {
      System.err.println("usage : java StringCost [type: plus or buffer] [count]");
      System.exit(1);
    }
    int count = Integer.parseInt(args[1]);

    long before = System.currentTimeMillis();
    if ("plus".equals(args[0])) {

      String buffer = "";
      for (int i = 0; i < count; i++) {
        buffer += "abc";
      }

    } else if ("buffer".equals(args[0])) {

      StringBuilder builder = new StringBuilder();
      for (int i = 0; i < count; i++) {
        builder.append("abc");
      }
    }
 
    System.out.println(String.format("%d ms", System.currentTimeMillis() - before));
    System.exit(0);
  }
}