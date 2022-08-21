/*
BorderLayoutExample in Java Swing
Please Subscribe to Asim Code
https://youtu.be/qzp1V3es6_Y
*/
import javax.swing.*;
import java.awt.*;

public class BorderLayoutExample{
  public static void main(String[] args) {
  JFrame frame = new JFrame();
  JButton button = new JButton("Click Me!");
  frame.getContentPane().add(BorderLayout.EAST, button);
  frame.setSize(300,300);
  frame.setVisible(true);
}
}
