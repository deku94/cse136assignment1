import java.io.*;
import java.util.*;
import java.text.*;

public class Hello
{
  private static final String[] colors = {"aqua", "black", "blue", "fuchsia", "gray", 
    "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", 
    "white", "yellow"};

  public static void main (String args[])
  {
    Random random = new Random();
    Date date = new Date();
    DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd hh:mm:dd");
    dateFormat.setTimeZone(TimeZone.getTimeZone("America/Los_Angeles"));

    System.out.println("Content-type: text/html\n");
    System.out.println("<!doctype html>");
    System.out.println("<html><head><title>Hello Java Based CGI World</title></head>");
    System.out.println("<body style='background-color: " + 
      colors[random.nextInt(colors.length)] + "'><h1>Hello World from Java @ " + 
      dateFormat.format(date) + "</h1>");
    System.out.println("</body></html>");
  }
}
