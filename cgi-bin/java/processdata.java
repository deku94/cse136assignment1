import java.util.*;
import java.io.*;
import java.net.URLDecoder;

public class processdata
{
  private static Map<String, String> getParams(String queryString) throws UnsupportedEncodingException
  {
    String[] params = queryString.split("&");
    Map<String, String> map = new HashMap<>();
    for (String param : params)
    { 
      String name = URLDecoder.decode(param.split("=")[0], "UTF-8");
      // If user didn't enter anything don't add the param to the param map
      if (param.split("=").length > 1)
      {
        String value = URLDecoder.decode(param.split("=")[1], "UTF-8");
        map.put(name, value);
      }
    }
    return map; 
  }
  
  private static Map<String, String> getParamsPost()
  {
    try 
    {
      String postString = "";
      while (System.in.available() > 0)
      {
        postString += (char) System.in.read();
      }
      return getParams(postString);
    } catch (IOException e) {
      return new HashMap<String, String>();
    }
  }
  
  private static void printData(Map<String, String> params)
  {
    if (params.containsKey("magicnumber") && params.get("magicnumber") != null)
    { 
      try
      {
        int magicnumber = Integer.parseInt(params.get("magicnumber"));
        if (params.containsKey("username") && params.get("username") != null && 
          params.containsKey("password") && params.get("password") != null)
        {
          for (int i = 0; i < magicnumber; i++)  
          {
            System.out.println("<h1>Hello " + params.get("username") + " with a password of " +
              params.get("password") + "!</h1>");
          }
        }
        else
        {
          System.out.println("<h1>Please enter a username and a password.</h1>");
        }
      } catch (NumberFormatException e) {
        System.out.println("<h1>Please enter a valid magic number.</h1>");
      }
    }
    else
    {
      System.out.println("<h1>Please enter a magic number.</h1>");
    }
  }

  public static void main(String[] args) throws UnsupportedEncodingException
  {
    // Get the request parameters
    String requestMethod = System.getenv("REQUEST_METHOD");
    String queryString = System.getenv("QUERY_STRING");
    Map<String, String> params = new HashMap<>();
    if (requestMethod.equals("GET")) 
    {
      params = getParams(queryString); 
    }
    else
    {
      params = getParamsPost();
    }
    
    System.out.println("Content-type: text/html\n");
    System.out.println("<!doctype html>");
    System.out.println("<html><head><title>Hello Java Based CGI World</title></head><body>");
    printData(params); 
    System.out.println("</body></html>");
  }
} 
