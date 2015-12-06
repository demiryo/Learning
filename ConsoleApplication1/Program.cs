using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
	class Program
	{
        static void MakeAGess()
        {
            Console.WriteLine(@"type any number");
            string input = Console.ReadLine();
            Console.WriteLine(@"time it by 5");
            string inputTimesFive = Console.ReadLine();


            int val = int.Parse(input);
            int answer = int.Parse(inputTimesFive);

            if (val * 5 == answer)
                Console.WriteLine(@"Correct! good for you!= (");
            else
                Console.WriteLine(@"horribile! are you egyptian!= )");
        }

		static void AnnoyingBanana()
		{
			Console.WriteLine("hi i like bananas! what do u think?");

			for (int i = 0; i < 20; i = i + 2)
			{
				string message = Console.ReadLine();
				Console.WriteLine("Loop no. " + i.ToString() + " : " + message + " respond!");
			}

			// Wait for any key
			Console.WriteLine("type to escape ebiss...");
			Console.ReadLine();
			// wait for 3 minutes then respond.
			Console.WriteLine(" O.K.i won't let u out. >= )");
		}

		static ConsoleKeyInfo outputmenu()
		{
			Console.Clear();
            Console.WriteLine("1. add");
			Console.WriteLine("2. subtraction");
			Console.WriteLine("3. multiplacation");
			Console.WriteLine("4. divide");
			Console.WriteLine("5. exit");

			return Console.ReadKey();
		}

		static void Main(string[] args)
		{
			ConsoleKeyInfo key;
			do {
				key = outputmenu();
			} while (key.Key != ConsoleKey.D5);
		}
	}
}
