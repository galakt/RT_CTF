using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace Authorized_Persons_Only_30
{
    class Program
    {
        static void Main(string[] args)
        {
            // http://stackoverflow.com/questions/12373738/how-do-i-set-a-cookie-on-httpclients-httprequestmessage
            CookieContainer cookieContainer = new CookieContainer();
            HttpClientHandler handler = new HttpClientHandler { CookieContainer = cookieContainer };

            var uri = new Uri(@"http://hack.bckdr.in/CKK/index.php");
            HttpClient client = new HttpClient(handler);
            var str = client.GetStringAsync(uri);
            var result = str.Result;
            Console.WriteLine(result);
            PrintCookie(cookieContainer, uri);

            Console.WriteLine("_________________________________________");
            cookieContainer.Add(uri, new Cookie("admin", "1"));
            PrintCookie(cookieContainer, uri);
            var str2 = client.GetStringAsync(uri);
            var result2 = str2.Result;
            Console.WriteLine(result2);

            /*
             * 
             * Another varient
             * 
             */

            /*
            var baseAddress = new Uri("http://example.com");
            using (var handler = new HttpClientHandler { UseCookies = false })
            using (var client = new HttpClient(handler) { BaseAddress = baseAddress })
            {
                var message = new HttpRequestMessage(HttpMethod.Get, "/test");
                message.Headers.Add("Cookie", "cookie1=value1; cookie2=value2");
                var result = await client.SendAsync(message);
                result.EnsureSuccessStatusCode();
            }
            */

            Console.ReadLine();
        }

        private static void PrintCookie(CookieContainer cookieContainer, Uri uri)
        {
            foreach (Cookie item in cookieContainer.GetCookies(uri))
            {
                Console.WriteLine($"Name = {item.Name}, Value = {item.Value}");
            }
        }
    }
}
