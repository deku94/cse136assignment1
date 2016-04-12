import java.util.*;

public class Env
{
  public static void main (String[] args) 
  {
    System.out.println("Content-type: text/html\n");
    System.out.println("<!doctype html>");
    System.out.println("<html><head><title>Environment Var Java</title></head><body>");
    System.out.println("<h1>Variables Sent By Server</h1>");
    System.out.println("<table><tr><th>Variable</th><th>Value</th></tr>");

    Map<String, String> env = System.getenv();
    Map<String, String> sortedEnv = new TreeMap<>(env);
    Map<String, String> req = new HashMap<>();    
    for (String envVar : sortedEnv.keySet())
    {
      if (envVar.contains("REQUEST_")) 
      {
        req.put(envVar, sortedEnv.get(envVar));
      }
      else 
      {
        System.out.println("<tr><td>" + envVar + "</td><td>" + sortedEnv.get(envVar) + "</td></tr>");
      }
    }

    System.out.println("</table>");
    System.out.println("<h1>Variables Sent By Browser</h1>");
    System.out.println("<table><tr><th>Variable</th><th>Value</th></tr>");
    for (String reqVar : req.keySet())
    {
      System.out.println("<tr><td>" + reqVar + "</td><td>" + req.get(reqVar) + "</td></tr>");
    } 
    
    System.out.println("</table></body></html>");	    
  }
} 
