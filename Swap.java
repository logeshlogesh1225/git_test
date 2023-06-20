class swap {
    public static void main(String[] args) {
        int x = 5;
        int y = 10;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("after swaping");

        int temp = x;
        x = y;
        y = temp;
        System.out.println("x = " + x);
        System.out.println("y = " + y);

    }
}