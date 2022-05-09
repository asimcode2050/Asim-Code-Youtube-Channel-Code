/*
How to Build a Java GUI Calculator
Please Subscribe to Asim Code
https://youtu.be/duMNUwt5osw
*/
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class CalculatorGUI extends JFrame implements ActionListener {
    private final static int CBUTTONS = 16;
    private JPanel keyPadPanel;
    private JTextField accumulator;
    private JButton keyPad[];
    private String label[] = {
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "C", "0", "=", "/"
    };

    public CalculatorGUI(String title) {
        super(title);
        keyPadPanel = new JPanel();
        keyPadPanel.setLayout(new GridLayout(4, 4, 1, 1));
        keyPad = new JButton[CBUTTONS];
        for (int i = 0; i < keyPad.length; i++) {
            keyPad[i] = new JButton(label[i]);
            keyPad[i].addActionListener(this);
            keyPadPanel.add(keyPad[i]);

        }
        accumulator = new JTextField("0", 20);
        accumulator.setEditable(false);
        getContentPane().setLayout(new BorderLayout(10, 10));
        getContentPane().add("North", accumulator);
        getContentPane().add("Center", keyPadPanel);

    }

    public void actionPerformed(ActionEvent e) {
        JButton button = (JButton) e.getSource();
        String key = button.getText();
        accumulator.setText(accumulator.getText() + key);
    }

    public static void main(String[] args) {
        CalculatorGUI gui = new CalculatorGUI("Calculator GUI Demo");
        gui.setSize(200, 200);
        gui.setVisible(true);
        gui.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }

} // CalculatorGUI
