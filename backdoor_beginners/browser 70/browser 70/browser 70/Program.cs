using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace browser_70
{
    class Program
    {
        static void Main(string[] args)
        {
            HttpClient client = new HttpClient();
            client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("SDSLabs", "1"));
            var str = client.GetStringAsync(new Uri(@"http://hack.bckdr.in/BRWSR/"));
            var result = str.Result;
            Console.WriteLine(result);
            Console.ReadLine();
        }
    }
}
